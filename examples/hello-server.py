import formlabs_local_api as formlabs
from formlabs_local_api import SceneTypeModel, Manual, ManualLayerThicknessMm
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
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        preform.api.scene_post(SceneTypeModel(Manual(
            machine_type="FORM-4-0",
            material_code="FLRG1011",
            layer_thickness_mm=ManualLayerThicknessMm("0.1"),
            print_setting="DEFAULT",
        )))
        print("Scene created, exiting")

if __name__ == "__main__":
    hello_server()
