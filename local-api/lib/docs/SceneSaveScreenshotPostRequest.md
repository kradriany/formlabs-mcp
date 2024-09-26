# SceneSaveScreenshotPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The file path to save the .png screenshot to | 
**view_type** | **str** | The type of view to use when taking the screenshot | [optional] [default to 'ZOOM_ON_MODELS']
**models** | [**ModelsSelectionModel**](ModelsSelectionModel.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.scene_save_screenshot_post_request import SceneSaveScreenshotPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SceneSaveScreenshotPostRequest from a JSON string
scene_save_screenshot_post_request_instance = SceneSaveScreenshotPostRequest.from_json(json)
# print the JSON string representation of the object
print(SceneSaveScreenshotPostRequest.to_json())

# convert the object into a dict
scene_save_screenshot_post_request_dict = scene_save_screenshot_post_request_instance.to_dict()
# create an instance of SceneSaveScreenshotPostRequest from a dict
scene_save_screenshot_post_request_from_dict = SceneSaveScreenshotPostRequest.from_dict(scene_save_screenshot_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


