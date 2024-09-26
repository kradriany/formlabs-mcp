# SceneModelsIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the model used within job preparation. | [optional] 
**position** | [**ScenePositionModel**](ScenePositionModel.md) |  | [optional] 
**orientation** | [**OrientationModel**](OrientationModel.md) |  | [optional] 
**scale** | **float** | The scale factor to apply to the model | [optional] 
**units** | [**UnitsModel**](UnitsModel.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.scene_models_id_post_request import SceneModelsIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneModelsIdPostRequest from a JSON string
scene_models_id_post_request_instance = SceneModelsIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneModelsIdPostRequest.to_json())

# convert the object into a dict
scene_models_id_post_request_dict = scene_models_id_post_request_instance.to_dict()
# create an instance of SceneModelsIdPostRequest from a dict
scene_models_id_post_request_from_dict = SceneModelsIdPostRequest.from_dict(scene_models_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


