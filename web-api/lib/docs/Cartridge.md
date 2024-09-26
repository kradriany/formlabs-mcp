# Cartridge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | 
**machine_type_id** | [**MachineTypeIdAdbEnum**](MachineTypeIdAdbEnum.md) | Available values are: &#x60;FORM-1-0&#x60; - Form 1   &#x60;FORM-1-1&#x60; - Form 1+   &#x60;FORM-2-0&#x60; - Form 2   &#x60;FORM-2-1&#x60; - Form 2.1   &#x60;FORM-3-0&#x60; - Form 3   &#x60;FORM-3-1&#x60; - Form 3   &#x60;FORM-3-2&#x60; - Form 3+   &#x60;DGJR-1-0&#x60; - Form 3   &#x60;FRML-3-0&#x60; - Form 3L   &#x60;FRBL-3-0&#x60; - Form 3BL   &#x60;FRMB-3-0&#x60; - Form 3B   &#x60;DGSR-1-0&#x60; - Form 3L   &#x60;FRMB-3-1&#x60; - Form 3B+   &#x60;PILK-1-0&#x60; - Fuse 1   &#x60;SIFT-1&#x60; - Sift   &#x60;UNKNOWN&#x60; - Unknown   &#x60;PILK-1-1&#x60; - Fuse 1   &#x60;SIFT-1-0&#x60; - Sift   &#x60;SIFT-1-1&#x60; - Sift   &#x60;CURL-1-1&#x60; - Cure L   &#x60;CURL-1-0&#x60; - Cure L   &#x60;WSHL-1-0&#x60; - Wash L   &#x60;FS30-1-0&#x60; - Fuse 1+ (30W)   &#x60;FS30-1-1&#x60; - Fuse 1+ (30W)   &#x60;FORM-4-0&#x60; - Form 4 | [optional] 
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


