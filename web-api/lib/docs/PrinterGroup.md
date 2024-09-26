# PrinterGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** |  | 

## Example

```python
from formlabs_web_api.models.printer_group import PrinterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterGroup from a JSON string
printer_group_instance = PrinterGroup.from_json(json)
# print the JSON string representation of the object
print(PrinterGroup.to_json())

# convert the object into a dict
printer_group_dict = printer_group_instance.to_dict()
# create an instance of PrinterGroup from a dict
printer_group_from_dict = PrinterGroup.from_dict(printer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


