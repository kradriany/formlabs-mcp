# SaveScreenshotRequestFlyaroundTransform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transform** | [**List[SaveScreenshotRequestFlyaroundTransformTransformInner]**](SaveScreenshotRequestFlyaroundTransformTransformInner.md) |  | [optional] 
**frame_count** | **float** | The desired number of frames in the animation. | [optional] 
**ensure_constant_size** | **bool** | Whether or not to ensure that every frame in the animation is the same size. | [optional] 

## Example

```python
from formlabs_local_api.models.save_screenshot_request_flyaround_transform import SaveScreenshotRequestFlyaroundTransform

# TODO update the JSON string below
json = "{}"
# create an instance of SaveScreenshotRequestFlyaroundTransform from a JSON string
save_screenshot_request_flyaround_transform_instance = SaveScreenshotRequestFlyaroundTransform.from_json(json)
# print the JSON string representation of the object
print(SaveScreenshotRequestFlyaroundTransform.to_json())

# convert the object into a dict
save_screenshot_request_flyaround_transform_dict = save_screenshot_request_flyaround_transform_instance.to_dict()
# create an instance of SaveScreenshotRequestFlyaroundTransform from a dict
save_screenshot_request_flyaround_transform_from_dict = SaveScreenshotRequestFlyaroundTransform.from_dict(save_screenshot_request_flyaround_transform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


