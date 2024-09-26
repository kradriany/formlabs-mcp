# PrinterTankStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tank** | [**TankReadOnly**](TankReadOnly.md) |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.printer_tank_status import PrinterTankStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PrinterTankStatus from a JSON string
printer_tank_status_instance = PrinterTankStatus.from_json(json)
# print the JSON string representation of the object
print(PrinterTankStatus.to_json())

# convert the object into a dict
printer_tank_status_dict = printer_tank_status_instance.to_dict()
# create an instance of PrinterTankStatus from a dict
printer_tank_status_from_dict = PrinterTankStatus.from_dict(printer_tank_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


