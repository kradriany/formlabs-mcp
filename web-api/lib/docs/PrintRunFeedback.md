# PrintRunFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**print_run** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**issue_category** | **str** |  | [optional] 
**issue_subcategory** | **str** |  | [optional] 
**issue_description** | **str** |  | [optional] 
**form_file_exists** | **bool** |  | [readonly] 

## Example

```python
from formlabs_web_api.models.print_run_feedback import PrintRunFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of PrintRunFeedback from a JSON string
print_run_feedback_instance = PrintRunFeedback.from_json(json)
# print the JSON string representation of the object
print(PrintRunFeedback.to_json())

# convert the object into a dict
print_run_feedback_dict = print_run_feedback_instance.to_dict()
# create an instance of PrintRunFeedback from a dict
print_run_feedback_from_dict = PrintRunFeedback.from_dict(print_run_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


