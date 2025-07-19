#!/usr/bin/env python3
"""
Advanced MCP analysis for Formlabs printer fleet
Provides comparative analysis and fleet management insights
"""

import asyncio
import httpx
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from collections import defaultdict


class AdvancedFormlabsAnalyzer:
    """Advanced analysis for Formlabs printer fleet"""
    
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
    
    async def get_formlabs_prints(self) -> List[Dict]:
        """Get latest prints"""
        response = await self.client.get(f"{self.base_url}/mcp/prints")
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()


class FleetAnalyzer:
    """Analyze entire printer fleet for insights"""
    
    def analyze_fleet_events(self, events: List[Dict], printers: List[Dict]) -> Dict:
        """Analyze events across all devices in the fleet"""
        
        # Group events by printer
        printer_events = defaultdict(list)
        for event in events:
            printer_id = event.get('printer')
            if printer_id:
                printer_events[printer_id].append(event)
        
        # Analyze each printer
        fleet_analysis = {
            "total_printers": len(printers),
            "active_printers": 0,
            "total_events": len(events),
            "printers": {},
            "fleet_summary": {},
            "insights": []
        }
        
        total_fleet_uptime = 0
        total_fleet_printing = 0
        successful_prints = 0
        failed_prints = 0
        
        for printer in printers:
            printer_id = printer['id']
            printer_events_list = printer_events.get(printer_id, [])
            
            if printer_events_list:
                analysis = self._analyze_single_printer(printer_events_list, printer)
                fleet_analysis["printers"][printer_id] = analysis
                fleet_analysis["active_printers"] += 1
                
                total_fleet_uptime += analysis['total_uptime_minutes']
                total_fleet_printing += analysis['total_printing_minutes']
                successful_prints += analysis['successful_prints']
                failed_prints += analysis['failed_prints']
        
        # Calculate fleet summary
        if total_fleet_uptime > 0:
            fleet_analysis["fleet_summary"] = {
                "total_uptime_minutes": round(total_fleet_uptime, 2),
                "total_printing_minutes": round(total_fleet_printing, 2),
                "fleet_utilization": round((total_fleet_printing / total_fleet_uptime) * 100, 2),
                "successful_prints": successful_prints,
                "failed_prints": failed_prints,
                "success_rate": round((successful_prints / (successful_prints + failed_prints)) * 100, 2) if (successful_prints + failed_prints) > 0 else 0,
                "avg_print_duration": round(total_fleet_printing / (successful_prints + failed_prints), 2) if (successful_prints + failed_prints) > 0 else 0
            }
        
        # Generate insights
        fleet_analysis["insights"] = self._generate_fleet_insights(fleet_analysis)
        
        return fleet_analysis
    
    def _analyze_single_printer(self, events: List[Dict], printer: Dict) -> Dict:
        """Analyze events for a single printer"""
        
        # Sort events by timestamp
        sorted_events = sorted(events, key=lambda x: x['updated_at'])
        
        # Track printing sessions
        printing_sessions = []
        current_session = None
        successful_prints = 0
        failed_prints = 0
        
        for event in sorted_events:
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
                    
                    if action == 'completed':
                        successful_prints += 1
                    else:
                        failed_prints += 1
                    
                    current_session = None
        
        # Calculate total printing time
        total_printing_minutes = 0
        for session in printing_sessions:
            if 'end_time' in session:
                start = datetime.fromisoformat(session['start_time'].replace('Z', '+00:00'))
                end = datetime.fromisoformat(session['end_time'].replace('Z', '+00:00'))
                duration = end - start
                total_printing_minutes += duration.total_seconds() / 60
        
        # Estimate uptime
        if sorted_events:
            first_event = sorted_events[0]
            last_event = sorted_events[-1]
            
            first_time = datetime.fromisoformat(first_event['updated_at'].replace('Z', '+00:00'))
            last_time = datetime.fromisoformat(last_event['updated_at'].replace('Z', '+00:00'))
            
            total_uptime_minutes = (last_time - first_time).total_seconds() / 60
        else:
            total_uptime_minutes = 0
        
        return {
            "name": printer['name'],
            "status": printer['status'],
            "total_events": len(events),
            "printing_sessions": len(printing_sessions),
            "successful_prints": successful_prints,
            "failed_prints": failed_prints,
            "success_rate": round((successful_prints / (successful_prints + failed_prints)) * 100, 2) if (successful_prints + failed_prints) > 0 else 0,
            "total_uptime_minutes": round(total_uptime_minutes, 2),
            "total_printing_minutes": round(total_printing_minutes, 2),
            "utilization_percentage": round((total_printing_minutes / total_uptime_minutes * 100) if total_uptime_minutes > 0 else 0, 2),
            "avg_print_duration": round(total_printing_minutes / (successful_prints + failed_prints), 2) if (successful_prints + failed_prints) > 0 else 0,
            "sessions": printing_sessions,
            "recent_events": sorted_events[-3:] if len(sorted_events) > 3 else sorted_events
        }
    
    def _generate_fleet_insights(self, analysis: Dict) -> List[str]:
        """Generate insights from fleet analysis"""
        insights = []
        summary = analysis.get("fleet_summary", {})
        printers = analysis.get("printers", {})
        
        if not summary:
            return ["No data available for insights"]
        
        # Utilization insights
        utilization = summary.get("fleet_utilization", 0)
        if utilization > 70:
            insights.append("🟢 High fleet utilization - consider adding more printers")
        elif utilization < 30:
            insights.append("🔴 Low fleet utilization - printers may be underutilized")
        else:
            insights.append("🟡 Moderate fleet utilization - good balance")
        
        # Success rate insights
        success_rate = summary.get("success_rate", 0)
        if success_rate < 80:
            insights.append("⚠️ Low success rate - investigate print failures")
        elif success_rate > 95:
            insights.append("✅ Excellent success rate - printers running well")
        
        # Individual printer insights
        for printer_id, printer_data in printers.items():
            printer_util = printer_data.get("utilization_percentage", 0)
            printer_success = printer_data.get("success_rate", 0)
            
            if printer_util < 20:
                insights.append(f"📉 {printer_data['name']} has low utilization ({printer_util}%)")
            if printer_success < 70:
                insights.append(f"⚠️ {printer_data['name']} has low success rate ({printer_success}%)")
        
        # Maintenance insights
        total_prints = summary.get("successful_prints", 0) + summary.get("failed_prints", 0)
        if total_prints > 50:
            insights.append("🔧 Consider scheduling maintenance - high print volume")
        
        return insights


