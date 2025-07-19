from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import datetime, timedelta
import httpx

from .auth import TokenManager
from .schemas import PrinterResponse, EventResponse, PrintResponse, ErrorResponse

app = FastAPI(
    title="MCP Formlabs API Bridge",
    description="Model-Context Protocol microservice bridging Formlabs IoT REST API",
    version="1.0.0"
)

FORMLABS_BASE_URL = "https://api.formlabs.com"

# Token manager will be initialized lazily
_token_manager = None

def get_token_manager():
    """Get the token manager instance, creating it if necessary"""
    global _token_manager
    if _token_manager is None:
        _token_manager = TokenManager()
    return _token_manager


def emulated_printers():
    now = datetime.utcnow()
    return [
        PrinterResponse(
            id="PRINTER001",
            name="Lab Printer",
            status="idle",
            updated_at=now,
            location="Lab A",
            firmware_version="2.1.0",
            message=None
        ),
        PrinterResponse(
            id="PRINTER002",
            name="Production Printer",
            status="printing",
            updated_at=now,
            location="Production Floor",
            firmware_version="2.0.5",
            message="Currently printing job #123"
        )
    ]

def emulated_events():
    now = datetime.utcnow()
    
    # Create events over the last 24 hours for realistic analysis
    events = []
    
    # 24 hours ago - printer startup
    startup_time = now - timedelta(hours=24)
    events.append(EventResponse(
        id=1,
        name="Printer Online - online",
        status="active",
        updated_at=startup_time,
        type="printer_online",
        action="online",
        printer="PRINTER001",
        message="Printer came online"
    ))
    
    # 23 hours ago - first print started
    first_print_start = now - timedelta(hours=23)
    events.append(EventResponse(
        id=2,
        name="Print Started - started",
        status="active",
        updated_at=first_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # 21 hours ago - first print completed
    first_print_end = now - timedelta(hours=21)
    events.append(EventResponse(
        id=3,
        name="Print Completed - completed",
        status="active",
        updated_at=first_print_end,
        type="print_completed",
        action="completed",
        printer="PRINTER001",
        message="Print job finished successfully"
    ))
    
    # 20 hours ago - second print started
    second_print_start = now - timedelta(hours=20)
    events.append(EventResponse(
        id=4,
        name="Print Started - started",
        status="active",
        updated_at=second_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # 18 hours ago - second print completed
    second_print_end = now - timedelta(hours=18)
    events.append(EventResponse(
        id=5,
        name="Print Completed - completed",
        status="active",
        updated_at=second_print_end,
        type="print_completed",
        action="completed",
        printer="PRINTER001",
        message="Print job finished successfully"
    ))
    
    # 16 hours ago - third print started
    third_print_start = now - timedelta(hours=16)
    events.append(EventResponse(
        id=6,
        name="Print Started - started",
        status="active",
        updated_at=third_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # 14 hours ago - third print failed
    third_print_fail = now - timedelta(hours=14)
    events.append(EventResponse(
        id=7,
        name="Print Failed - failed",
        status="active",
        updated_at=third_print_fail,
        type="print_failed",
        action="failed",
        printer="PRINTER001",
        message="Print job failed due to material issue"
    ))
    
    # 12 hours ago - fourth print started
    fourth_print_start = now - timedelta(hours=12)
    events.append(EventResponse(
        id=8,
        name="Print Started - started",
        status="active",
        updated_at=fourth_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # 10 hours ago - fourth print completed
    fourth_print_end = now - timedelta(hours=10)
    events.append(EventResponse(
        id=9,
        name="Print Completed - completed",
        status="active",
        updated_at=fourth_print_end,
        type="print_completed",
        action="completed",
        printer="PRINTER001",
        message="Print job finished successfully"
    ))
    
    # 8 hours ago - maintenance event
    maintenance_time = now - timedelta(hours=8)
    events.append(EventResponse(
        id=10,
        name="Maintenance Required - maintenance",
        status="active",
        updated_at=maintenance_time,
        type="maintenance_required",
        action="maintenance",
        printer="PRINTER001",
        message="Maintenance required - resin tank needs cleaning"
    ))
    
    # 6 hours ago - maintenance completed
    maintenance_done = now - timedelta(hours=6)
    events.append(EventResponse(
        id=11,
        name="Maintenance Completed - completed",
        status="active",
        updated_at=maintenance_done,
        type="maintenance_completed",
        action="completed",
        printer="PRINTER001",
        message="Maintenance completed successfully"
    ))
    
    # 4 hours ago - fifth print started
    fifth_print_start = now - timedelta(hours=4)
    events.append(EventResponse(
        id=12,
        name="Print Started - started",
        status="active",
        updated_at=fifth_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # 2 hours ago - fifth print completed
    fifth_print_end = now - timedelta(hours=2)
    events.append(EventResponse(
        id=13,
        name="Print Completed - completed",
        status="active",
        updated_at=fifth_print_end,
        type="print_completed",
        action="completed",
        printer="PRINTER001",
        message="Print job finished successfully"
    ))
    
    # 1 hour ago - current print started
    current_print_start = now - timedelta(hours=1)
    events.append(EventResponse(
        id=14,
        name="Print Started - started",
        status="active",
        updated_at=current_print_start,
        type="print_started",
        action="started",
        printer="PRINTER001",
        message="Print job started"
    ))
    
    # Add some events for PRINTER002 as well
    events.append(EventResponse(
        id=15,
        name="Print Started - started",
        status="active",
        updated_at=now - timedelta(minutes=30),
        type="print_started",
        action="started",
        printer="PRINTER002",
        message="New print job started"
    ))
    
    return events

def emulated_prints():
    now = datetime.utcnow()
    return [
        PrintResponse(
            id="print-123",
            name="Test Print",
            status="finished",
            updated_at=now,
            material="Resin A",
            volume_ml=25.5,
            layer_count=1000,
            printer="PRINTER001",
            message="Print completed successfully"
        ),
        PrintResponse(
            id="print-124",
            name="Production Part",
            status="printing",
            updated_at=now - timedelta(minutes=30),
            material="Resin B",
            volume_ml=45.2,
            layer_count=1500,
            printer="PRINTER002",
            message="Currently printing layer 750/1500"
        )
    ]

def emulated_printer_status(printer_id: str):
    now = datetime.utcnow()
    if printer_id == "PRINTER001":
        return PrinterResponse(
            id="PRINTER001",
            name="Lab Printer",
            status="idle",
            updated_at=now,
            location="Lab A",
            firmware_version="2.1.0",
            message="Ready for next print job"
        )
    elif printer_id == "PRINTER002":
        return PrinterResponse(
            id="PRINTER002",
            name="Production Printer",
            status="printing",
            updated_at=now,
            location="Production Floor",
            firmware_version="2.0.5",
            message="Currently printing job #124 - 45% complete"
        )
    else:
        raise HTTPException(status_code=404, detail=f"Printer {printer_id} not found")

def emulated_print_status(print_id: str):
    now = datetime.utcnow()
    if print_id == "print-123":
        return PrintResponse(
            id="print-123",
            name="Test Print",
            status="finished",
            updated_at=now,
            material="Resin A",
            volume_ml=25.5,
            layer_count=1000,
            printer="PRINTER001",
            message="Print completed successfully - ready for post-processing"
        )
    elif print_id == "print-124":
        return PrintResponse(
            id="print-124",
            name="Production Part",
            status="printing",
            updated_at=now,
            material="Resin B",
            volume_ml=45.2,
            layer_count=1500,
            printer="PRINTER002",
            message="Currently printing layer 750/1500 - 50% complete"
        )
    else:
        raise HTTPException(status_code=404, detail=f"Print job {print_id} not found")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "MCP Formlabs API Bridge is running"}


@app.get("/mcp/printers", response_model=List[PrinterResponse])
async def get_printers():
    """Get simplified printer list"""
    try:
        response = await get_token_manager().make_authenticated_request(
            "GET", 
            f"{FORMLABS_BASE_URL}/developer/v1/printers/"
        )
        response.raise_for_status()
        
        printers_data = response.json()
        normalized_printers = []
        
        for printer in printers_data:
            # Extract status from printer_status if available
            status = "unknown"
            if printer.get("printer_status"):
                status = printer["printer_status"].get("status", "unknown")
            
            # Get last modified time
            updated_at = datetime.now()
            if printer.get("printer_status", {}).get("last_modified"):
                try:
                    updated_at = datetime.fromisoformat(
                        printer["printer_status"]["last_modified"].replace("Z", "+00:00")
                    )
                except:
                    pass
            
            normalized_printers.append(PrinterResponse(
                id=printer["serial"],
                name=printer.get("alias", printer["serial"]),
                status=status,
                updated_at=updated_at,
                location=printer.get("location"),
                firmware_version=printer.get("firmware_version")
            ))
        
        return normalized_printers
        
    except Exception as e:
        # Return emulated data if real API fails
        return emulated_printers()


@app.get("/mcp/events", response_model=List[EventResponse])
async def get_events(since: Optional[str] = Query(None, description="ISO 8601 timestamp")):
    """Get recent events with optional since filter"""
    try:
        params = {"per_page": 50}  # Limit to recent events
        
        if since:
            # Add 1 second to since to avoid duplicate events
            try:
                since_dt = datetime.fromisoformat(since.replace("Z", "+00:00"))
                since_dt += timedelta(seconds=1)
                params["date__gt"] = since_dt.isoformat()
            except ValueError:
                raise HTTPException(status_code=400, detail="Invalid since parameter format")
        
        response = await get_token_manager().make_authenticated_request(
            "GET", 
            f"{FORMLABS_BASE_URL}/developer/v1/events/",
            params=params
        )
        response.raise_for_status()
        
        events_data = response.json()
        normalized_events = []
        
        for event in events_data.get("results", []):
            # Parse created_at timestamp
            updated_at = datetime.now()
            if event.get("created_at"):
                try:
                    updated_at = datetime.fromisoformat(
                        event["created_at"].replace("Z", "+00:00")
                    )
                except:
                    pass
            
            # Create a meaningful name from event type and action
            name = f"{event.get('type_label', event.get('type', 'Unknown'))} - {event.get('action', 'Unknown')}"
            
            normalized_events.append(EventResponse(
                id=event["id"],
                name=name,
                status="active" if not event.get("was_read", False) else "read",
                updated_at=updated_at,
                type=event.get("type", "unknown"),
                action=event.get("action", "unknown"),
                printer=event.get("printer"),
                message=event.get("message")
            ))
        
        return normalized_events
        
    except Exception as e:
        # Return emulated data if real API fails
        return emulated_events()


@app.get("/mcp/prints", response_model=List[PrintResponse])
async def get_prints():
    """Get latest prints"""
    try:
        params = {
            "per_page": 20,  # Limit to recent prints
            "ordering": "-created_at"  # Most recent first
        }
        
        response = await get_token_manager().make_authenticated_request(
            "GET", 
            f"{FORMLABS_BASE_URL}/developer/v1/prints/",
            params=params
        )
        response.raise_for_status()
        
        prints_data = response.json()
        normalized_prints = []
        
        for print_run in prints_data.get("results", []):
            # Parse created_at timestamp
            updated_at = datetime.now()
            if print_run.get("created_at"):
                try:
                    updated_at = datetime.fromisoformat(
                        print_run["created_at"].replace("Z", "+00:00")
                    )
                except:
                    pass
            
            # Determine status
            status = print_run.get("status", "unknown").lower()
            
            normalized_prints.append(PrintResponse(
                id=print_run["guid"],
                name=print_run.get("name", "Unnamed Print"),
                status=status,
                updated_at=updated_at,
                material=print_run.get("material"),
                volume_ml=print_run.get("volume_ml"),
                layer_count=print_run.get("layer_count"),
                printer=print_run.get("printer"),
                message=print_run.get("message")
            ))
        
        return normalized_prints
        
    except Exception as e:
        # Return emulated data if real API fails
        return emulated_prints()


@app.get("/mcp/printers/{printer_id}", response_model=PrinterResponse)
async def get_printer_status(printer_id: str):
    """Get detailed status of a specific printer"""
    try:
        response = await get_token_manager().make_authenticated_request(
            "GET", 
            f"{FORMLABS_BASE_URL}/developer/v1/printers/{printer_id}/"
        )
        response.raise_for_status()
        
        printer_data = response.json()
        
        # Extract status from printer_status if available
        status = "unknown"
        if printer_data.get("printer_status"):
            status = printer_data["printer_status"].get("status", "unknown")
        
        # Get last modified time
        updated_at = datetime.now()
        if printer_data.get("printer_status", {}).get("last_modified"):
            try:
                updated_at = datetime.fromisoformat(
                    printer_data["printer_status"]["last_modified"].replace("Z", "+00:00")
                )
            except:
                pass
        
        return PrinterResponse(
            id=printer_data["serial"],
            name=printer_data.get("alias", printer_data["serial"]),
            status=status,
            updated_at=updated_at,
            location=printer_data.get("location"),
            firmware_version=printer_data.get("firmware_version")
        )
        
    except Exception as e:
        # Return emulated data if real API fails
        return emulated_printer_status(printer_id)


@app.get("/mcp/prints/{print_id}", response_model=PrintResponse)
async def monitor_print(print_id: str):
    """Monitor a specific print job by its ID"""
    try:
        response = await get_token_manager().make_authenticated_request(
            "GET", 
            f"{FORMLABS_BASE_URL}/developer/v1/prints/{print_id}/"
        )
        response.raise_for_status()
        
        print_data = response.json()
        
        # Parse created_at timestamp
        updated_at = datetime.now()
        if print_data.get("created_at"):
            try:
                updated_at = datetime.fromisoformat(
                    print_data["created_at"].replace("Z", "+00:00")
                )
            except:
                pass
        
        # Determine status
        status = print_data.get("status", "unknown").lower()
        
        return PrintResponse(
            id=print_data["guid"],
            name=print_data.get("name", "Unnamed Print"),
            status=status,
            updated_at=updated_at,
            material=print_data.get("material"),
            volume_ml=print_data.get("volume_ml"),
            layer_count=print_data.get("layer_count"),
            printer=print_data.get("printer"),
            message=print_data.get("message")
        )
        
    except Exception as e:
        # Return emulated data if real API fails
        return emulated_print_status(print_id)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for graceful error responses"""
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(detail=str(exc)).model_dump()
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


def main():
    """Entry point for console script"""
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 