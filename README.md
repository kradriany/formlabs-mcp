# MCP Formlabs API Bridge

A **skinny Model-Context Protocol (MCP) micro-service** that bridges the Formlabs IoT REST API and the "ion-dashboard" React app.

## 🚀 Features

- **Authentication**: Automatic bearer token management with client-credentials flow
- **Proxy Endpoints**: Three normalized API routes for printers, events, and prints
- **Resilience**: Automatic token refresh, 429 retry-with-backoff, and graceful error handling
- **Flat JSON**: Normalized responses for easy dashboard consumption
- **Testing**: Comprehensive pytest unit tests
- **Containerization**: Docker and docker-compose support

## 📋 Prerequisites

- Python 3.11+
- Formlabs.com account with registered printers
- Formlabs API credentials (Client ID & Client Secret)

## 🛠️ Quick Start

### 1. Setup Environment

```bash
# Clone and setup
git clone <your-repo>
cd mcp-skinny

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Credentials

```bash
# Copy example environment file
cp env.example .env

# Edit .env with your Formlabs API credentials
# Get them from: https://dashboard.formlabs.com/#developer
```

### 3. Run the Service

```bash
# Development mode (with hot reload)
./scripts/dev.sh

# Or manually
uvicorn mcp.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Verify Installation

- Health check: http://localhost:8000/
- API docs: http://localhost:8000/docs
- OpenAPI schema: http://localhost:8000/openapi.json

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mcp

# Run specific test file
pytest tests/test_auth.py
```

## 🐳 Docker Deployment

```bash
# Build and run with docker-compose
docker-compose up --build

# Or build manually
docker build -t mcp-formlabs .
docker run -p 8000:8000 --env-file .env mcp-formlabs
```

## 📡 API Endpoints

### GET /mcp/printers
Returns a simplified list of all printers.

**Response:**
```json
[
  {
    "id": "PRINTER001",
    "name": "Lab Printer",
    "status": "idle",
    "updated_at": "2024-01-01T12:00:00Z",
    "location": "Lab A",
    "firmware_version": "2.1.0",
    "message": null
  }
]
```

### GET /mcp/events
Returns recent events with optional filtering.

**Query Parameters:**
- `since` (optional): ISO 8601 timestamp to filter events

**Response:**
```json
[
  {
    "id": 1,
    "name": "Print Completed - completed",
    "status": "active",
    "updated_at": "2024-01-01T12:00:00Z",
    "type": "print_completed",
    "action": "completed",
    "printer": "PRINTER001",
    "message": "Print job finished successfully"
  }
]
```

### GET /mcp/prints
Returns the latest print jobs.

**Response:**
```json
[
  {
    "id": "print-123",
    "name": "Test Print",
    "status": "finished",
    "updated_at": "2024-01-01T12:00:00Z",
    "material": "Resin A",
    "volume_ml": 25.5,
    "layer_count": 1000,
    "printer": "PRINTER001",
    "message": "Print completed successfully"
  }
]
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `CLIENT_ID` | Formlabs API Client ID | Yes |
| `CLIENT_SECRET` | Formlabs API Client Secret | Yes |
| `DASHBOARD_URL` | Dashboard URL for push updates | No |

### Getting Formlabs API Credentials

1. Visit [Formlabs Dashboard Developer Tools](https://dashboard.formlabs.com/#developer)
2. Create new Application credentials
3. Copy Client ID and Client Secret to your `.env` file

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   ion-dashboard │    │   MCP Bridge    │    │  Formlabs API   │
│   (React App)   │◄──►│   (FastAPI)     │◄──►│   (REST API)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Token Manager │
                       │   (Auth Cache)  │
                       └─────────────────┘
```

## 📁 Project Structure

```
mcp-skinny/
├── mcp/
│   ├── __init__.py
│   ├── main.py          # FastAPI app & routes
│   ├── auth.py          # Token manager
│   └── schemas.py       # Response models
├── tests/
│   ├── __init__.py
│   ├── test_auth.py     # Auth tests
│   └── test_main.py     # API tests
├── scripts/
│   └── dev.sh           # Development script
├── docker-compose.yml   # Container orchestration
├── Dockerfile          # Container definition
├── requirements.txt    # Python dependencies
├── openapi.json       # Formlabs API spec
└── README.md          # This file
```

## 🔄 Integration with ion-dashboard

1. **Configure Dashboard**: Add to dashboard's `.env`:
   ```
   REACT_APP_MCP_URL=http://localhost:8000/mcp
   ```

2. **Update Dashboard Code**: Modify dashboard to fetch from MCP endpoints instead of direct Formlabs API

3. **Test Integration**: Verify dashboard widgets display printer status & events

## 🚨 Error Handling

The service provides graceful error handling:

- **401 Unauthorized**: Automatic token refresh
- **429 Rate Limited**: Exponential backoff retry
- **API Errors**: Normalized error responses
- **Network Issues**: Retry with backoff

All errors return consistent JSON format:
```json
{
  "status": "error",
  "detail": "Error description"
}
```

## 📊 Monitoring

- **Health Check**: `GET /` returns service status
- **Logs**: Structured logging for debugging
- **Metrics**: Request/response timing available

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Check the [Formlabs API Documentation](https://formlabs.com/support/privacy-policy/)
- Review the [ion-dashboard repository](https://github.com/iottechorg/iot-middleware-dashboard)
- Open an issue in this repository 