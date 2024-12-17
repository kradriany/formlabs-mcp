"""
Demo application of a Print Upload Dialog using the Formlabs Local API.

The application is meant to be demo of the API calls and logic involved in building a print upload dialog.
The model to be sliced and uploaded is a simple cube.stl file included in the same directory as this script.

The following are all left intentionally unfinished to keep the demo code concise:
- Loading user models
- Print preparation
- Application styling
- Deployment

Installation:
- On MacOS if using Python 3.12: brew install python-tk@3.12
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk  # themed tk
from typing import TypedDict, NotRequired
import atexit
import pathlib
from requests import request
from requests.exceptions import HTTPError
import formlabs_local_api_minimal as formlabs
import sys
import time

server_path: str = ""
if sys.platform == "win32":
    server_path = str(pathlib.Path().resolve().parents[1] / "PreFormServer/PreFormServer.exe")
elif sys.platform == "darwin":
    server_path = str(pathlib.Path().resolve().parents[1] / "PreFormServer.app/Contents/MacOS/PreFormServer")
else:
    print("Unsupported platform")
    sys.exit(1)

# Type Definitions
PrinterTypeDropdownLabel = str  # Example "Form 3/3+"
PrinterDropdownLabel = str  # Example [Form 3] TestyTest - Idle
PrintSettingDropdownLabel = str  # Example "Alumina 4N V1 0.050 mm (Default Settings)"
ProductName = str  # Example: "Form 3"
MachineTypeId = str  # Example: "FORM-3-0"
PrintOperationId = str  # uuid string
DeviceData = TypedDict(
    "DeviceData",
    {
        "product_name": ProductName,
        "id": str,
        "status": str,
        "dashboard_queue_id": NotRequired[str],
        "supported_machine_type_ids": NotRequired[list[MachineTypeId]],
        "ready_to_print_now": NotRequired[bool],
    },
)
SceneSettings = TypedDict(
    "SceneSettings",
    {
        "layer_thickness_mm": float,
        "machine_type": MachineTypeId,
        "material_code": str,
        "print_setting": str,
    },
)

TEST_FILE_PATH = pathlib.Path().resolve() / "cube.stl"
SLICING_PROGRESS_POLL_INTERVAL_S = 0.5
PRINTER_GROUP_PRODUCT_NAME: ProductName = "Printer Group"
BASE_API_URL = "http://localhost:44388"


class AppState:
    def __init__(self):
        self.logged_in_access_token: str = ""
        self.logged_in_username: str = ""
        self.available_printers: dict[PrinterDropdownLabel, DeviceData] = self.get_printers()
        self.selected_printer: PrinterDropdownLabel = ""
        self.api_materials_and_printer_data = api_request("GET", "/list-materials/")
        self.product_names_within_material_group: dict[PrinterTypeDropdownLabel, list[ProductName]] = {}
        self.supported_machine_type_ids_by_material_group: dict[PrinterTypeDropdownLabel, list[MachineTypeId]] = {}
        self.available_print_settings: dict[
            PrinterTypeDropdownLabel, dict[PrintSettingDropdownLabel, SceneSettings]
        ] = {}
        self.set_list_materials_derived_data()
        self.printer_selection_menu_options: list[PrinterDropdownLabel] = []
        self.selected_printer_type: PrinterTypeDropdownLabel = ""
        self.print_setting_selection_menu_options: list[PrintSettingDropdownLabel] = []
        self.selected_print_setting: PrintSettingDropdownLabel = ""
        self.set_selected_printer_type(self.available_printer_types[0])
        self.job_name: str = "Test Job"

    def get_printers(self) -> dict[PrinterDropdownLabel, DeviceData]:
        """Use the Formlabs Local API to get a list of available printers
        and format the results for use in the dropdown menu
        """
        data = api_request("GET", "/devices/?can_print=true")
        available_printers = {}
        for device in data["devices"]:
            available_printers[self.get_printer_dropdown_label(device)] = device
        return available_printers

    def get_printer_dropdown_label(self, device) -> PrinterDropdownLabel:
        # Example: "[Form 3] FoamyPorcupine - Idle"
        return f"[{device['product_name']}] {device['id']} - {device['status']}"

    def get_print_setting_dropdown_label(self, material_label, setting_label) -> PrintSettingDropdownLabel:
        # Example: "Alumina 4N V1 0.050 mm (Default Settings)"
        return f"{material_label} {setting_label}"

    def set_list_materials_derived_data(self) -> None:
        """Extract and store derived data from the list-materials API response"""
        for v in self.api_materials_and_printer_data["printer_types"]:
            self.product_names_within_material_group[v["label"]] = v["supported_product_names"]
            self.supported_machine_type_ids_by_material_group[v["label"]] = v["supported_machine_type_ids"]
            # Flatten the nested materials list into a single list of print settings per printer type
            flattened_materials: dict[PrintSettingDropdownLabel, SceneSettings] = {}
            for m in v["materials"]:
                for s in m["material_settings"]:
                    label = self.get_print_setting_dropdown_label(m["label"], s["label"])
                    flattened_materials[label] = s["scene_settings"]
            self.available_print_settings[v["label"]] = flattened_materials
        # List of printer type dropdown labels for use in the UI
        self.available_printer_types: list[PrinterTypeDropdownLabel] = list(self.available_print_settings.keys())

    def get_selected_print_setting_json(self) -> SceneSettings:
        """Get the JSON data for the selected print setting based on the selected printer type dropdown value"""
        return self.available_print_settings[self.selected_printer_type][self.selected_print_setting]

    def get_selected_printer_id(self) -> str:
        selected_printer_data: DeviceData = self.available_printers[self.selected_printer]
        if selected_printer_data["product_name"] == PRINTER_GROUP_PRODUCT_NAME:
            return selected_printer_data["dashboard_queue_id"]
        else:
            return selected_printer_data["id"]

    def update_printer_selection_menu_options(self) -> None:
        self.printer_selection_menu_options = self.get_filtered_printers_based_on_selected_printer_type(
            self.selected_printer_type
        )
        if len(self.printer_selection_menu_options) == 0:
            self.selected_printer = ""
        else:
            if not self.selected_printer or self.selected_printer not in self.printer_selection_menu_options:
                self.selected_printer = self.printer_selection_menu_options[0]

    def set_selected_printer_type(self, new_value) -> None:
        self.selected_printer_type = new_value
        self.print_setting_selection_menu_options = list(
            self.available_print_settings[self.selected_printer_type].keys()
        )
        self.selected_print_setting = self.print_setting_selection_menu_options[0]
        self.update_printer_selection_menu_options()

    def should_show_printer_group(self, selected_printer_type, device_data: DeviceData) -> bool:
        """Check if there is an overlap between the supported machine types of the
        selected printer type and the printer group's supported machine types
        """
        a: list[MachineTypeId] = self.supported_machine_type_ids_by_material_group[selected_printer_type]
        b: list[MachineTypeId] = device_data["supported_machine_type_ids"]
        return len(list(set(a) & set(b))) > 0

    def get_filtered_printers_based_on_selected_printer_type(self, selected_printer_type) -> list[PrinterDropdownLabel]:
        new_choices: list[PrinterDropdownLabel] = []
        for dropdown_label, device_data in self.available_printers.items():
            # Filter printers to these two cases:
            # 1. Printers that match the selected printer type.
            #    Example device has type "Form 3" when the user has selected the "Form 3/3+" printer type.
            # 2. Device is a Fleet Control Printer Group that supports at least one of the
            #    selected printer type's supported machine types.
            if device_data["product_name"] in self.product_names_within_material_group[selected_printer_type] or (
                device_data["product_name"] == PRINTER_GROUP_PRODUCT_NAME
                and self.should_show_printer_group(selected_printer_type, device_data)
            ):
                new_choices.append(dropdown_label)
        return new_choices

    def update_printers(self) -> None:
        self.available_printers = self.get_printers()
        self.update_printer_selection_menu_options()


def api_request(method, url_path, data=None):
    """Helper function to make a request to the Formlabs Local API"""
    kwargs = {"json": data} if data else {}
    response = request(method, f"{BASE_API_URL}{url_path}", **kwargs)
    response.raise_for_status()
    # Only some API endpoints return JSON data
    if response.headers.get("Content-Type", "").startswith("application/json"):
        return response.json()
    return None


def create_and_submit_print_job(
    print_setting_json: SceneSettings,
    selected_printer_id: str,
    job_name: str,
    print_now: bool,
) -> PrintOperationId:
    """Use the Formlabs Local API to create a print job and submit it to a printer"""
    # Create an empty Formlabs Local API scene based on the selected print setting
    api_request("POST", "/scene/", print_setting_json)
    # Import a test model (in a real application this would be a user-designed model)
    api_request("POST", "/scene/import-model/", {"file": str(TEST_FILE_PATH)})
    # Submit the print job to the selected printer
    response_data = api_request(
        "POST",
        "/scene/print/?async=true",
        {
            "printer": selected_printer_id,
            "job_name": job_name,
            "print_now": print_now,
        },
    )
    return response_data["operationId"]


def update_status_text_and_progress_bar(text: str, progress: float | None = None) -> None:
    global progress_label_textvar, progress_label, progress_bar_value, progress_bar
    progress_label_textvar.set(text)
    progress_label.update()
    if progress is not None:
        progress_bar_value.set(progress)
        progress_bar.grid()
    else:
        progress_bar.grid_remove()  # hide progress bar


def poll_print_status(operation_id: PrintOperationId) -> None:
    """Poll the status of a print job operation until it is complete and update the UI"""
    while True:
        data = api_request("GET", f"/operations/{operation_id}/")
        if data["status"] == "SUCCEEDED":
            update_status_text_and_progress_bar("Print job uploaded successfully!")
            break
        elif data["status"] == "FAILED":
            update_status_text_and_progress_bar(f"Print job upload failed! Error: {data['result']['error']['message']}")
            break
        else:
            update_status_text_and_progress_bar(f"Progress: {data['progress']*100:.2f}%", data["progress"] * 100)
            time.sleep(SLICING_PROGRESS_POLL_INTERVAL_S)


def upload_print(state: AppState, print_now: bool = False) -> None:
    """Submit a print job to the selected printer with the selected print setting"""
    if not state.selected_printer:
        messagebox.showerror("Error", "No printer selected.")
        return
    if not state.selected_print_setting:
        messagebox.showerror("Error", "No print setting selected.")
        return
    if not state.job_name:
        messagebox.showerror("Error", "Job Name cannot be empty.")
        return

    update_status_text_and_progress_bar("Print operation started...", 0)

    operation_id = create_and_submit_print_job(
        state.get_selected_print_setting_json(),
        state.get_selected_printer_id(),
        state.job_name,
        print_now,
    )
    poll_print_status(operation_id)


def sync_printer_dropdown_with_state(state: AppState) -> None:
    global selected_printer, printer_selection_menu
    printer_selection_menu["values"] = state.printer_selection_menu_options
    selected_printer.set(state.selected_printer)


def sync_print_setting_dropdown_with_state(state: AppState) -> None:
    global print_setting_selection_menu, selected_print_setting
    print_setting_selection_menu["values"] = state.print_setting_selection_menu_options
    selected_print_setting.set(state.selected_print_setting)


def on_add_printer_by_ip_pressed(state: AppState) -> None:
    """Use the Formlabs Local API to attempt to discover a printer at the given IP address"""
    ip_address = simpledialog.askstring(title="Add Printer by IP Address", prompt="Printer IP Address:")
    if ip_address is not None and len(ip_address) > 0:
        try:
            response_json = api_request(
                "POST",
                "/discover-devices/",
                {"timeout_seconds": 10, "ip_address": ip_address},
            )
            if response_json["count"] > 0:
                messagebox.showinfo("Success", f"Printer successfully added")
            else:
                messagebox.showerror("Error", "No printers found at the provided IP address.")
                # Failing to find a printer an IP address could remove a printer from the list
            get_printers_and_sync_dropdown(state)
        except HTTPError as err:
            if err.response.status_code == 400:
                messagebox.showerror("Error", "No printers found at the provided IP address.")
            else:
                messagebox.showerror("Error", "Unexpected error occurred.")


def update_login_ui_state(state: AppState) -> None:
    if state.logged_in_username:
        web_login_logout_button.configure(text=f"Logout {state.logged_in_username}")
    else:
        web_login_logout_button.configure(text="Formlabs Account Login")


def on_login_logout_button_pressed(state: AppState) -> None:
    """Use the Formlabs Local API to login to a user's Formlabs Account.
    Formlabs Accounts are needed for remote printing and Fleet Control uploads.
    """
    if state.logged_in_username:
        api_request("POST", "/logout/")
        state.logged_in_access_token = ""
        state.logged_in_username = ""
        update_login_ui_state(state)
        messagebox.showinfo("Success", f"Logged out.")
        get_printers_and_sync_dropdown(state)
    else:
        username = simpledialog.askstring(title="Login to Dashboard", prompt="Username:")
        if username is not None and len(username) > 0:
            password = simpledialog.askstring(title="Login to Dashboard", prompt="Password:")
            if password is not None and len(password) > 0:
                try:
                    access_tokens = api_request("POST", "/login/", {"username": username, "password": password})
                    state.logged_in_access_token = access_tokens["access_token"]
                    user_data = api_request("GET", "/user/")
                    state.logged_in_username = user_data["username"]
                    update_login_ui_state(state)
                    # Deal with the delay between logging in and getting new remote printers or printer groups
                    time.sleep(5)
                    messagebox.showinfo("Success", f"Logged in as {username}")
                    # Refresh list of printers to include the new Printer Groups
                    get_printers_and_sync_dropdown(state)
                except HTTPError as err:
                    messagebox.showinfo("Error", f"Login failed.")


def discover_printers_button_pressed(state: AppState) -> None:
    """Use the Formlabs Local API to discover printers on the local network"""
    messagebox.showinfo("Discover Printers", f"Starting to Discover Printers for 10s")
    d = api_request("POST", "/discover-devices/", {"timeout_seconds": 10})
    get_printers_and_sync_dropdown(state)
    messagebox.showinfo("Discover Printers", f"Discovery Finished. Found {d['count']} devices.")


def get_printers_and_sync_dropdown(state: AppState) -> None:
    """Refresh the list of available printers and sync the dropdown menu with the new state"""
    state.update_printers()
    sync_printer_dropdown_with_state(state)


def sync_printing_button_options(state: AppState) -> None:
    """Enable or disable the print buttons based on the selected printer's readiness"""
    global queue_print_button, print_now_button
    if state.selected_printer:
        device_data = state.available_printers[state.selected_printer]
        ready_to_print_now = device_data.get("ready_to_print_now", False)
        if ready_to_print_now:
            print_now_button["state"] = "normal"
        else:
            print_now_button["state"] = "disabled"
        queue_print_button["state"] = "normal"
    else:
        queue_print_button["state"] = "disabled"
        print_now_button["state"] = "disabled"


