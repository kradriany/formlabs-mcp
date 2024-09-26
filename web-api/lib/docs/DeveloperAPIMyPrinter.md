# DeveloperAPIMyPrinter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **str** |  | [readonly] 
**machine_type_id** | [**DeveloperAPIMyPrinterMachineTypeIdEnum**](DeveloperAPIMyPrinterMachineTypeIdEnum.md) | Available values are: &#x60;FORM-1-0&#x60; - Form 1   &#x60;FORM-1-1&#x60; - Form 1+   &#x60;FORM-2-0&#x60; - Form 2   &#x60;FORM-2-1&#x60; - Form 2.1   &#x60;FORM-3-0&#x60; - Form 3   &#x60;FORM-3-1&#x60; - Form 3   &#x60;FORM-3-2&#x60; - Form 3+   &#x60;DGJR-1-0&#x60; - Form 3   &#x60;FRML-3-0&#x60; - Form 3L   &#x60;FRBL-3-0&#x60; - Form 3BL   &#x60;FRMB-3-0&#x60; - Form 3B   &#x60;DGSR-1-0&#x60; - Form 3L   &#x60;FRMB-3-1&#x60; - Form 3B+   &#x60;PILK-1-0&#x60; - Fuse 1   &#x60;SIFT-1&#x60; - Sift   &#x60;UNKNOWN&#x60; - Unknown   &#x60;PILK-1-1&#x60; - Fuse 1   &#x60;SIFT-1-0&#x60; - Sift   &#x60;SIFT-1-1&#x60; - Sift   &#x60;CURL-1-1&#x60; - Cure L   &#x60;CURL-1-0&#x60; - Cure L   &#x60;WSHL-1-0&#x60; - Wash L   &#x60;FS30-1-0&#x60; - Fuse 1+ (30W)   &#x60;FS30-1-1&#x60; - Fuse 1+ (30W)   &#x60;FORM-4-0&#x60; - Form 4 | [readonly] 
**total_print_time_ms** | **int** |  | [readonly] 
**total_number_of_prints** | [**DeveloperAPIMyPrinterTotalNumberOfPrints**](DeveloperAPIMyPrinterTotalNumberOfPrints.md) |  | 
**printer_status** | [**MyDeepPrinterStatus**](MyDeepPrinterStatus.md) |  | [readonly] 
**cartridge_status** | [**PrinterCartridgeStatus**](PrinterCartridgeStatus.md) |  | [readonly] 
**tank_status** | [**PrinterTankStatus**](PrinterTankStatus.md) |  | [readonly] 
**group** | [**PrinterGroup**](PrinterGroup.md) |  | [readonly] 
**previous_print_run** | **Dict[str, object]** |  | [readonly] 
**firmware_version** | **str** |  | [readonly] 
**location** | **str** | This is a user defined physical location of the printer | [readonly] 

## Example

```python
from formlabs_web_api.models.developer_apimy_printer import DeveloperAPIMyPrinter

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperAPIMyPrinter from a JSON string
developer_apimy_printer_instance = DeveloperAPIMyPrinter.from_json(json)
# print the JSON string representation of the object
print(DeveloperAPIMyPrinter.to_json())

# convert the object into a dict
developer_apimy_printer_dict = developer_apimy_printer_instance.to_dict()
# create an instance of DeveloperAPIMyPrinter from a dict
developer_apimy_printer_from_dict = DeveloperAPIMyPrinter.from_dict(developer_apimy_printer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


