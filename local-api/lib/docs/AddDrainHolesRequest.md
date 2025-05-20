# AddDrainHolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | The ID of the model to add drain holes to | 
**drain_holes** | [**List[DrainHoleModel]**](DrainHoleModel.md) | List of drain holes to add | 

## Example

```python
from formlabs_local_api.models.add_drain_holes_request import AddDrainHolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDrainHolesRequest from a JSON string
add_drain_holes_request_instance = AddDrainHolesRequest.from_json(json)
# print the JSON string representation of the object
print(AddDrainHolesRequest.to_json())

# convert the object into a dict
add_drain_holes_request_dict = add_drain_holes_request_instance.to_dict()
# create an instance of AddDrainHolesRequest from a dict
add_drain_holes_request_from_dict = AddDrainHolesRequest.from_dict(add_drain_holes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


