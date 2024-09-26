# Form2Printer


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
**estimated_print_time_remaining_ms** | **int** |  | 
**tank_id** | **str** |  | 
**tank_material_code** | **str** |  | 
**cartridge_data** | [**Dict[str, Form4PrinterCartridgeDataValue]**](Form4PrinterCartridgeDataValue.md) |  | 

## Example

```python
from formlabs_local_api.models.form2_printer import Form2Printer

# TODO update the JSON string below
json = "{}"
# create an instance of Form2Printer from a JSON string
form2_printer_instance = Form2Printer.from_json(json)
# print the JSON string representation of the object
print(Form2Printer.to_json())

# convert the object into a dict
form2_printer_dict = form2_printer_instance.to_dict()
# create an instance of Form2Printer from a dict
form2_printer_from_dict = Form2Printer.from_dict(form2_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


