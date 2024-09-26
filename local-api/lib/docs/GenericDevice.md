# GenericDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**product_name** | **str** |  | 
**status** | **str** |  | 
**is_connected** | **bool** |  | 
**connection_type** | **str** |  | 
**ip_address** | **str** |  | 
**firmware_version** | **str** |  | 

## Example

```python
from formlabs_local_api.models.generic_device import GenericDevice

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDevice from a JSON string
generic_device_instance = GenericDevice.from_json(json)
# print the JSON string representation of the object
print(GenericDevice.to_json())

# convert the object into a dict
generic_device_dict = generic_device_instance.to_dict()
# create an instance of GenericDevice from a dict
generic_device_from_dict = GenericDevice.from_dict(generic_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