################################ GUI Setup
root = tk.Tk()
root.title("Demo Print Dialog")
root.geometry("500x300")

################################# Start PreFormServer in background
print("Starting PreFormServer...")
local_api_server = formlabs.PreFormApi.start_preform_sync(pathToPreformServer=server_path)
print("PreFormServer started.")


################################# Stop PreFormServer on exit
def clean_up_preformserver():
    global local_api_server
    if local_api_server:
        local_api_server.stop_preform_server()
        print("PreFormServer stopped.")


atexit.register(clean_up_preformserver)


def _quit():
    root.quit()
    root.destroy()
    clean_up_preformserver()


root.protocol("WM_DELETE_WINDOW", _quit)

################################# State
state: AppState = AppState()

################################# UI State Variables
selected_printer_type = tk.StringVar(root)
selected_printer_type.set(state.selected_printer_type)
selected_printer = tk.StringVar(root)
selected_printer.set(state.selected_printer)
selected_print_setting = tk.StringVar(root)
selected_print_setting.set(state.selected_print_setting)
job_name = tk.StringVar(root)
job_name.set(state.job_name)
progress_label_textvar = tk.StringVar(root)
progress_bar_value = tk.DoubleVar()

################################# UI Elements:
top_frame = tk.Frame(root)
top_frame.pack(anchor="w", padx=10, pady=10)

