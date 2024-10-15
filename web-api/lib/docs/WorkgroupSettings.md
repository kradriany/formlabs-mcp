# WorkgroupSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | [readonly] 
**update_mode** | **str** |  | [optional] 

## Example

```python
from formlabs_web_api.models.workgroup_settings import WorkgroupSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupSettings from a JSON string
workgroup_settings_instance = WorkgroupSettings.from_json(json)
# print the JSON string representation of the object
print(WorkgroupSettings.to_json())

# convert the object into a dict
workgroup_settings_dict = workgroup_settings_instance.to_dict()
# create an instance of WorkgroupSettings from a dict
workgroup_settings_from_dict = WorkgroupSettings.from_dict(workgroup_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


