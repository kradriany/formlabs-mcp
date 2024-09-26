# PaginatedWorkgroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Workgroup]**](Workgroup.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_workgroup_list import PaginatedWorkgroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWorkgroupList from a JSON string
paginated_workgroup_list_instance = PaginatedWorkgroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWorkgroupList.to_json())

# convert the object into a dict
paginated_workgroup_list_dict = paginated_workgroup_list_instance.to_dict()
# create an instance of PaginatedWorkgroupList from a dict
paginated_workgroup_list_from_dict = PaginatedWorkgroupList.from_dict(paginated_workgroup_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