web_login_logout_button = tk.Button(
    top_frame,
    text="Formlabs Account Login",
    command=lambda: on_login_logout_button_pressed(state),
)
web_login_logout_button.grid(row=0, column=0, sticky="w")

add_printer_button = tk.Button(
    top_frame,
    text="Add Printer by IP",
    command=lambda: on_add_printer_by_ip_pressed(state),
)
add_printer_button.grid(row=0, column=1, sticky="w")

discover_printers_button = tk.Button(
    top_frame,
    text="Discover Printers",
    command=lambda: discover_printers_button_pressed(state),
)
discover_printers_button.grid(row=0, column=2, sticky="w")

frame = tk.Frame(root)
frame.pack(anchor="w", padx=10, pady=10)

printer_type_selection_label = tk.Label(frame, text="Printer Type: ")
printer_type_selection_label.grid(row=0, column=0, sticky="w")

printer_type_selection_menu = ttk.Combobox(frame, width=15, state="readonly", textvariable=selected_printer_type)
printer_type_selection_menu["values"] = state.available_printer_types
printer_type_selection_menu.grid(row=0, column=1, sticky="w")

printer_selection_label = tk.Label(frame, text="Printer: ")
printer_selection_label.grid(row=1, column=0, sticky="w")

printer_selection_menu = ttk.Combobox(frame, width=34, state="readonly", textvariable=selected_printer)
printer_selection_menu["values"] = state.printer_selection_menu_options
printer_selection_menu.grid(row=1, column=1, sticky="w")

