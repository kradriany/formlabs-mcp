# AddDrainHoles200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugs** | [**ModelsSelectionModel**](ModelsSelectionModel.md) |  | [optional] 
**warnings** | **List[str]** |  | [optional] 
**infos** | **List[str]** |  | [optional] 

## Example

```python
from formlabs_local_api.models.add_drain_holes200_response import AddDrainHoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddDrainHoles200Response from a JSON string
add_drain_holes200_response_instance = AddDrainHoles200Response.from_json(json)
# print the JSON string representation of the object
print(AddDrainHoles200Response.to_json())

# convert the object into a dict
add_drain_holes200_response_dict = add_drain_holes200_response_instance.to_dict()
# create an instance of AddDrainHoles200Response from a dict
add_drain_holes200_response_from_dict = AddDrainHoles200Response.from_dict(add_drain_holes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


