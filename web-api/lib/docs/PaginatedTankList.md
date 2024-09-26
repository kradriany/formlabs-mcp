# PaginatedTankList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Tank]**](Tank.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_tank_list import PaginatedTankList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTankList from a JSON string
paginated_tank_list_instance = PaginatedTankList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTankList.to_json())

# convert the object into a dict
paginated_tank_list_dict = paginated_tank_list_instance.to_dict()
# create an instance of PaginatedTankList from a dict
paginated_tank_list_from_dict = PaginatedTankList.from_dict(paginated_tank_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


