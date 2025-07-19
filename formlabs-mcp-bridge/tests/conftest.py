import pytest
import os
from unittest.mock import patch, MagicMock, AsyncMock


@pytest.fixture(autouse=True)
def setup_test_env():
    """Setup test environment variables"""
    test_env = {
        'CLIENT_ID': 'test_client_id',
        'CLIENT_SECRET': 'test_client_secret',
        'DASHBOARD_URL': 'http://localhost:3000'
    }
    
    with patch.dict(os.environ, test_env):
        yield


@pytest.fixture
def mock_token_manager():
    """Mock token manager for testing"""
    with patch('mcp.main.get_token_manager') as mock_get_tm:
        mock_tm = MagicMock()
        # Mock the token manager methods
        mock_tm.get_token = MagicMock(return_value="test_token")
        # Mock the token manager methods
        mock_tm.get_token = MagicMock(return_value="test_token")
        mock_tm.make_authenticated_request = AsyncMock()
        mock_get_tm.return_value = mock_tm
        yield mock_tm 