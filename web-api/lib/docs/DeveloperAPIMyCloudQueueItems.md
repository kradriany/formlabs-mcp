# DeveloperAPIMyCloudQueueItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** |  | 
**volume_ml** | **float** |  | 
**material_name** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**username** | **str** |  | 
**allowed_machine_type_ids** | **List[str]** |  | [optional] 

## Example

```python
from formlabs_web_api.models.developer_apimy_cloud_queue_items import DeveloperAPIMyCloudQueueItems

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIMyCloudQueueItems from a JSON string
developer_apimy_cloud_queue_items_instance = DeveloperAPIMyCloudQueueItems.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIMyCloudQueueItems.to_json())

# convert the object into a dict
developer_apimy_cloud_queue_items_dict = developer_apimy_cloud_queue_items_instance.to_dict()
# create an instance of DeveloperAPIMyCloudQueueItems from a dict
developer_apimy_cloud_queue_items_from_dict = DeveloperAPIMyCloudQueueItems.from_dict(developer_apimy_cloud_queue_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


