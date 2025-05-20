# GetSceneInterferencesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_offset_mm** | **float** | The minimum distance between models for them not to be considered interfering with each other. | [optional] 

## Example

```python
from formlabs_local_api.models.get_scene_interferences_request import GetSceneInterferencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSceneInterferencesRequest from a JSON string
get_scene_interferences_request_instance = GetSceneInterferencesRequest.from_json(json)
# print the JSON string representation of the object
print(GetSceneInterferencesRequest.to_json())

# convert the object into a dict
get_scene_interferences_request_dict = get_scene_interferences_request_instance.to_dict()
# create an instance of GetSceneInterferencesRequest from a dict
get_scene_interferences_request_from_dict = GetSceneInterferencesRequest.from_dict(get_scene_interferences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


