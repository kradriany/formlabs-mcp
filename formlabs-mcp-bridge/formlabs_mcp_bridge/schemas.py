from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class PrinterResponse(BaseModel):
    """Flat printer response for dashboard consumption"""
    id: str
    name: str
    status: str
    updated_at: datetime
    message: Optional[str] = None
    location: Optional[str] = None
    firmware_version: Optional[str] = None


class EventResponse(BaseModel):
    """Flat event response for dashboard consumption"""
    id: int
    name: str
    status: str
    updated_at: datetime
    message: Optional[str] = None
    type: str
    action: str
    printer: Optional[str] = None


class PrintResponse(BaseModel):
    """Flat print response for dashboard consumption"""
    id: str
    name: str
    status: str
    updated_at: datetime
    message: Optional[str] = None
    material: Optional[str] = None
    volume_ml: Optional[float] = None
    layer_count: Optional[int] = None
    printer: Optional[str] = None


class ErrorResponse(BaseModel):
    """Standard error response"""
    status: str = "error"
    detail: str 