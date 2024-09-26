# FormCell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | 
**firmware_version** | **str** |  | 
**status** | **str** |  | 
**rotation** | **str** |  | 

## Example

```python
from formlabs_web_api.models.form_cell import FormCell

# TODO update the JSON string below
json = "{}"
# create an instance of FormCell from a JSON string
form_cell_instance = FormCell.from_json(json)
# print the JSON string representation of the object
print(FormCell.to_json())

# convert the object into a dict
form_cell_dict = form_cell_instance.to_dict()
# create an instance of FormCell from a dict
form_cell_from_dict = FormCell.from_dict(form_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


