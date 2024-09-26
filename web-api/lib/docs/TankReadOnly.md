# TankReadOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [readonly] 
**material** | **str** |  | [readonly] 
**print_time_ms** | **int** |  | [readonly] 
**layers_printed** | **int** |  | [readonly] 
**first_fill_date** | **datetime** |  | [readonly] 
**heatmap** | **str** |  | [optional] 
**heatmap_gif** | **str** |  | [readonly] 
**display_name** | **str** |  | [optional] 
**layer_count** | **int** |  | [readonly] 
**inside_printer** | **str** |  | [readonly] 
**tank_type** | **str** |  | [readonly] 
**connected_group** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**last_print_date** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.tank_read_only import TankReadOnly

# TODO update the JSON string below
json = "{}"
# create an instance of TankReadOnly from a JSON string
tank_read_only_instance = TankReadOnly.from_json(json)
# print the JSON string representation of the object
print(TankReadOnly.to_json())

# convert the object into a dict
tank_read_only_dict = tank_read_only_instance.to_dict()
# create an instance of TankReadOnly from a dict
tank_read_only_from_dict = TankReadOnly.from_dict(tank_read_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


