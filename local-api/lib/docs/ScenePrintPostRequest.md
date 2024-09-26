# ScenePrintPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**printer** | **str** | Printer serial name, IP address, or Fleet Control Queue ID | 
**job_name** | **str** |  | [optional] 

## Example

```python
from formlabs_local_api.models.scene_print_post_request import ScenePrintPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScenePrintPostRequest from a JSON string
scene_print_post_request_instance = ScenePrintPostRequest.from_json(json)
# print the JSON string representation of the object
print(ScenePrintPostRequest.to_json())

# convert the object into a dict
scene_print_post_request_dict = scene_print_post_request_instance.to_dict()
# create an instance of ScenePrintPostRequest from a dict
scene_print_post_request_from_dict = ScenePrintPostRequest.from_dict(scene_print_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


