# Formlabs MCP (Model-Context Protocol) Integration

This project provides a complete MCP (Model-Context Protocol) integration for Formlabs 3D printers, allowing AI models to interact with Formlabs printers through a standardized interface.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AI Model      │    │   MCP Bridge    │    │  Formlabs API   │
│   (Cursor/LLM)  │◄──►│   (FastAPI)     │◄──►│   (REST API)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Token Manager │
                       │   (Auth Cache)  │
                       └─────────────────┘
```

## 📋 MCP Configuration

The `.cursor/mcp.json` file defines the MCP server and tools:

### 🛠️ Available Tools

1. **`get_formlabs_printers`**
   - **Description**: Get a list of all Formlabs printers with their status and details
   - **Input**: None
   - **Output**: List of printer objects with status, location, firmware version

2. **`get_formlabs_events`**
   - **Description**: Get recent events from Formlabs printers with optional filtering
   - **Input**: Optional `since` parameter (ISO 8601 timestamp)
   - **Output**: List of event objects with type, action, printer, and message

3. **`get_formlabs_prints`**
   - **Description**: Get the latest print jobs from Formlabs printers
   - **Input**: None
   - **Output**: List of print job objects with status, material, volume, progress

4. **`get_formlabs_printer_status`**
   - **Description**: Get detailed status of a specific Formlabs printer
   - **Input**: `printer_id` (string)
   - **Output**: Detailed printer status object

5. **`monitor_formlabs_print`**
   - **Description**: Monitor a specific print job by its ID
   - **Input**: `print_id` (string)
   - **Output**: Detailed print job status with progress information

### 📚 Available Resources

- **`formlabs-printers`**: Real-time list of Formlabs printers and their status
- **`formlabs-events`**: Recent events from Formlabs printers
- **`formlabs-prints`**: Latest print jobs from Formlabs printers
- **`formlabs-api-docs`**: Interactive API documentation

## 🚀 Quick Start

### 1. Start the MCP Server

```bash
# From the project directory
uvicorn mcp.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Configure Environment Variables

Create a `.env` file with your Formlabs API credentials:

```bash
CLIENT_ID=your_formlabs_client_id
CLIENT_SECRET=your_formlabs_client_secret
DASHBOARD_URL=http://localhost:3000
```

### 3. Test the MCP Tools

```bash
# Run the example client
python mcp_client_example.py
```

## 📡 API Endpoints

### Core MCP Endpoints

- `GET /mcp/printers` - List all printers
- `GET /mcp/events` - Get recent events (with optional `since` filter)
- `GET /mcp/prints` - Get latest print jobs
- `GET /mcp/printers/{printer_id}` - Get specific printer status
- `GET /mcp/prints/{print_id}` - Monitor specific print job

### Documentation

- `GET /` - Health check
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /openapi.json` - OpenAPI schema

## 🔧 Usage Examples

### Using the MCP Tools in Cursor

Once the MCP server is running, you can use the tools directly in Cursor:

```python
# Example: Get all printers
printers = await get_formlabs_printers()
for printer in printers:
    print(f"{printer['name']} - {printer['status']}")

# Example: Monitor a specific print
print_status = await monitor_formlabs_print("print-123")
print(f"Print {print_status['name']} is {print_status['status']}")

# Example: Get events since yesterday
from datetime import datetime, timedelta
yesterday = (datetime.now() - timedelta(days=1)).isoformat()
events = await get_formlabs_events(since=yesterday)
```

### Using the Python Client

```python
from mcp_client_example import FormlabsMCPClient
import asyncio

async def main():
    client = FormlabsMCPClient()
    
    # Get all printers
    printers = await client.get_formlabs_printers()
    print(f"Found {len(printers)} printers")
    
    # Monitor a specific print
    print_status = await client.monitor_formlabs_print("print-123")
    print(f"Print progress: {print_status['message']}")
    
    await client.close()

asyncio.run(main())
```

## 🎯 Use Cases

### 1. **Print Farm Monitoring**
- Monitor multiple printers simultaneously
- Track print job progress across all machines
- Get alerts for completed or failed prints

### 2. **Production Planning**
- Check printer availability and status
- Monitor material usage and remaining capacity
- Track print queue and estimated completion times

### 3. **Quality Control**
- Monitor print parameters and settings
- Track print success rates
- Get detailed event logs for troubleshooting

### 4. **Integration with AI Workflows**
- Automate print job scheduling based on AI analysis
- Generate reports on printer utilization
- Create predictive maintenance alerts

## 🔄 Emulated Data

When real Formlabs API credentials are not available, the MCP server returns realistic emulated data:

### Sample Printer Data
```json
{
  "id": "PRINTER001",
  "name": "Lab Printer",
  "status": "idle",
  "location": "Lab A",
  "firmware_version": "2.1.0",
  "message": "Ready for next print job"
}
```

### Sample Print Data
```json
{
  "id": "print-123",
  "name": "Test Print",
  "status": "finished",
  "material": "Resin A",
  "volume_ml": 25.5,
  "layer_count": 1000,
  "printer": "PRINTER001",
  "message": "Print completed successfully"
}
```

## 🛡️ Error Handling

The MCP server includes comprehensive error handling:

- **Authentication Errors**: Automatic token refresh and retry
- **Rate Limiting**: Exponential backoff for 429 responses
- **Network Issues**: Graceful fallback to emulated data
- **Invalid Requests**: Clear error messages with suggestions

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `CLIENT_ID` | Formlabs API Client ID | Yes | - |
| `CLIENT_SECRET` | Formlabs API Client Secret | Yes | - |
| `DASHBOARD_URL` | Dashboard URL for push updates | No | `http://localhost:3000` |

### Server Configuration

- **Host**: `0.0.0.0` (accessible from any IP)
- **Port**: `8000`
- **Reload**: Enabled for development
- **Logging**: Structured logging for debugging

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run specific test categories
pytest tests/test_auth.py
pytest tests/test_main.py

# Run with coverage
pytest --cov=mcp
```

## 🐳 Docker Deployment

```bash
# Build and run with docker-compose
docker-compose up --build

# Or build manually
docker build -t mcp-formlabs .
docker run -p 8000:8000 --env-file .env mcp-formlabs
```

## 📊 Monitoring

- **Health Check**: `GET /` returns service status
- **Metrics**: Request/response timing available
- **Logs**: Structured logging for debugging
- **Documentation**: Auto-generated OpenAPI docs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
- Check the [Formlabs API Documentation](https://formlabs.com/support/privacy-policy/)
- Review the [ion-dashboard repository](https://github.com/iottechorg/iot-middleware-dashboard)
- Open an issue in this repository

---

**The Formlabs MCP integration is now ready for production use!** 🚀 