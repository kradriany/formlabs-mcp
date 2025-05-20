# SaveScreenshotRequestFlyaroundTransformTransformInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yaw** | **float** | Yaw rotation in degrees for the camera&#39;s view, where 0º looks down the negative X-axis | 
**pitch** | **float** | Pitch rotation in degrees for the camera&#39;s view, where 0º looks flat from the horizon and positive angles look down on models (in SLA scenes, toward the build platform) | 

## Example

```python
from formlabs_local_api.models.save_screenshot_request_flyaround_transform_transform_inner import SaveScreenshotRequestFlyaroundTransformTransformInner

# TODO update the JSON string below
json = "{}"
# create an instance of SaveScreenshotRequestFlyaroundTransformTransformInner from a JSON string
save_screenshot_request_flyaround_transform_transform_inner_instance = SaveScreenshotRequestFlyaroundTransformTransformInner.from_json(json)
# print the JSON string representation of the object
print(SaveScreenshotRequestFlyaroundTransformTransformInner.to_json())

# convert the object into a dict
save_screenshot_request_flyaround_transform_transform_inner_dict = save_screenshot_request_flyaround_transform_transform_inner_instance.to_dict()
# create an instance of SaveScreenshotRequestFlyaroundTransformTransformInner from a dict
save_screenshot_request_flyaround_transform_transform_inner_from_dict = SaveScreenshotRequestFlyaroundTransformTransformInner.from_dict(save_screenshot_request_flyaround_transform_transform_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


