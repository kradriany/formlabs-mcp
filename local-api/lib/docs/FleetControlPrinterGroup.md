# FleetControlPrinterGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**product_name** | **str** |  | 
**status** | **str** |  | 
**is_connected** | **bool** |  | 
**connection_type** | **str** |  | 
**firmware_version** | **str** |  | 
**dashboard_group_id** | **str** |  | 
**dashboard_queue_id** | **str** |  | 

## Example

```python
from formlabs_local_api.models.fleet_control_printer_group import FleetControlPrinterGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FleetControlPrinterGroup from a JSON string
fleet_control_printer_group_instance = FleetControlPrinterGroup.from_json(json)
# print the JSON string representation of the object
print(FleetControlPrinterGroup.to_json())

# convert the object into a dict
fleet_control_printer_group_dict = fleet_control_printer_group_instance.to_dict()
# create an instance of FleetControlPrinterGroup from a dict
fleet_control_printer_group_from_dict = FleetControlPrinterGroup.from_dict(fleet_control_printer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


