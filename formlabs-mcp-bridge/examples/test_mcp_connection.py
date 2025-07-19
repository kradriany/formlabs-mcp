#!/usr/bin/env python3
"""
Test MCP connection to Formlabs emulator
Analyzes device uptime and printing time from events
"""

import asyncio
import httpx
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class FormlabsMCPTester:
    """Test connection to Formlabs MCP emulator"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient()
    
    async def get_formlabs_printers(self) -> List[Dict]:
        """Get list of all printers"""
        response = await self.client.get(f"{self.base_url}/mcp/printers")
        response.raise_for_status()
        return response.json()
    
    async def get_formlabs_events(self, since: Optional[str] = None) -> List[Dict]:
        """Get events with optional since filter"""
        params = {}
        if since:
            params["since"] = since
        
        response = await self.client.get(f"{self.base_url}/mcp/events", params=params)
        response.raise_for_status()
        return response.json()
    
    async def get_formlabs_printer_status(self, printer_id: str) -> Dict:
        """Get specific printer status"""
        response = await self.client.get(f"{self.base_url}/mcp/printers/{printer_id}")
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()


class DeviceAnalyzer:
    """Analyze device uptime and printing time from events"""
    
    def __init__(self):
        self.device_states = {}  # Track device state over time
        self.printing_sessions = {}  # Track printing sessions per device
    
    def analyze_events(self, events: List[Dict], target_device: str) -> Dict:
        """Analyze events to determine uptime and printing time for target device"""
        
        # Sort events by timestamp
        sorted_events = sorted(events, key=lambda x: x['updated_at'])
        
        # Track state changes for target device
        device_events = [e for e in sorted_events if e.get('printer') == target_device]
        
        if not device_events:
            return {
                "device_found": False,
                "message": f"No events found for device {target_device}"
            }
        
        # Analyze printing sessions
        printing_sessions = []
        current_session = None
        
        for event in device_events:
            event_type = event.get('type', '')
            action = event.get('action', '')
            
            # Detect print start
            if event_type == 'print_started' and action == 'started':
                if current_session is None:
                    current_session = {
                        'start_time': event['updated_at'],
                        'start_event': event
                    }
            
            # Detect print completion or failure
            elif event_type in ['print_completed', 'print_failed'] and action in ['completed', 'failed']:
                if current_session is not None:
                    current_session['end_time'] = event['updated_at']
                    current_session['end_event'] = event
                    current_session['status'] = action
                    printing_sessions.append(current_session)
                    current_session = None
        
        # Calculate total printing time
        total_printing_minutes = 0
        for session in printing_sessions:
            if 'end_time' in session:
                start = datetime.fromisoformat(session['start_time'].replace('Z', '+00:00'))
                end = datetime.fromisoformat(session['end_time'].replace('Z', '+00:00'))
                duration = end - start
                total_printing_minutes += duration.total_seconds() / 60
        
        # Estimate uptime (time between first and last event)
        if device_events:
            first_event = device_events[0]
            last_event = device_events[-1]
            
            first_time = datetime.fromisoformat(first_event['updated_at'].replace('Z', '+00:00'))
            last_time = datetime.fromisoformat(last_event['updated_at'].replace('Z', '+00:00'))
            
            total_uptime_minutes = (last_time - first_time).total_seconds() / 60
        else:
            total_uptime_minutes = 0
        
        return {
            "device_found": True,
            "target_device": target_device,
            "total_events": len(device_events),
            "printing_sessions": len(printing_sessions),
            "total_uptime_minutes": round(total_uptime_minutes, 2),
            "total_printing_minutes": round(total_printing_minutes, 2),
            "uptime_percentage": round((total_printing_minutes / total_uptime_minutes * 100) if total_uptime_minutes > 0 else 0, 2),
            "sessions": printing_sessions,
            "recent_events": device_events[-5:] if len(device_events) > 5 else device_events
        }


async def test_mcp_connection():
    """Main test function"""
    
    print("🔌 Testing MCP Connection to Formlabs Emulator")
    print("=" * 60)
    
    # Initialize tester and analyzer
    tester = FormlabsMCPTester()
    analyzer = DeviceAnalyzer()
    
    try:
        # 1. Get list of all devices
        print("\n📋 Step 1: Getting list of all devices...")
        printers = await tester.get_formlabs_printers()
        
        if not printers:
            print("❌ No printers found in the system")
            return
        
        print(f"✅ Found {len(printers)} printer(s):")
        for printer in printers:
            print(f"   • {printer['name']} ({printer['id']}) - {printer['status']}")
        
        # 2. Check for target device
        target_device = "PRINTER001"  # We can make this configurable
        print(f"\n🎯 Step 2: Checking for target device '{target_device}'...")
        
        target_found = any(p['id'] == target_device for p in printers)
        if not target_found:
            print(f"❌ Target device '{target_device}' not found")
            print("Available devices:")
            for printer in printers:
                print(f"   • {printer['id']}")
            return
        
        print(f"✅ Target device '{target_device}' found!")
        
        # 3. Get events from last 24 hours
        print("\n📊 Step 3: Getting events from last 24 hours...")
        yesterday = (datetime.now() - timedelta(days=1)).isoformat()
        events = await tester.get_formlabs_events(since=yesterday)
        
        print(f"✅ Found {len(events)} events in the last 24 hours")
        
        # 4. Analyze device uptime and printing time
        print(f"\n📈 Step 4: Analyzing uptime and printing time for '{target_device}'...")
        analysis = analyzer.analyze_events(events, target_device)
        
        if not analysis['device_found']:
            print(f"❌ {analysis['message']}")
            return
        
        # 5. Display results
        print("\n📊 Analysis Results:")
        print("-" * 40)
        print(f"Target Device: {analysis['target_device']}")
        print(f"Total Events: {analysis['total_events']}")
        print(f"Printing Sessions: {analysis['printing_sessions']}")
        print(f"Total Uptime: {analysis['total_uptime_minutes']:.2f} minutes")
        print(f"Total Printing Time: {analysis['total_printing_minutes']:.2f} minutes")
        print(f"Uptime Percentage: {analysis['uptime_percentage']:.2f}%")
        
        # 6. Show recent events
        if analysis['recent_events']:
            print(f"\n🕒 Recent Events for {target_device}:")
            for event in analysis['recent_events']:
                print(f"   • {event['name']} - {event['updated_at']}")
        
        # 7. Show printing sessions
        if analysis['sessions']:
            print(f"\n🖨️ Printing Sessions for {target_device}:")
            for i, session in enumerate(analysis['sessions'], 1):
                start_time = session['start_time']
                end_time = session.get('end_time', 'Ongoing')
                status = session.get('status', 'Unknown')
                print(f"   {i}. {start_time} → {end_time} ({status})")
        
        # 8. Summary
        print(f"\n📋 Summary:")
        print(f"   • Device {target_device} was active for {analysis['total_uptime_minutes']:.2f} minutes")
        print(f"   • Spent {analysis['total_printing_minutes']:.2f} minutes printing")
        print(f"   • Utilization rate: {analysis['uptime_percentage']:.2f}%")
        
        if analysis['uptime_percentage'] > 50:
            print("   🟢 High utilization - device is being used effectively")
        elif analysis['uptime_percentage'] > 20:
            print("   🟡 Moderate utilization - device has room for more jobs")
        else:
            print("   🔴 Low utilization - device may be underutilized")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        await tester.close()


if __name__ == "__main__":
    asyncio.run(test_mcp_connection()) 