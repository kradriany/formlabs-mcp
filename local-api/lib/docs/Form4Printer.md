# Form4Printer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**product_name** | **str** |  | 
**status** | **str** |  | 
**is_connected** | **bool** |  | 
**connection_type** | **str** |  | 
**ip_address** | **str** |  | 
**firmware_version** | **str** |  | 
**is_remote_print_enabled** | **bool** |  | 
**estimated_print_time_remaining_ms** | **int** |  | 
**tank_id** | **str** |  | 
**tank_material_code** | **str** |  | 
**cartridge_data** | [**Dict[str, Form4PrinterCartridgeDataValue]**](Form4PrinterCartridgeDataValue.md) |  | 
**ready_to_print_now** | **bool** |  | 

## Example

```python
from formlabs_local_api.models.form4_printer import Form4Printer

# TODO update the JSON string below
json = "{}"
# create an instance of Form4Printer from a JSON string
form4_printer_instance = Form4Printer.from_json(json)
# print the JSON string representation of the object
print(Form4Printer.to_json())

# convert the object into a dict
form4_printer_dict = form4_printer_instance.to_dict()
# create an instance of Form4Printer from a dict
form4_printer_from_dict = Form4Printer.from_dict(form4_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


