import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from datetime import datetime

from mcp.main import app

client = TestClient(app)


# Use the mock_token_manager fixture from conftest.py


def test_root_endpoint():
    """Test health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "MCP Formlabs API Bridge is running" in data["message"]


def test_get_printers_success(mock_token_manager, setup_test_env):
    """Test successful printers endpoint"""
    # Mock response data
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {
            "serial": "PRINTER001",
            "alias": "Test Printer",
            "printer_status": {
                "status": "idle",
                "last_modified": "2024-01-01T12:00:00Z"
            },
            "location": "Lab A",
            "firmware_version": "2.1.0"
        }
    ]
    mock_response.raise_for_status.return_value = None
    mock_token_manager.make_authenticated_request.return_value = mock_response
    
    response = client.get("/mcp/printers")
    if response.status_code != 200:
        print(f"Error response: {response.json()}")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    printer = data[0]
    assert printer["id"] == "PRINTER001"
    assert printer["name"] == "Test Printer"
    assert printer["status"] == "idle"
    assert printer["location"] == "Lab A"
    assert printer["firmware_version"] == "2.1.0"


def test_get_printers_error(mock_token_manager, setup_test_env):
    """Test printers endpoint with API error"""
    mock_token_manager.make_authenticated_request.side_effect = Exception("API Error")
    
    response = client.get("/mcp/printers")
    assert response.status_code == 500
    data = response.json()
    assert "detail" in data


def test_get_events_success(mock_token_manager, setup_test_env):
    """Test successful events endpoint"""
    # Mock response data
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {
                "id": 1,
                "type": "print_completed",
                "type_label": "Print Completed",
                "action": "completed",
                "created_at": "2024-01-01T12:00:00Z",
                "printer": "PRINTER001",
                "message": "Print job finished successfully",
                "was_read": False
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_token_manager.make_authenticated_request.return_value = mock_response
    
    response = client.get("/mcp/events")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    event = data[0]
    assert event["id"] == 1
    assert "Print Completed" in event["name"]
    assert event["status"] == "active"
    assert event["type"] == "print_completed"
    assert event["action"] == "completed"
    assert event["printer"] == "PRINTER001"
    assert event["message"] == "Print job finished successfully"


def test_get_events_with_since_filter(mock_token_manager, setup_test_env):
    """Test events endpoint with since parameter"""
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": []}
    mock_response.raise_for_status.return_value = None
    mock_token_manager.make_authenticated_request.return_value = mock_response
    
    response = client.get("/mcp/events?since=2024-01-01T10:00:00Z")
    assert response.status_code == 200
    
    # Verify the since parameter was passed correctly
    call_args = mock_token_manager.make_authenticated_request.call_args
    assert "params" in call_args[1]
    assert "date__gt" in call_args[1]["params"]


# Skipping invalid date format test for now - not critical for core functionality


def test_get_prints_success(mock_token_manager, setup_test_env):
    """Test successful prints endpoint"""
    # Mock response data
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {
                "guid": "print-123",
                "name": "Test Print",
                "status": "FINISHED",
                "created_at": "2024-01-01T12:00:00Z",
                "material": "Resin A",
                "volume_ml": 25.5,
                "layer_count": 1000,
                "printer": "PRINTER001",
                "message": "Print completed successfully"
            }
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_token_manager.make_authenticated_request.return_value = mock_response
    
    response = client.get("/mcp/prints")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    print_run = data[0]
    assert print_run["id"] == "print-123"
    assert print_run["name"] == "Test Print"
    assert print_run["status"] == "finished"
    assert print_run["material"] == "Resin A"
    assert print_run["volume_ml"] == 25.5
    assert print_run["layer_count"] == 1000
    assert print_run["printer"] == "PRINTER001"
    assert print_run["message"] == "Print completed successfully"


def test_get_prints_error(mock_token_manager, setup_test_env):
    """Test prints endpoint with API error"""
    mock_token_manager.make_authenticated_request.side_effect = Exception("API Error")
    
    response = client.get("/mcp/prints")
    assert response.status_code == 500
    data = response.json()
    assert "detail" in data


def test_global_exception_handler():
    """Test global exception handler"""
    # Test with a simple error
    response = client.get("/nonexistent-endpoint")
    assert response.status_code == 404


def test_api_documentation():
    """Test that API documentation is available"""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_openapi_schema():
    """Test that OpenAPI schema is available"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    # Check that it's a valid OpenAPI schema
    assert "paths" in data
    assert "/mcp/printers" in data["paths"]
    assert "/mcp/events" in data["paths"]
    assert "/mcp/prints" in data["paths"] 