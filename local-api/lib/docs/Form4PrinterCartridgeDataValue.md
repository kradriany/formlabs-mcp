# Form4PrinterCartridgeDataValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cartridge_material_code** | **str** |  | 
**cartridge_estimated_volume_dispensed_m_l** | **float** |  | 
**cartridge_original_volume_m_l** | **float** |  | 

## Example

```python
from formlabs_local_api.models.form4_printer_cartridge_data_value import Form4PrinterCartridgeDataValue

# TODO update the JSON string below
json = "{}"
# create an instance of Form4PrinterCartridgeDataValue from a JSON string
form4_printer_cartridge_data_value_instance = Form4PrinterCartridgeDataValue.from_json(json)
# print the JSON string representation of the object
print(Form4PrinterCartridgeDataValue.to_json())

# convert the object into a dict
form4_printer_cartridge_data_value_dict = form4_printer_cartridge_data_value_instance.to_dict()
# create an instance of Form4PrinterCartridgeDataValue from a dict
form4_printer_cartridge_data_value_from_dict = Form4PrinterCartridgeDataValue.from_dict(form4_printer_cartridge_data_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


