# PaginatedPrintRunWithFleetControlDataList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PrintRunWithFleetControlData]**](PrintRunWithFleetControlData.md) |  | [optional] 

## Example

```python
from formlabs_web_api.models.paginated_print_run_with_fleet_control_data_list import PaginatedPrintRunWithFleetControlDataList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPrintRunWithFleetControlDataList from a JSON string
paginated_print_run_with_fleet_control_data_list_instance = PaginatedPrintRunWithFleetControlDataList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPrintRunWithFleetControlDataList.to_json())

# convert the object into a dict
paginated_print_run_with_fleet_control_data_list_dict = paginated_print_run_with_fleet_control_data_list_instance.to_dict()
# create an instance of PaginatedPrintRunWithFleetControlDataList from a dict
paginated_print_run_with_fleet_control_data_list_from_dict = PaginatedPrintRunWithFleetControlDataList.from_dict(paginated_print_run_with_fleet_control_data_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


