# GroupsMembersDestroyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Email address of the member to remove | 

## Example

```python
from formlabs_web_api.models.groups_members_destroy_request import GroupsMembersDestroyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMembersDestroyRequest from a JSON string
groups_members_destroy_request_instance = GroupsMembersDestroyRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsMembersDestroyRequest.to_json())

# convert the object into a dict
groups_members_destroy_request_dict = groups_members_destroy_request_instance.to_dict()
# create an instance of GroupsMembersDestroyRequest from a dict
groups_members_destroy_request_from_dict = GroupsMembersDestroyRequest.from_dict(groups_members_destroy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


