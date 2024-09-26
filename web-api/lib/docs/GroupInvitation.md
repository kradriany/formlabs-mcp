# GroupInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**is_admin** | **bool** |  | [optional] 

## Example

```python
from formlabs_web_api.models.group_invitation import GroupInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInvitation from a JSON string
group_invitation_instance = GroupInvitation.from_json(json)
# print the JSON string representation of the object
print(GroupInvitation.to_json())

# convert the object into a dict
group_invitation_dict = group_invitation_instance.to_dict()
# create an instance of GroupInvitation from a dict
group_invitation_from_dict = GroupInvitation.from_dict(group_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


