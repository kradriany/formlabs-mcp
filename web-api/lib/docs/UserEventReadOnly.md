# UserEventReadOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**printer** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**print_run** | [**MyPrintRunReadOnly**](MyPrintRunReadOnly.md) |  | [readonly] 
**tank** | **str** |  | [readonly] 
**cartridge** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 
**type_label** | **str** |  | [readonly] 
**action** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**was_read** | **bool** |  | [readonly] 
**group** | [**PrinterGroup**](PrinterGroup.md) |  | 

## Example

```python
from formlabs_web_api.models.user_event_read_only import UserEventReadOnly

# TODO update the JSON string below
json = "{}"
# create an instance of UserEventReadOnly from a JSON string
user_event_read_only_instance = UserEventReadOnly.from_json(json)
# print the JSON string representation of the object
print(UserEventReadOnly.to_json())

# convert the object into a dict
user_event_read_only_dict = user_event_read_only_instance.to_dict()
# create an instance of UserEventReadOnly from a dict
user_event_read_only_from_dict = UserEventReadOnly.from_dict(user_event_read_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


