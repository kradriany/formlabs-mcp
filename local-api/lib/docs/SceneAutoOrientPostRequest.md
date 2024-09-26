# SceneAutoOrientPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**ModelsSelectionModel**](ModelsSelectionModel.md) |  | 
**mode** | **str** |  | 
**tilt** | **int** | Degrees of tilt. Only applies to the DENTAL mode | [optional] 

## Example

```python
from formlabs_local_api.models.scene_auto_orient_post_request import SceneAutoOrientPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneAutoOrientPostRequest from a JSON string
scene_auto_orient_post_request_instance = SceneAutoOrientPostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneAutoOrientPostRequest.to_json())

# convert the object into a dict
scene_auto_orient_post_request_dict = scene_auto_orient_post_request_instance.to_dict()
# create an instance of SceneAutoOrientPostRequest from a dict
scene_auto_orient_post_request_from_dict = SceneAutoOrientPostRequest.from_dict(scene_auto_orient_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


