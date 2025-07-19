import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime, timedelta
import httpx

from mcp.auth import TokenManager


@pytest.fixture
def token_manager():
    """Create a token manager with mock credentials"""
    with patch.dict('os.environ', {
        'CLIENT_ID': 'test_client_id',
        'CLIENT_SECRET': 'test_client_secret'
    }):
        return TokenManager()


@pytest.mark.asyncio
async def test_token_manager_initialization():
    """Test token manager initializes correctly with valid credentials"""
    with patch.dict('os.environ', {
        'CLIENT_ID': 'test_client_id',
        'CLIENT_SECRET': 'test_client_secret'
    }):
        tm = TokenManager()
        assert tm.client_id == 'test_client_id'
        assert tm.client_secret == 'test_client_secret'
        assert tm.access_token is None
        assert tm.expires_at is None


@pytest.mark.asyncio
async def test_token_manager_missing_credentials():
    """Test token manager raises error with missing credentials"""
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError, match="CLIENT_ID and CLIENT_SECRET must be set"):
            TokenManager()


@pytest.mark.asyncio
async def test_get_token_success(token_manager):
    """Test successful token retrieval"""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "access_token": "test_token_123",
        "expires_in": 86400
    }
    mock_response.raise_for_status.return_value = None
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        token = await token_manager.get_token()
        
        assert token == "test_token_123"
        assert token_manager.access_token == "test_token_123"
        assert token_manager.expires_at is not None


@pytest.mark.asyncio
async def test_get_token_401_error(token_manager):
    """Test token refresh fails with 401 (invalid credentials)"""
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "401 Unauthorized", request=MagicMock(), response=mock_response
    )
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        with pytest.raises(Exception, match="Invalid client credentials"):
            await token_manager.get_token()


@pytest.mark.asyncio
async def test_get_token_429_retry_success(token_manager):
    """Test token refresh succeeds after 429 retry"""
    # First call returns 429, second call succeeds
    mock_response_429 = MagicMock()
    mock_response_429.status_code = 429
    mock_response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
        "429 Too Many Requests", request=MagicMock(), response=mock_response_429
    )
    
    mock_response_success = MagicMock()
    mock_response_success.json.return_value = {
        "access_token": "test_token_123",
        "expires_in": 86400
    }
    mock_response_success.raise_for_status.return_value = None
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.post.side_effect = [
            mock_response_429,
            mock_response_success
        ]
        
        token = await token_manager.get_token()
        
        assert token == "test_token_123"
        # Verify post was called twice (retry)
        assert mock_client.return_value.__aenter__.return_value.post.call_count == 2


@pytest.mark.asyncio
async def test_get_token_429_max_retries_exceeded(token_manager):
    """Test token refresh fails after max retries"""
    mock_response = MagicMock()
    mock_response.status_code = 429
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "429 Too Many Requests", request=MagicMock(), response=mock_response
    )
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        with pytest.raises(Exception, match="Rate limit exceeded after max retries"):
            await token_manager.get_token()


@pytest.mark.asyncio
async def test_token_not_expired(token_manager):
    """Test token is returned when not expired"""
    # Set a valid token
    token_manager.access_token = "valid_token"
    token_manager.expires_at = datetime.now() + timedelta(hours=1)
    
    token = await token_manager.get_token()
    assert token == "valid_token"


@pytest.mark.asyncio
async def test_token_refresh_before_expiry(token_manager):
    """Test token is refreshed 5 minutes before expiry"""
    # Set a token that expires in 3 minutes (should trigger refresh)
    token_manager.access_token = "old_token"
    token_manager.expires_at = datetime.now() + timedelta(minutes=3)
    
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "access_token": "new_token_123",
        "expires_in": 86400
    }
    mock_response.raise_for_status.return_value = None
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        token = await token_manager.get_token()
        
        assert token == "new_token_123"
        assert token_manager.access_token == "new_token_123"


@pytest.mark.asyncio
async def test_make_authenticated_request_success(token_manager):
    """Test successful authenticated request"""
    # Mock token
    token_manager.access_token = "test_token"
    token_manager.expires_at = datetime.now() + timedelta(hours=1)
    
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "test"}
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.request.return_value = mock_response
        
        response = await token_manager.make_authenticated_request(
            "GET", "https://api.formlabs.com/test"
        )
        
        assert response.status_code == 200
        # Verify Authorization header was set
        call_args = mock_client.return_value.__aenter__.return_value.request.call_args
        assert "Authorization" in call_args[1]["headers"]
        assert call_args[1]["headers"]["Authorization"] == "bearer test_token"


@pytest.mark.asyncio
async def test_make_authenticated_request_401_refresh(token_manager):
    """Test authenticated request refreshes token on 401"""
    # Mock initial token
    token_manager.access_token = "old_token"
    token_manager.expires_at = datetime.now() + timedelta(hours=1)
    
    # First request returns 401, second succeeds
    mock_response_401 = MagicMock()
    mock_response_401.status_code = 401
    
    mock_response_success = MagicMock()
    mock_response_success.status_code = 200
    mock_response_success.json.return_value = {"data": "test"}
    
    # Mock token refresh
    mock_token_response = MagicMock()
    mock_token_response.json.return_value = {
        "access_token": "new_token_123",
        "expires_in": 86400
    }
    mock_token_response.raise_for_status.return_value = None
    
    with patch('httpx.AsyncClient') as mock_client:
        mock_client.return_value.__aenter__.return_value.request.side_effect = [
            mock_response_401,
            mock_response_success
        ]
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_token_response
        
        response = await token_manager.make_authenticated_request(
            "GET", "https://api.formlabs.com/test"
        )
        
        assert response.status_code == 200
        # Verify token was refreshed
        assert token_manager.access_token == "new_token_123" 