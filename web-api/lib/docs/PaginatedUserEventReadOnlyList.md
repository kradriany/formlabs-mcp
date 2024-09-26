# PaginatedUserEventReadOnlyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[UserEventReadOnly]**](UserEventReadOnly.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_user_event_read_only_list import PaginatedUserEventReadOnlyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserEventReadOnlyList from a JSON string
paginated_user_event_read_only_list_instance = PaginatedUserEventReadOnlyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserEventReadOnlyList.to_json())

# convert the object into a dict
paginated_user_event_read_only_list_dict = paginated_user_event_read_only_list_instance.to_dict()
# create an instance of PaginatedUserEventReadOnlyList from a dict
paginated_user_event_read_only_list_from_dict = PaginatedUserEventReadOnlyList.from_dict(paginated_user_event_read_only_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


