"""
Demo application that batches all STL files in a folder into .form files.

Usage: python3 batching-minimal.py ~/Documents/folder-of-stl-files

Optional flags:
--auto-orient: Auto orient models
--dental-mode: Use dental mode when auto orienting
--auto-support: Auto support models
--username: Username for login if uploading to a remote printer or Fleet Control queue
--password: Password for login if uploading to a remote printer or Fleet Control queue
--upload-to: Upload to a specific printer, IP Address, or Fleet Control Printer Group ID
"""

import argparse
import os
import pathlib
import csv
import sys
import requests
import formlabs_local_api_minimal as formlabs


def list_files_in_directory(directory_path):
    return [
        f
        for f in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, f)) and f.endswith(".stl")
    ]


def create_scene():
    response = requests.request(
        "POST",
        "http://localhost:44388/scene/",
        json={
            "machine_type": "FORM-4-0",
            "material_code": "FLGPGR05",
            "layer_thickness_mm": 0.1,
            "print_setting": "DEFAULT",
        },
    )
    response.raise_for_status()
    return response.json()["id"]


parser = argparse.ArgumentParser(description="Process a folder path.")
parser.add_argument("folder", type=str, help="Path to the folder")
parser.add_argument("--auto-orient", action="store_true", help="Auto orient models")
parser.add_argument("--dental-mode", action="store_true", help="Use dental mode when auto orienting")
parser.add_argument("--auto-support", action="store_true", help="Auto support models")
parser.add_argument("--username", type=str, help="Username for login")
parser.add_argument("--password", type=str, help="Password for login")
parser.add_argument("--upload-to", type=str, help="Upload to a specific printer, IP Address, or Fleet Control Printer Group ID")
args = parser.parse_args()

directory_path = os.path.abspath(args.folder)
files_to_batch = list_files_in_directory(directory_path)
print("Files to batch:")
print(files_to_batch)
current_batch = 1
models_in_current_batch = []
scene_id = None
CSV_RESULT_FILENAME = os.path.join(directory_path, "summary.csv")

pathToPreformServer = None
if sys.platform == 'win32':
    pathToPreformServer = pathlib.Path().resolve() / "PreFormServer/PreFormServer.exe"
elif sys.platform == 'darwin':
    pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
else:
    print("Unsupported platform")
    sys.exit(1)

with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer):
    if args.username and args.password:
        login_response = requests.request(
            "POST",
            "http://localhost:44388/login/",
            json={
                "username": args.username,
                "password": args.password,
            },
        )
        login_response.raise_for_status()

    with open(CSV_RESULT_FILENAME, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Batch Number", "Batch Print Filename", "Model Source Filename"])

        def save_batch_form():
            global current_batch, models_in_current_batch, scene_id
            form_file_name = f"batch_{current_batch}.form"
            save_path = os.path.join(directory_path, form_file_name)
            save_form_response = requests.request(
                "POST",
                f"http://localhost:44388/scene/{scene_id}/save-form/",
                json={
                    "file": save_path,
                },
            )
            save_form_response.raise_for_status()
            print(f"Saving batch {current_batch} to {save_path}")
            for i, model in enumerate(models_in_current_batch):
                print(f"{i+1}. {model['file_name']}")
                csvwriter.writerow([current_batch, form_file_name, model['file_name']])
            current_batch += 1
            models_in_current_batch = []
            if args.upload_to:
                print(f"Uploading batch to {args.upload_to}")
                print_response = requests.request(
                    "POST",
                    f"http://localhost:44388/scene/{scene_id}/print/",
                    json={
                        "printer": args.upload_to,
                        "job_name": form_file_name,
                    },
                )
                print_response.raise_for_status()

        scene_id = create_scene()
        while len(files_to_batch) > 0:
            next_file = files_to_batch.pop()
            print(f"Importing {next_file}")
            import_model_response = requests.request(
                "POST",
                f"http://localhost:44388/scene/{scene_id}/import-model/",
                json={
                    "file": os.path.join(directory_path, next_file),
                },
            )
            import_model_response.raise_for_status()
            new_model_id = import_model_response.json()["id"]
            models_in_current_batch.append({"model_id": new_model_id, "file_name": next_file})
            if args.auto_orient:
                print(f"Auto orienting {new_model_id}")
                auto_orient_params = {"models": [new_model_id]}
                if args.dental_mode:
                    auto_orient_params["mode"] = "DENTAL"
                    auto_orient_params["tilt"] = 0
                auto_orient_response = requests.request(
                    "POST",
                    f"http://localhost:44388/scene/{scene_id}/auto-orient/",
                    json=auto_orient_params,
                )
                auto_orient_response.raise_for_status()
            if args.auto_support:
                print(f"Auto supporting {new_model_id}")
                auto_support_response = requests.request(
                    "POST",
                    f"http://localhost:44388/scene/{scene_id}/auto-support/",
                    json={
                        "models": [new_model_id],
                    },
                )
                auto_support_response.raise_for_status()
            print(f"Auto layouting all")
            layout_response = requests.request(
                "POST",
                f"http://localhost:44388/scene/{scene_id}/auto-layout/",
                json={
                    "models": "ALL",
                },
            )
            if layout_response.status_code != 200:
                print("Not all models can fit, removing model")
                model_data = models_in_current_batch.pop()
                delete_response = requests.request(
                    "DELETE",
                    f"http://localhost:44388/scene/{scene_id}/models/{str(model_data['model_id'])}/",
                )
                delete_response.raise_for_status()
                files_to_batch.append(model_data["file_name"])
                save_batch_form()
                print("Clearing scene")
                scene_id = create_scene()

        if len(models_in_current_batch) > 0:
            save_batch_form()
