# SceneModelsIdReplacePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | Full path to the file to load | [optional] 
**repair_behavior** | [**RepairBehaviorModel**](RepairBehaviorModel.md) |  | [optional] [default to RepairBehaviorModel.IGNORE]

## Example

```python
from formlabs_local_api.models.scene_models_id_replace_post_request import SceneModelsIdReplacePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneModelsIdReplacePostRequest from a JSON string
scene_models_id_replace_post_request_instance = SceneModelsIdReplacePostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneModelsIdReplacePostRequest.to_json())

# convert the object into a dict
scene_models_id_replace_post_request_dict = scene_models_id_replace_post_request_instance.to_dict()
# create an instance of SceneModelsIdReplacePostRequest from a dict
scene_models_id_replace_post_request_from_dict = SceneModelsIdReplacePostRequest.from_dict(scene_models_id_replace_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


