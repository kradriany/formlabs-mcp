# SceneModelsIdReplacePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | [optional] 
**model_properties** | [**ModelProperties**](ModelProperties.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.scene_models_id_replace_post200_response import SceneModelsIdReplacePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SceneModelsIdReplacePost200Response from a JSON string
scene_models_id_replace_post200_response_instance = SceneModelsIdReplacePost200Response.from_json(json)
# print the JSON string representation of the object
print(SceneModelsIdReplacePost200Response.to_json())

# convert the object into a dict
scene_models_id_replace_post200_response_dict = scene_models_id_replace_post200_response_instance.to_dict()
# create an instance of SceneModelsIdReplacePost200Response from a dict
scene_models_id_replace_post200_response_from_dict = SceneModelsIdReplacePost200Response.from_dict(scene_models_id_replace_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


