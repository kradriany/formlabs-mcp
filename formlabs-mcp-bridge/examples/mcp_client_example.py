#!/usr/bin/env python3
"""
Example client demonstrating how to use the Formlabs MCP tools
"""

import httpx
import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List


class FormlabsMCPClient:
    """Client for interacting with the Formlabs MCP bridge"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient()
    
    async def get_formlabs_printers(self) -> List[Dict[str, Any]]:
        """Get a list of all Formlabs printers with their status and details"""
        response = await self.client.get(f"{self.base_url}/mcp/printers")
        response.raise_for_status()
        return response.json()
    
    async def get_formlabs_events(self, since: str = None) -> List[Dict[str, Any]]:
        """Get recent events from Formlabs printers with optional filtering"""
        params = {}
        if since:
            params["since"] = since
        
        response = await self.client.get(f"{self.base_url}/mcp/events", params=params)
        response.raise_for_status()
        return response.json()
    
    async def get_formlabs_prints(self) -> List[Dict[str, Any]]:
        """Get the latest print jobs from Formlabs printers"""
        response = await self.client.get(f"{self.base_url}/mcp/prints")
        response.raise_for_status()
        return response.json()
    
    async def get_formlabs_printer_status(self, printer_id: str) -> Dict[str, Any]:
        """Get detailed status of a specific Formlabs printer"""
        response = await self.client.get(f"{self.base_url}/mcp/printers/{printer_id}")
        response.raise_for_status()
        return response.json()
    
    async def monitor_formlabs_print(self, print_id: str) -> Dict[str, Any]:
        """Monitor a specific print job by its ID"""
        response = await self.client.get(f"{self.base_url}/mcp/prints/{print_id}")
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()


async def main():
    """Example usage of the Formlabs MCP client"""
    
    client = FormlabsMCPClient()
    
    try:
        print("🚀 Formlabs MCP Client Example")
        print("=" * 50)
        
        # 1. Get all printers
        print("\n📋 1. Getting all printers...")
        printers = await client.get_formlabs_printers()
        for printer in printers:
            print(f"   • {printer['name']} ({printer['id']}) - {printer['status']}")
            print(f"     Location: {printer['location']}, Firmware: {printer['firmware_version']}")
        
        # 2. Get recent events
        print("\n📊 2. Getting recent events...")
        events = await client.get_formlabs_events()
        for event in events:
            print(f"   • {event['name']} - {event['status']}")
            print(f"     Printer: {event['printer']}, Message: {event['message']}")
        
        # 3. Get latest prints
        print("\n🖨️  3. Getting latest prints...")
        prints = await client.get_formlabs_prints()
        for print_job in prints:
            print(f"   • {print_job['name']} ({print_job['id']}) - {print_job['status']}")
            print(f"     Material: {print_job['material']}, Volume: {print_job['volume_ml']}ml")
        
        # 4. Get specific printer status
        print("\n🔍 4. Getting specific printer status...")
        printer_status = await client.get_formlabs_printer_status("PRINTER001")
        print(f"   • {printer_status['name']} - {printer_status['status']}")
        print(f"     Message: {printer_status['message']}")
        
        # 5. Monitor specific print
        print("\n📈 5. Monitoring specific print...")
        print_status = await client.monitor_formlabs_print("print-123")
        print(f"   • {print_status['name']} - {print_status['status']}")
        print(f"     Progress: {print_status['message']}")
        
        # 6. Get events since a specific time
        print("\n⏰ 6. Getting events since 1 hour ago...")
        one_hour_ago = (datetime.utcnow() - timedelta(hours=1)).isoformat()
        recent_events = await client.get_formlabs_events(since=one_hour_ago)
        print(f"   Found {len(recent_events)} events in the last hour")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main()) 