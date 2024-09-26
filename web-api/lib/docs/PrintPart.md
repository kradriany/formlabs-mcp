# PrintPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**guid** | **str** |  | [readonly] 
**display_name** | **str** |  | [optional] 
**end_layer** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**raw_mesh_hash** | **str** |  | [optional] 
**start_layer** | **int** |  | [optional] 
**volume_ml** | **float** |  | [optional] 
**prepared_scene** | **str** |  | 

## Example

```python
from formlabs_web_api.models.print_part import PrintPart

# TODO update the JSON string below
json = "{}"
# create an instance of PrintPart from a JSON string
print_part_instance = PrintPart.from_json(json)
# print the JSON string representation of the object
print(PrintPart.to_json())

# convert the object into a dict
print_part_dict = print_part_instance.to_dict()
# create an instance of PrintPart from a dict
print_part_from_dict = PrintPart.from_dict(print_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


