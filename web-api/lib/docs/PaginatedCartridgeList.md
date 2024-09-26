# PaginatedCartridgeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Cartridge]**](Cartridge.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_cartridge_list import PaginatedCartridgeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCartridgeList from a JSON string
paginated_cartridge_list_instance = PaginatedCartridgeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCartridgeList.to_json())

# convert the object into a dict
paginated_cartridge_list_dict = paginated_cartridge_list_instance.to_dict()
# create an instance of PaginatedCartridgeList from a dict
paginated_cartridge_list_from_dict = PaginatedCartridgeList.from_dict(paginated_cartridge_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


