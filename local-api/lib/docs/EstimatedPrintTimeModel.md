# EstimatedPrintTimeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_print_time_s** | **float** |  | [optional] 
**preprint_time_s** | **float** |  | [optional] 

## Example

```python
from formlabs_local_api.models.estimated_print_time_model import EstimatedPrintTimeModel

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedPrintTimeModel from a JSON string
estimated_print_time_model_instance = EstimatedPrintTimeModel.from_json(json)
# print the JSON string representation of the object
print(EstimatedPrintTimeModel.to_json())

# convert the object into a dict
estimated_print_time_model_dict = estimated_print_time_model_instance.to_dict()
# create an instance of EstimatedPrintTimeModel from a dict
estimated_print_time_model_from_dict = EstimatedPrintTimeModel.from_dict(estimated_print_time_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


