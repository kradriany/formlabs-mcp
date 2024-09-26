# Fuse11Printer


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
**bed_temperature_c** | **float** |  | 
**powder_level** | **str** |  | 
**printing_layer** | **int** |  | 
**printing_guid** | **str** |  | 
**cylinder_material_code** | **str** |  | 
**cylinder_serial** | **str** |  | 
**printer_material_code** | **str** |  | 
**powder_credit_g** | **float** |  | 

## Example

```python
from formlabs_local_api.models.fuse11_printer import Fuse11Printer

# TODO update the JSON string below
json = "{}"
# create an instance of Fuse11Printer from a JSON string
fuse11_printer_instance = Fuse11Printer.from_json(json)
# print the JSON string representation of the object
print(Fuse11Printer.to_json())

# convert the object into a dict
fuse11_printer_dict = fuse11_printer_instance.to_dict()
# create an instance of Fuse11Printer from a dict
fuse11_printer_from_dict = Fuse11Printer.from_dict(fuse11_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


