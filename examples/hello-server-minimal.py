import formlabs_local_api_minimal as formlabs
import requests
import pathlib
import sys

def hello_server():
    pathToPreformServer = None
    if sys.platform == 'win32':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.exe"
    elif sys.platform == 'darwin':
        pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
    else:
        print("Unsupported platform")
        sys.exit(1)
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer):
        payload = {
            "machine_type": "FORM-4-0",
            "material_code": "FLRG1011",
            "layer_thickness_mm": 0.1,
            "print_setting": "DEFAULT"
        }
        response = requests.request("POST", "http://localhost:44388/scene/", json=payload)
        response.raise_for_status()
        print(response.json())
        print("Scene created, exiting")

if __name__ == "__main__":
    hello_server()
