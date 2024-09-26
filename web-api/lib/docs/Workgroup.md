# Workgroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** |  | 
**remote_print_enabled_override** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**memberships** | [**List[WorkgroupMembership]**](WorkgroupMembership.md) |  | [readonly] 
**printers** | **List[str]** |  | [readonly] 
**invitations** | [**List[GroupInvitation]**](GroupInvitation.md) |  | [readonly] 
**has_fleet_control** | **bool** |  | [optional] 
**has_fleet_control_updated_by** | **int** |  | [optional] 
**settings** | [**WorkgroupSettings**](WorkgroupSettings.md) |  | [readonly] 

## Example

```python
from formlabs_web_api.models.workgroup import Workgroup

# TODO update the JSON string below
json = "{}"
# create an instance of Workgroup from a JSON string
workgroup_instance = Workgroup.from_json(json)
# print the JSON string representation of the object
print(Workgroup.to_json())

# convert the object into a dict
workgroup_dict = workgroup_instance.to_dict()
# create an instance of Workgroup from a dict
workgroup_from_dict = Workgroup.from_dict(workgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


