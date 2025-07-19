#!/bin/bash

# MCP Formlabs API Bridge - Development Script

echo "🚀 Starting MCP Formlabs API Bridge in development mode..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run:"
    echo "   python3 -m venv .venv"
    echo "   source .venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating template..."
    cat > .env << EOF
# Formlabs API Credentials
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here

# Optional: Dashboard URL for push updates
DASHBOARD_URL=http://localhost:3000
EOF
    echo "📝 Please edit .env file with your Formlabs API credentials"
    echo "   Get them from: https://dashboard.formlabs.com/#developer"
    exit 1
fi

# Check if credentials are set
if grep -q "your_client_id_here" .env; then
    echo "❌ Please update .env file with your actual Formlabs API credentials"
    exit 1
fi

# Run tests first
echo "🧪 Running tests..."
pytest -q
if [ $? -ne 0 ]; then
    echo "❌ Tests failed. Please fix issues before starting server."
    exit 1
fi

echo "✅ Tests passed!"

# Start the server
echo "🌐 Starting server on http://localhost:8000"
echo "📚 API docs available at http://localhost:8000/docs"
echo "🛑 Press Ctrl+C to stop"
echo ""

uvicorn mcp.main:app --reload --host 0.0.0.0 --port 8000 