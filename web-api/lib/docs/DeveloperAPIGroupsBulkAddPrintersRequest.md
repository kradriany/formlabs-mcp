# DeveloperAPIGroupsBulkAddPrintersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_group** | **str** |  | 
**printers** | **List[object]** |  | 

## Example

```python
from formlabs_web_api.models.developer_api_groups_bulk_add_printers_request import DeveloperAPIGroupsBulkAddPrintersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIGroupsBulkAddPrintersRequest from a JSON string
developer_api_groups_bulk_add_printers_request_instance = DeveloperAPIGroupsBulkAddPrintersRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIGroupsBulkAddPrintersRequest.to_json())

# convert the object into a dict
developer_api_groups_bulk_add_printers_request_dict = developer_api_groups_bulk_add_printers_request_instance.to_dict()
# create an instance of DeveloperAPIGroupsBulkAddPrintersRequest from a dict
developer_api_groups_bulk_add_printers_request_from_dict = DeveloperAPIGroupsBulkAddPrintersRequest.from_dict(developer_api_groups_bulk_add_printers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


