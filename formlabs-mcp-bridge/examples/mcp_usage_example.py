#!/usr/bin/env python3
"""
Comprehensive example of using Formlabs MCP tools
Demonstrates real-world usage scenarios for printer fleet management
"""

import asyncio
import httpx
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class FormlabsMCPClient:
    """Complete MCP client demonstrating all available tools"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient()
    
    # MCP Tool 1: get_formlabs_printers
    async def get_formlabs_printers(self) -> List[Dict]:
        """Get a list of all Formlabs printers with their status and details"""
        response = await self.client.get(f"{self.base_url}/mcp/printers")
        response.raise_for_status()
        return response.json()
    
    # MCP Tool 2: get_formlabs_events
    async def get_formlabs_events(self, since: Optional[str] = None) -> List[Dict]:
        """Get recent events from Formlabs printers with optional filtering"""
        params = {}
        if since:
            params["since"] = since
        
        response = await self.client.get(f"{self.base_url}/mcp/events", params=params)
        response.raise_for_status()
        return response.json()
    
    # MCP Tool 3: get_formlabs_prints
    async def get_formlabs_prints(self) -> List[Dict]:
        """Get the latest print jobs from Formlabs printers"""
        response = await self.client.get(f"{self.base_url}/mcp/prints")
        response.raise_for_status()
        return response.json()
    
    # MCP Tool 4: get_formlabs_printer_status
    async def get_formlabs_printer_status(self, printer_id: str) -> Dict:
        """Get detailed status of a specific Formlabs printer"""
        response = await self.client.get(f"{self.base_url}/mcp/printers/{printer_id}")
        response.raise_for_status()
        return response.json()
    
    # MCP Tool 5: monitor_formlabs_print
    async def monitor_formlabs_print(self, print_id: str) -> Dict:
        """Monitor a specific print job by its ID"""
        response = await self.client.get(f"{self.base_url}/mcp/prints/{print_id}")
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()


class PrinterFleetManager:
    """Example fleet management using MCP tools"""
    
    def __init__(self, mcp_client: FormlabsMCPClient):
        self.client = mcp_client
    
    async def daily_fleet_report(self) -> Dict:
        """Generate a daily fleet report using MCP tools"""
        print("📊 Generating Daily Fleet Report...")
        
        # Get all printers
        printers = await self.client.get_formlabs_printers()
        
        # Get events from last 24 hours
        yesterday = (datetime.now() - timedelta(days=1)).isoformat()
        events = await self.client.get_formlabs_events(since=yesterday)
        
        # Get latest prints
        prints = await self.client.get_formlabs_prints()
        
        # Analyze each printer
        printer_reports = {}
        for printer in printers:
            printer_id = printer['id']
            printer_status = await self.client.get_formlabs_printer_status(printer_id)
            
            # Get events for this printer
            printer_events = [e for e in events if e.get('printer') == printer_id]
            
            printer_reports[printer_id] = {
                "printer": printer,
                "status": printer_status,
                "events_count": len(printer_events),
                "recent_events": printer_events[-3:] if printer_events else []
            }
        
        return {
            "report_date": datetime.now().isoformat(),
            "total_printers": len(printers),
            "total_events": len(events),
            "total_prints": len(prints),
            "printers": printer_reports
        }
    
    async def monitor_active_prints(self) -> List[Dict]:
        """Monitor all currently active prints"""
        print("🖨️ Monitoring Active Prints...")
        
        prints = await self.client.get_formlabs_prints()
        active_prints = [p for p in prints if p['status'] in ['printing', 'preparing']]
        
        detailed_prints = []
        for print_job in active_prints:
            print_id = print_job['id']
            detailed_status = await self.client.monitor_formlabs_print(print_id)
            detailed_prints.append(detailed_status)
        
        return detailed_prints
    
    async def check_printer_health(self, printer_id: str) -> Dict:
        """Check health status of a specific printer"""
        print(f"🏥 Checking Health for Printer {printer_id}...")
        
        # Get printer status
        status = await self.client.get_formlabs_printer_status(printer_id)
        
        # Get recent events
        yesterday = (datetime.now() - timedelta(days=1)).isoformat()
        events = await self.client.get_formlabs_events(since=yesterday)
        printer_events = [e for e in events if e.get('printer') == printer_id]
        
        # Analyze health indicators
        error_events = [e for e in printer_events if 'error' in e.get('type', '').lower() or 'failed' in e.get('type', '').lower()]
        maintenance_events = [e for e in printer_events if 'maintenance' in e.get('type', '').lower()]
        
        health_score = 100
        issues = []
        
        if error_events:
            health_score -= len(error_events) * 10
            issues.append(f"{len(error_events)} error events in last 24 hours")
        
        if maintenance_events:
            health_score -= len(maintenance_events) * 5
            issues.append(f"{len(maintenance_events)} maintenance events in last 24 hours")
        
        if status['status'] == 'error':
            health_score -= 30
            issues.append("Printer currently in error state")
        
        return {
            "printer_id": printer_id,
            "printer_name": status['name'],
            "current_status": status['status'],
            "health_score": max(0, health_score),
            "issues": issues,
            "recent_events": len(printer_events),
            "error_events": len(error_events),
            "maintenance_events": len(maintenance_events)
        }
    
    async def get_print_job_history(self, printer_id: str, hours: int = 24) -> List[Dict]:
        """Get print job history for a specific printer"""
        print(f"📋 Getting Print History for Printer {printer_id}...")
        
        # Get events from specified time period
        since_time = (datetime.now() - timedelta(hours=hours)).isoformat()
        events = await self.client.get_formlabs_events(since=since_time)
        
        # Filter for print-related events for this printer
        print_events = [
            e for e in events 
            if e.get('printer') == printer_id and 
            'print' in e.get('type', '').lower()
        ]
        
        return print_events


async def demonstrate_mcp_usage():
    """Demonstrate comprehensive MCP tool usage"""
    
    print("🚀 Formlabs MCP Tools Demonstration")
    print("=" * 60)
    
    client = FormlabsMCPClient()
    fleet_manager = PrinterFleetManager(client)
    
    try:
        # Scenario 1: Daily Fleet Report
        print("\n📊 Scenario 1: Daily Fleet Report")
        print("-" * 40)
        report = await fleet_manager.daily_fleet_report()
        
        print(f"Report Date: {report['report_date']}")
        print(f"Total Printers: {report['total_printers']}")
        print(f"Total Events: {report['total_events']}")
        print(f"Total Prints: {report['total_prints']}")
        
        for printer_id, printer_data in report['printers'].items():
            printer = printer_data['printer']
            print(f"\n{printer['name']} ({printer_id}):")
            print(f"  Status: {printer['status']}")
            print(f"  Events: {printer_data['events_count']}")
            print(f"  Location: {printer.get('location', 'Unknown')}")
        
        # Scenario 2: Monitor Active Prints
        print("\n🖨️ Scenario 2: Monitor Active Prints")
        print("-" * 40)
        active_prints = await fleet_manager.monitor_active_prints()
        
        if active_prints:
            for print_job in active_prints:
                print(f"Print: {print_job['name']} ({print_job['id']})")
                print(f"  Status: {print_job['status']}")
                print(f"  Printer: {print_job['printer']}")
                print(f"  Material: {print_job.get('material', 'Unknown')}")
                print(f"  Message: {print_job.get('message', 'No message')}")
        else:
            print("No active prints found")
        
        # Scenario 3: Check Printer Health
        print("\n🏥 Scenario 3: Printer Health Check")
        print("-" * 40)
        for printer in report['printers']:
            health = await fleet_manager.check_printer_health(printer)
            print(f"\n{health['printer_name']} ({health['printer_id']}):")
            print(f"  Health Score: {health['health_score']}/100")
            print(f"  Current Status: {health['current_status']}")
            if health['issues']:
                print(f"  Issues: {', '.join(health['issues'])}")
            else:
                print("  Issues: None detected")
        
        # Scenario 4: Print Job History
        print("\n📋 Scenario 4: Print Job History")
        print("-" * 40)
        for printer_id in report['printers']:
            history = await fleet_manager.get_print_job_history(printer_id, hours=24)
            printer_name = report['printers'][printer_id]['printer']['name']
            print(f"\n{printer_name} - Last 24 hours:")
            print(f"  Print events: {len(history)}")
            
            for event in history[-3:]:  # Show last 3 events
                print(f"    • {event['name']} - {event['updated_at']}")
        
        # Scenario 5: Real-time Monitoring Example
        print("\n⏱️ Scenario 5: Real-time Monitoring Example")
        print("-" * 40)
        print("Simulating real-time monitoring loop...")
        
        # Get current state
        printers = await client.get_formlabs_printers()
        events = await client.get_formlabs_events(since=(datetime.now() - timedelta(minutes=5)).isoformat())
        
        print(f"Current printer status:")
        for printer in printers:
            print(f"  {printer['name']}: {printer['status']}")
        
        if events:
            print(f"Recent events (last 5 minutes): {len(events)}")
            for event in events:
                print(f"  • {event['name']} on {event['printer']}")
        else:
            print("No recent events")
        
        print("\n✅ MCP Tools Demonstration Complete!")
        print("\n💡 Key Insights:")
        print("  • All operations are read-only (no control over printers)")
        print("  • Events provide the primary way to detect status changes")
        print("  • No real-time sensor data streams available")
        print("  • Authentication and rate limiting must be handled")
        print("  • Data normalization required for dashboard consumption")
        
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(demonstrate_mcp_usage()) 