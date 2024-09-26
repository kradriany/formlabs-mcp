# PatchedPartialWorkGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**remote_print_enabled_override** | **str** |  | [optional] 

## Example

```python
from formlabs_web_api.models.patched_partial_work_group_request import PatchedPartialWorkGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPartialWorkGroupRequest from a JSON string
patched_partial_work_group_request_instance = PatchedPartialWorkGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPartialWorkGroupRequest.to_json())

# convert the object into a dict
patched_partial_work_group_request_dict = patched_partial_work_group_request_instance.to_dict()
# create an instance of PatchedPartialWorkGroupRequest from a dict
patched_partial_work_group_request_from_dict = PatchedPartialWorkGroupRequest.from_dict(patched_partial_work_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


