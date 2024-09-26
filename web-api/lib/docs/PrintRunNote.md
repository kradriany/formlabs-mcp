# PrintRunNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**print_run** | **str** |  | 
**note** | **str** |  | 
**author** | [**BasicUser**](BasicUser.md) |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.print_run_note import PrintRunNote

# TODO update the JSON string below
json = "{}"
# create an instance of PrintRunNote from a JSON string
print_run_note_instance = PrintRunNote.from_json(json)
# print the JSON string representation of the object
print(PrintRunNote.to_json())

# convert the object into a dict
print_run_note_dict = print_run_note_instance.to_dict()
# create an instance of PrintRunNote from a dict
print_run_note_from_dict = PrintRunNote.from_dict(print_run_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


