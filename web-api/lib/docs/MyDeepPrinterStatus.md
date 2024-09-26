# MyDeepPrinterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [readonly] 
**last_pinged_at** | **datetime** |  | [optional] 
**hopper_level** | **int** |  | [optional] 
**material_credit** | **float** |  | [optional] 
**hopper_material** | **str** |  | [optional] 
**last_modified** | **datetime** |  | [readonly] 
**current_temperature** | **float** |  | [optional] 
**current_print_run** | [**MyPrintRunReadOnly**](MyPrintRunReadOnly.md) |  | [readonly] 
**form_cell** | [**FormCell**](FormCell.md) |  | [readonly] 
**last_printer_cooldown_started** | **datetime** |  | [optional] 
**outer_boundary_offset_corrections** | **object** |  | [optional] 
**build_platform_contents** | [**BuildPlatformContentsEnum**](BuildPlatformContentsEnum.md) |  | [optional] 
**tank_mixer_state** | [**TankMixerStateEnum**](TankMixerStateEnum.md) |  | [optional] 
**ready_to_print** | [**ReadyToPrintEnum**](ReadyToPrintEnum.md) |  | [optional] 
**printer_capabilities** | **List[str]** |  | [optional] 
**printernet_capabilities** | **List[str]** |  | [optional] 
**camera_status** | [**CameraStatusEnum**](CameraStatusEnum.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.my_deep_printer_status import MyDeepPrinterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MyDeepPrinterStatus from a JSON string
my_deep_printer_status_instance = MyDeepPrinterStatus.from_json(json)
# print the JSON string representation of the object
print(MyDeepPrinterStatus.to_json())

# convert the object into a dict
my_deep_printer_status_dict = my_deep_printer_status_instance.to_dict()
# create an instance of MyDeepPrinterStatus from a dict
my_deep_printer_status_from_dict = MyDeepPrinterStatus.from_dict(my_deep_printer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


