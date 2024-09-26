# SceneAutoPackPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_spacing_mm** | **float** | The minimum spacing between models when packing | [optional] 

## Example

```python
from formlabs_local_api.models.scene_auto_pack_post_request import SceneAutoPackPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneAutoPackPostRequest from a JSON string
scene_auto_pack_post_request_instance = SceneAutoPackPostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneAutoPackPostRequest.to_json())

# convert the object into a dict
scene_auto_pack_post_request_dict = scene_auto_pack_post_request_instance.to_dict()
# create an instance of SceneAutoPackPostRequest from a dict
scene_auto_pack_post_request_from_dict = SceneAutoPackPostRequest.from_dict(scene_auto_pack_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


