# NewWorkgroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**name** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**has_fleet_control** | **bool** |  | [optional] 
**has_fleet_control_updated_by** | **int** | The user who is the Fleet Control administrator of the Printer Group | [optional] 

## Example

```python
from formlabs_web_api.models.new_workgroup import NewWorkgroup

# TODO update the JSON string below
json = "{}"
# create an instance of NewWorkgroup from a JSON string
new_workgroup_instance = NewWorkgroup.from_json(json)
# print the JSON string representation of the object
print(NewWorkgroup.to_json())

# convert the object into a dict
new_workgroup_dict = new_workgroup_instance.to_dict()
# create an instance of NewWorkgroup from a dict
new_workgroup_from_dict = NewWorkgroup.from_dict(new_workgroup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


