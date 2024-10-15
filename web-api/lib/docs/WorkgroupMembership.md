# WorkgroupMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_admin** | **bool** |  | [optional] 
**user** | **str** |  | [readonly] 
**email** | **str** |  | [readonly] 
**first_name** | **str** |  | [readonly] 
**last_name** | **str** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.workgroup_membership import WorkgroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of WorkgroupMembership from a JSON string
workgroup_membership_instance = WorkgroupMembership.from_json(json)
# print the JSON string representation of the object
print(WorkgroupMembership.to_json())

# convert the object into a dict
workgroup_membership_dict = workgroup_membership_instance.to_dict()
# create an instance of WorkgroupMembership from a dict
workgroup_membership_from_dict = WorkgroupMembership.from_dict(workgroup_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


