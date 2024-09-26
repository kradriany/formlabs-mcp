# DeveloperAPIGroupMembershipUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Email address of the member to update | 
**is_admin** | **bool** | Change if the member is an administrator | [optional] 

## Example

```python
from formlabs_web_api.models.developer_api_group_membership_update_request import DeveloperAPIGroupMembershipUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIGroupMembershipUpdateRequest from a JSON string
developer_api_group_membership_update_request_instance = DeveloperAPIGroupMembershipUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIGroupMembershipUpdateRequest.to_json())

# convert the object into a dict
developer_api_group_membership_update_request_dict = developer_api_group_membership_update_request_instance.to_dict()
# create an instance of DeveloperAPIGroupMembershipUpdateRequest from a dict
developer_api_group_membership_update_request_from_dict = DeveloperAPIGroupMembershipUpdateRequest.from_dict(developer_api_group_membership_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


