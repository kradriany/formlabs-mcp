# Tank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | 
**material** | **str** |  | [optional] 
**layers_printed** | **int** |  | [optional] 
**print_time_ms** | **int** |  | [optional] 
**heatmap** | **str** |  | [optional] 
**heatmap_gif** | **str** |  | [readonly] 
**mechanical_version** | **str** |  | [optional] 
**manufacture_date** | **datetime** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**lot_number** | **str** |  | [optional] 
**layer_count** | **int** |  | [optional] 
**last_modified** | **datetime** |  | [readonly] 
**inside_printer** | **str** |  | [readonly] 
**write_count** | **int** |  | [optional] 
**tank_type** | **str** |  | [optional] 
**connected_group** | **str** |  | [optional] 
**first_fill_date** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**last_print_date** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.tank import Tank

# TODO update the JSON string below
json = "{}"
# create an instance of Tank from a JSON string
tank_instance = Tank.from_json(json)
# print the JSON string representation of the object
print(Tank.to_json())

# convert the object into a dict
tank_dict = tank_instance.to_dict()
# create an instance of Tank from a dict
tank_from_dict = Tank.from_dict(tank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


