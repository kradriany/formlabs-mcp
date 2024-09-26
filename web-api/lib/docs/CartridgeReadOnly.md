# CartridgeReadOnly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [readonly] 
**material** | **str** |  | [readonly] 
**initial_volume_ml** | **float** |  | [readonly] 
**volume_dispensed_ml** | **float** |  | [readonly] 
**display_name** | **str** |  | [optional] 
**is_empty** | **bool** |  | [readonly] 
**inside_printer** | **str** |  | [readonly] 
**connected_group** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**last_print_date** | **datetime** |  | [readonly] 
**machine_type_id** | [**MachineTypeIdAdbEnum**](MachineTypeIdAdbEnum.md) | Available values are: &#x60;FORM-1-0&#x60; - Form 1   &#x60;FORM-1-1&#x60; - Form 1+   &#x60;FORM-2-0&#x60; - Form 2   &#x60;FORM-2-1&#x60; - Form 2.1   &#x60;FORM-3-0&#x60; - Form 3   &#x60;FORM-3-1&#x60; - Form 3   &#x60;FORM-3-2&#x60; - Form 3+   &#x60;DGJR-1-0&#x60; - Form 3   &#x60;FRML-3-0&#x60; - Form 3L   &#x60;FRBL-3-0&#x60; - Form 3BL   &#x60;FRMB-3-0&#x60; - Form 3B   &#x60;DGSR-1-0&#x60; - Form 3L   &#x60;FRMB-3-1&#x60; - Form 3B+   &#x60;PILK-1-0&#x60; - Fuse 1   &#x60;SIFT-1&#x60; - Sift   &#x60;UNKNOWN&#x60; - Unknown   &#x60;PILK-1-1&#x60; - Fuse 1   &#x60;SIFT-1-0&#x60; - Sift   &#x60;SIFT-1-1&#x60; - Sift   &#x60;CURL-1-1&#x60; - Cure L   &#x60;CURL-1-0&#x60; - Cure L   &#x60;WSHL-1-0&#x60; - Wash L   &#x60;FS30-1-0&#x60; - Fuse 1+ (30W)   &#x60;FS30-1-1&#x60; - Fuse 1+ (30W)   &#x60;FORM-4-0&#x60; - Form 4 | [readonly] 

## Example

```python
from formlabs_web_api.models.cartridge_read_only import CartridgeReadOnly

# TODO update the JSON string below
json = "{}"
# create an instance of CartridgeReadOnly from a JSON string
cartridge_read_only_instance = CartridgeReadOnly.from_json(json)
# print the JSON string representation of the object
print(CartridgeReadOnly.to_json())

# convert the object into a dict
cartridge_read_only_dict = cartridge_read_only_instance.to_dict()
# create an instance of CartridgeReadOnly from a dict
cartridge_read_only_from_dict = CartridgeReadOnly.from_dict(cartridge_read_only_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