print_setting_selection_label = tk.Label(frame, text="Print Setting: ")
print_setting_selection_label.grid(row=2, column=0, sticky="w")

print_setting_selection_menu = ttk.Combobox(frame, width=34, state="readonly", textvariable=selected_print_setting)
print_setting_selection_menu["values"] = state.print_setting_selection_menu_options
print_setting_selection_menu.grid(row=2, column=1, sticky="w")

job_name_label = tk.Label(frame, text="Job Name: ")
job_name_label.grid(row=3, column=0, sticky="w")
job_name_entry = tk.Entry(frame, textvariable=job_name)
job_name_entry.grid(row=3, column=1, sticky="w")

print_buttons_frame = tk.Frame(frame)
print_buttons_frame.grid(row=4, column=1, sticky="w")
queue_print_button = tk.Button(
    print_buttons_frame,
    text="Upload to Queue",
    command=lambda: upload_print(state),
)
queue_print_button.pack(side=tk.LEFT)

print_now_button = tk.Button(
    print_buttons_frame,
    text="Print Now",
    command=lambda: upload_print(state, print_now=True),
)
print_now_button.pack(side=tk.LEFT)

bottom_frame = tk.Frame(root)
bottom_frame.pack(anchor="w", padx=10, pady=10)

progress_label = tk.Label(bottom_frame, textvariable=progress_label_textvar)
progress_label.grid(row=0, column=0, sticky="w")
progress_bar = ttk.Progressbar(
    bottom_frame,
    orient="horizontal",
    length=200,
    mode="determinate",
    variable=progress_bar_value,
)
progress_bar.grid(row=1, column=0, sticky="w")
progress_bar.grid_remove()  # Hide it initially


