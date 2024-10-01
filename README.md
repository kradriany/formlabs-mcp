# Formlabs API Python Library & Examples

Python code related to using Formlabs' local and web APIs.

## Available Libraries

1. Formlabs Local Python Library (Minimal)
    - A small library that depends on the Python HTTP client library [`requests`](https://pypi.org/project/requests/) with a helper class for starting the PreFormServer executable.
    - The [`requests`](https://pypi.org/project/requests/) library should be used to make API requests.
    - Request formatting and parsing is not included in the library and should be done in client code.
2. Formlabs Local Python Library
    - A library automatically generated from the OpenAPI YAML specification of the Formlabs Local API.
    - Library provides types and handles request formatting.
    - **Warning**: API version updates may change the libraries types and require changes to your code. For this reason, we don't recommend this library for long term integrations that want minimal to no code changes between PreFormServer versions.
3. Formlabs Web Python Library
    - A library automatically generated from the OpenAPI YAML specification of the Formlabs Web API.
    - Library provides types and handles request formatting.

## Python library installation:

First, have at least Python 3.7 installed and available on your path.
We recommend installing the Python package in a [Python virtual environment](https://docs.python.org/3/library/venv.html) during testing.

```
# Create a virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Ensure you have pip installed
python3 -m ensurepip --default-pip

# Install Formlabs Local Python library (Minimal)
python3 -m pip install -e local-api/minimal-lib

# Install Formlabs Local Python library
python3 -m pip install -e local-api/lib

# Install Formlabs Web Python library
python3 -m pip install -e web-api/lib
```

Now test the installation by running an example. The example expects that a PreFormServer executable has been downloaded, extracted, and placed in the folder where you are going to run the demo.

```
# Activate virtual environment, if you haven't already
source myenv/bin/activate

# Test installation by running a demo:
python3 examples/hello-server.py

# When you are done, deactivate the virtual environment
deactivate
```

## Generating the Python Libraries

All these examples work on the OpenAPI 3.0 descriptions of the Formlabs Local and Web HTTP REST APIs

```bash
brew install openapi-generator

rm -rf local-api/lib
rm -rf web-api/lib
openapi-generator generate -i local-api/formlabs-api-local-openapi.yaml -g python -o ./local-api/lib -c ./local-api/gen-config.yaml
openapi-generator generate -i web-api/formlabs-api-web-openapi.yaml -g python -o ./web-api/lib -c ./web-api/gen-config.yaml
```
