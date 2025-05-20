# HollowModel400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failures** | **List[str]** | The IDs of models the hollowing operation failed for | [optional] 

## Example

```python
from formlabs_local_api.models.hollow_model400_response import HollowModel400Response

# TODO update the JSON string below
json = "{}"
# create an instance of HollowModel400Response from a JSON string
hollow_model400_response_instance = HollowModel400Response.from_json(json)
# print the JSON string representation of the object
print(HollowModel400Response.to_json())

# convert the object into a dict
hollow_model400_response_dict = hollow_model400_response_instance.to_dict()
# create an instance of HollowModel400Response from a dict
hollow_model400_response_from_dict = HollowModel400Response.from_dict(hollow_model400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