################################# Setup event handling after UI elements exist:
def on_selected_printer_type_change(state: AppState, selected_printer_type: tk.StringVar) -> None:
    state.set_selected_printer_type(selected_printer_type.get())
    sync_printer_dropdown_with_state(state)
    sync_print_setting_dropdown_with_state(state)
    sync_printing_button_options(state)


def on_selected_printer_change(state: AppState, selected_printer: tk.StringVar) -> None:
    state.selected_printer = selected_printer.get()
    sync_printing_button_options(state)


def on_selected_print_setting_change(state: AppState, selected_print_setting: tk.StringVar) -> None:
    state.selected_print_setting = selected_print_setting.get()


def on_job_name_change(state: AppState, job_name: tk.StringVar) -> None:
    state.job_name = job_name.get()


selected_printer_type.trace_add(
    "write",
    lambda n, i, m: on_selected_printer_type_change(state, selected_printer_type),
)
selected_printer_type.trace_add(
    "write",
    lambda n, i, m: on_selected_printer_type_change(state, selected_printer_type),
)
selected_printer.trace_add("write", lambda n, i, m: on_selected_printer_change(state, selected_printer))
selected_print_setting.trace_add(
    "write",
    lambda n, i, m: on_selected_print_setting_change(state, selected_print_setting),
)
job_name.trace_add("write", lambda n, i, m: on_job_name_change(state, job_name))

update_login_ui_state(state)
sync_printing_button_options(state)

################################# Run main event loop
root.mainloop()
