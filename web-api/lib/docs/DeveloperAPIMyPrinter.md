# DeveloperAPIMyPrinter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [readonly] 
**alias** | **str** |  | [readonly] 
**machine_type_id** | **str** |  | [readonly] 
**printer_status** | [**MyDeepPrinterStatus**](MyDeepPrinterStatus.md) |  | [readonly] 
**cartridge_status** | [**PrinterCartridgeStatus**](PrinterCartridgeStatus.md) | The status of the printer&#39;s cartridges. If the printer has multiple cartridges, this will be a list of statuses. | [readonly] 
**tank_status** | [**PrinterTankStatus**](PrinterTankStatus.md) |  | [readonly] 
**group** | [**PrinterGroup**](PrinterGroup.md) |  | [readonly] 
**previous_print_run** | **Dict[str, object]** |  | [readonly] 
**firmware_version** | **str** |  | [readonly] 
**location** | **str** | This is a user defined physical location of the printer | [readonly] 

## Example

```python
from formlabs_web_api.models.developer_apimy_printer import DeveloperAPIMyPrinter

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIMyPrinter from a JSON string
developer_apimy_printer_instance = DeveloperAPIMyPrinter.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIMyPrinter.to_json())

# convert the object into a dict
developer_apimy_printer_dict = developer_apimy_printer_instance.to_dict()
# create an instance of DeveloperAPIMyPrinter from a dict
developer_apimy_printer_from_dict = DeveloperAPIMyPrinter.from_dict(developer_apimy_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


