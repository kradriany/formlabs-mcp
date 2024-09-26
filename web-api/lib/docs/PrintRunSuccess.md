# PrintRunSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**print_run** | **str** |  | 
**print_run_success** | [**PrintRunSuccessEnum**](PrintRunSuccessEnum.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.print_run_success import PrintRunSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of PrintRunSuccess from a JSON string
print_run_success_instance = PrintRunSuccess.from_json(json)
# print the JSON string representation of the object
print(PrintRunSuccess.to_json())

# convert the object into a dict
print_run_success_dict = print_run_success_instance.to_dict()
# create an instance of PrintRunSuccess from a dict
print_run_success_from_dict = PrintRunSuccess.from_dict(print_run_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


