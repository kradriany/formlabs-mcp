# DeveloperAPIGroupMembershipCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Email address of the member to invite | 
**is_admin** | **bool** | Change if the member is an administrator | [optional] 

## Example

```python
from formlabs_web_api.models.developer_api_group_membership_create_request import DeveloperAPIGroupMembershipCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIGroupMembershipCreateRequest from a JSON string
developer_api_group_membership_create_request_instance = DeveloperAPIGroupMembershipCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIGroupMembershipCreateRequest.to_json())

# convert the object into a dict
developer_api_group_membership_create_request_dict = developer_api_group_membership_create_request_instance.to_dict()
# create an instance of DeveloperAPIGroupMembershipCreateRequest from a dict
developer_api_group_membership_create_request_from_dict = DeveloperAPIGroupMembershipCreateRequest.from_dict(developer_api_group_membership_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


