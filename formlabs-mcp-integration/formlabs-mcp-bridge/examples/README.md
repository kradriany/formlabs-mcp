# Formlabs MCP Bridge Examples

This directory contains comprehensive examples demonstrating how to use the Formlabs MCP Bridge for printer monitoring and fleet management.

## 📋 Available Examples

### 1. `test_mcp_connection.py`
**Basic MCP Connection Test**
- Tests basic connectivity to the MCP bridge
- Analyzes device uptime and printing time from events
- Demonstrates event-based monitoring approach
- Shows how to calculate utilization percentages

**Usage:**
```bash
python test_mcp_connection.py
```

**Output:**
- List of all devices
- Target device verification
- 24-hour event analysis
- Uptime and printing time calculations
- Utilization metrics

### 2. `advanced_mcp_analysis.py`
**Advanced Fleet Analysis**
- Comprehensive analysis across multiple printers
- Fleet-wide utilization metrics
- Success rate analysis
- Performance ranking and insights
- Automated recommendations

**Usage:**
```bash
python advanced_mcp_analysis.py
```

**Output:**
- Fleet summary statistics
- Individual printer analysis
- Performance comparisons
- Health insights and recommendations
- Utilization rankings

### 3. `mcp_usage_example.py`
**Comprehensive Usage Demonstration**
- Demonstrates all 5 MCP tools
- Real-world fleet management scenarios
- Health monitoring and reporting
- Print job history tracking
- Real-time monitoring simulation

**Usage:**
```bash
python mcp_usage_example.py
```

**Output:**
- Daily fleet reports
- Active print monitoring
- Printer health checks
- Print job history
- Real-time status updates

### 4. `mcp_client_example.py`
**Simple Client Example**
- Basic HTTP client implementation
- Direct API endpoint testing
- Simple data retrieval examples
- Error handling demonstration

**Usage:**
```bash
python mcp_client_example.py
```

**Output:**
- Printer status information
- Event data retrieval
- Print job details
- Basic error handling

## 🎮 Emulation Mode Testing

All examples work with the built-in emulation mode, providing realistic data for testing:

### Emulated Data Features
- **2 Virtual Printers**: PRINTER001 (Lab) and PRINTER002 (Production)
- **24 Hours of Events**: Realistic timeline with print starts, completions, failures
- **Maintenance Cycles**: Tank cleaning and maintenance events
- **Status Variations**: Idle, printing, error states
- **Material Information**: Different resins and volumes

### Starting Emulation
```bash
# From the formlabs-mcp-bridge directory
uvicorn formlabs_mcp_bridge.main:app --reload --host 0.0.0.0 --port 8000
```

### Testing Examples
```bash
# Test basic connectivity
python examples/test_mcp_connection.py

# Test advanced analysis
python examples/advanced_mcp_analysis.py

# Test comprehensive usage
python examples/mcp_usage_example.py

# Test simple client
python examples/mcp_client_example.py
```

## 🔌 Real Machine Testing

For testing with actual Formlabs printers:

### Prerequisites
1. **Formlabs Developer Account**
2. **CLIENT_ID and CLIENT_SECRET**
3. **Network access to api.formlabs.com**

### Configuration
```bash
# Set environment variables
export FORMLABS_CLIENT_ID="your_client_id"
export FORMLABS_CLIENT_SECRET="your_client_secret"

# Or create .env file
cp env.example .env
# Edit .env with your credentials
```

### Running Examples
```bash
# Start the MCP bridge
uvicorn formlabs_mcp_bridge.main:app --reload --host 0.0.0.0 --port 8000

# In another terminal, run examples
python examples/test_mcp_connection.py
```

## 📊 Example Outputs

### Basic Connection Test Output
```
🔌 Testing MCP Connection to Formlabs Emulator
============================================================

📋 Step 1: Getting list of all devices...
✅ Found 2 printer(s):
   • Lab Printer (PRINTER001) - idle
   • Production Printer (PRINTER002) - printing

🎯 Step 2: Checking for target device 'PRINTER001'...
✅ Target device 'PRINTER001' found!

📊 Step 3: Getting events from last 24 hours...
✅ Found 15 events in the last 24 hours

📈 Step 4: Analyzing uptime and printing time for 'PRINTER001'...

📊 Analysis Results:
----------------------------------------
Target Device: PRINTER001
Total Events: 14
Printing Sessions: 5
Total Uptime: 1380.00 minutes
Total Printing Time: 600.00 minutes
Uptime Percentage: 43.48%
```

### Advanced Analysis Output
```
🚀 Advanced Formlabs Fleet Analysis
============================================================

📋 Gathering fleet data...
✅ Found 2 printers, 15 events, 2 prints

📊 Analyzing fleet performance...

📈 Fleet Summary:
----------------------------------------
Total Printers: 2
Active Printers: 2
Fleet Utilization: 43.48%
Success Rate: 80.00%
Total Printing Time: 600.00 minutes
Average Print Duration: 120.00 minutes

🖨️ Individual Printer Analysis:
----------------------------------------

Lab Printer (PRINTER001):
  Status: idle
  Utilization: 43.48%
  Success Rate: 80.00%
  Prints: 4 successful, 1 failed
  Total Time: 600.00 minutes printing
```

## 🛠️ Customizing Examples

### Modifying Target Devices
Edit the examples to target specific printers:

```python
# In test_mcp_connection.py
target_device = "YOUR_PRINTER_ID"  # Change this to your printer ID
```

### Adjusting Time Windows
Modify the time period for analysis:

```python
# For 7 days instead of 24 hours
yesterday = (datetime.now() - timedelta(days=7)).isoformat()
```

### Adding Custom Analysis
Extend the examples with your own analysis logic:

```python
# Add custom metrics
def custom_analysis(events, printers):
    # Your custom analysis here
    pass
```

## 🧪 Testing with Swagger UI

1. **Start the MCP Bridge:**
   ```bash
   uvicorn formlabs_mcp_bridge.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Open Swagger UI:**
   - Navigate to `http://localhost:8000/docs`
   - Test all endpoints interactively
   - View request/response schemas
   - Try different parameters

3. **Test Endpoints:**
   - `GET /mcp/printers` - List all printers
   - `GET /mcp/events` - Get recent events
   - `GET /mcp/prints` - Get print jobs
   - `GET /mcp/printers/{printer_id}` - Get specific printer
   - `GET /mcp/prints/{print_id}` - Monitor specific print

## 🔧 Troubleshooting

### Common Issues

1. **Connection Errors:**
   ```bash
   # Check if server is running
   curl http://localhost:8000/
   
   # Check server logs
   uvicorn formlabs_mcp_bridge.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Import Errors:**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Install in development mode
   pip install -e .
   ```

3. **Authentication Errors:**
   ```bash
   # Check environment variables
   echo $FORMLABS_CLIENT_ID
   echo $FORMLABS_CLIENT_SECRET
   
   # Or check .env file
   cat .env
   ```

### Debug Mode
Run examples with debug output:

```python
# Add to examples
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Next Steps

1. **Start with emulation**: Use the examples with emulated data
2. **Test with real machines**: Configure authentication and test with real printers
3. **Customize for your needs**: Modify examples for your specific use cases
4. **Integrate with your systems**: Use the MCP tools in your applications
5. **Contribute**: Add new examples or improve existing ones

---

**Ready to get started? Run `python examples/test_mcp_connection.py` to begin!** 🚀 