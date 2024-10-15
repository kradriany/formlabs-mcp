# Cartridge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | 
**consumable_type** | **str** |  | [optional] 
**machine_type_id** | **str** |  | [optional] 
**material** | **str** |  | [optional] 
**initial_volume_ml** | **float** |  | [optional] 
**volume_dispensed_ml** | **float** |  | [optional] 
**dispense_count** | **int** |  | [optional] 
**write_count** | **int** |  | [optional] 
**mechanical_version** | **str** |  | [optional] 
**manufacture_date** | **datetime** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**lot_number** | **str** |  | [optional] 
**last_modified** | **datetime** |  | [readonly] 
**is_empty** | **bool** |  | [readonly] 
**inside_printer** | **str** |  | [readonly] 
**connected_group** | **str** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**last_print_date** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.cartridge import Cartridge

# TODO update the JSON string below
json = "{}"
# create an instance of Cartridge from a JSON string
cartridge_instance = Cartridge.from_json(json)
# print the JSON string representation of the object
print(Cartridge.to_json())

# convert the object into a dict
cartridge_dict = cartridge_instance.to_dict()
# create an instance of Cartridge from a dict
cartridge_from_dict = Cartridge.from_dict(cartridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


