import os
import time
import asyncio
from datetime import datetime, timedelta
from typing import Optional
import httpx
from dotenv import load_dotenv

load_dotenv()


class TokenManager:
    """Manages Formlabs API authentication tokens with automatic refresh"""
    
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.base_url = "https://api.formlabs.com"
        self.token_url = f"{self.base_url}/developer/v1/o/token/"
        
        if not self.client_id or not self.client_secret:
            raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in environment variables")
        
        self.access_token: Optional[str] = None
        self.expires_at: Optional[datetime] = None
        self._lock = asyncio.Lock()
    
    async def get_token(self) -> str:
        """Get a valid access token, refreshing if necessary"""
        async with self._lock:
            # Check if token is still valid (refresh 5 minutes before expiry)
            if (self.access_token and self.expires_at and 
                datetime.now() < self.expires_at - timedelta(minutes=5)):
                return self.access_token
            
            # Get new token
            await self._refresh_token()
            return self.access_token
    
    async def _refresh_token(self, retry_count: int = 0) -> None:
        """Refresh the access token with retry logic"""
        max_retries = 3
        base_delay = 1.0
        
        try:
            async with httpx.AsyncClient() as client:
                data = {
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret
                }
                
                response = await client.post(
                    self.token_url,
                    data=data,
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    timeout=30.0
                )
                
                if response.status_code == 429:
                    # Rate limited - retry with exponential backoff
                    if retry_count < max_retries:
                        delay = base_delay * (2 ** retry_count)
                        await asyncio.sleep(delay)
                        await self._refresh_token(retry_count + 1)
                        return
                    else:
                        raise Exception("Rate limit exceeded after max retries")
                
                response.raise_for_status()
                token_data = response.json()
                
                self.access_token = token_data["access_token"]
                # Token expires in 24 hours (86400 seconds)
                self.expires_at = datetime.now() + timedelta(seconds=token_data.get("expires_in", 86400))
                
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise Exception("Invalid client credentials")
            elif e.response.status_code == 429:
                if retry_count < max_retries:
                    delay = base_delay * (2 ** retry_count)
                    await asyncio.sleep(delay)
                    await self._refresh_token(retry_count + 1)
                    return
                else:
                    raise Exception("Rate limit exceeded after max retries")
            else:
                raise Exception(f"Token refresh failed: {e.response.status_code}")
        except Exception as e:
            raise Exception(f"Token refresh failed: {str(e)}")
    
    async def make_authenticated_request(self, method: str, url: str, **kwargs) -> httpx.Response:
        """Make an authenticated request to the Formlabs API with retry logic"""
        max_retries = 3
        base_delay = 1.0
        
        for attempt in range(max_retries):
            try:
                token = await self.get_token()
                
                async with httpx.AsyncClient() as client:
                    headers = {
                        "Authorization": f"bearer {token}",
                        "Content-Type": "application/json",
                        **kwargs.get("headers", {})
                    }
                    
                    response = await client.request(
                        method,
                        url,
                        headers=headers,
                        timeout=30.0,
                        **{k: v for k, v in kwargs.items() if k != "headers"}
                    )
                    
                    if response.status_code == 401:
                        # Token expired, refresh and retry
                        self.access_token = None
                        self.expires_at = None
                        continue
                    elif response.status_code == 429:
                        # Rate limited - retry with exponential backoff
                        if attempt < max_retries - 1:
                            delay = base_delay * (2 ** attempt)
                            await asyncio.sleep(delay)
                            continue
                    
                    return response
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                delay = base_delay * (2 ** attempt)
                await asyncio.sleep(delay)
        
        raise Exception("Request failed after max retries")


# Token manager will be initialized when needed 