async def run_advanced_analysis():
    """Run advanced fleet analysis"""
    
    print("🚀 Advanced Formlabs Fleet Analysis")
    print("=" * 60)
    
    analyzer = AdvancedFormlabsAnalyzer()
    fleet_analyzer = FleetAnalyzer()
    
    try:
        # Get all data
        print("\n📋 Gathering fleet data...")
        printers = await analyzer.get_formlabs_printers()
        yesterday = (datetime.now() - timedelta(days=1)).isoformat()
        events = await analyzer.get_formlabs_events(since=yesterday)
        prints = await analyzer.get_formlabs_prints()
        
        print(f"✅ Found {len(printers)} printers, {len(events)} events, {len(prints)} prints")
        
        # Analyze fleet
        print("\n📊 Analyzing fleet performance...")
        fleet_analysis = fleet_analyzer.analyze_fleet_events(events, printers)
        
        # Display results
        print("\n📈 Fleet Summary:")
        print("-" * 40)
        summary = fleet_analysis["fleet_summary"]
        print(f"Total Printers: {fleet_analysis['total_printers']}")
        print(f"Active Printers: {fleet_analysis['active_printers']}")
        print(f"Fleet Utilization: {summary.get('fleet_utilization', 0):.2f}%")
        print(f"Success Rate: {summary.get('success_rate', 0):.2f}%")
        print(f"Total Printing Time: {summary.get('total_printing_minutes', 0):.2f} minutes")
        print(f"Average Print Duration: {summary.get('avg_print_duration', 0):.2f} minutes")
        
        # Individual printer analysis
        print(f"\n🖨️ Individual Printer Analysis:")
        print("-" * 40)
        for printer_id, printer_data in fleet_analysis["printers"].items():
            print(f"\n{printer_data['name']} ({printer_id}):")
            print(f"  Status: {printer_data['status']}")
            print(f"  Utilization: {printer_data['utilization_percentage']:.2f}%")
            print(f"  Success Rate: {printer_data['success_rate']:.2f}%")
            print(f"  Prints: {printer_data['successful_prints']} successful, {printer_data['failed_prints']} failed")
            print(f"  Total Time: {printer_data['total_printing_minutes']:.2f} minutes printing")
        
        # Insights
        print(f"\n💡 Fleet Insights:")
        print("-" * 40)
        for insight in fleet_analysis["insights"]:
            print(f"  {insight}")
        
        # Recommendations
        print(f"\n🎯 Recommendations:")
        print("-" * 40)
        
        summary = fleet_analysis["fleet_summary"]
        utilization = summary.get("fleet_utilization", 0)
        success_rate = summary.get("success_rate", 0)
        
        if utilization < 30:
            print("  • Consider consolidating print jobs to fewer printers")
            print("  • Review print scheduling to increase utilization")
        elif utilization > 70:
            print("  • Consider adding more printers to the fleet")
            print("  • Optimize print queue management")
        
        if success_rate < 80:
            print("  • Investigate common causes of print failures")
            print("  • Review printer maintenance schedules")
            print("  • Check material quality and settings")
        
        # Performance comparison
        if len(fleet_analysis["printers"]) > 1:
            print(f"\n📊 Performance Comparison:")
            print("-" * 40)
            
            printers_list = list(fleet_analysis["printers"].items())
            printers_list.sort(key=lambda x: x[1]['utilization_percentage'], reverse=True)
            
            print("Ranked by Utilization:")
            for i, (printer_id, data) in enumerate(printers_list, 1):
                print(f"  {i}. {data['name']}: {data['utilization_percentage']:.2f}% utilization")
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        await analyzer.close()


if __name__ == "__main__":
    asyncio.run(run_advanced_analysis()) 