# PaginatedDeveloperAPIMyPrinterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DeveloperAPIMyPrinter]**](DeveloperAPIMyPrinter.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_developer_apimy_printer_list import PaginatedDeveloperAPIMyPrinterList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDeveloperAPIMyPrinterList from a JSON string
paginated_developer_apimy_printer_list_instance = PaginatedDeveloperAPIMyPrinterList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDeveloperAPIMyPrinterList.to_json())

# convert the object into a dict
paginated_developer_apimy_printer_list_dict = paginated_developer_apimy_printer_list_instance.to_dict()
# create an instance of PaginatedDeveloperAPIMyPrinterList from a dict
paginated_developer_apimy_printer_list_from_dict = PaginatedDeveloperAPIMyPrinterList.from_dict(paginated_developer_apimy_printer_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


