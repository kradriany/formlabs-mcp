# LabelPart400ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | [**LabelPart400ResponseErrorMessage**](LabelPart400ResponseErrorMessage.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.label_part400_response_error import LabelPart400ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPart400ResponseError from a JSON string
label_part400_response_error_instance = LabelPart400ResponseError.from_json(json)
# print the JSON string representation of the object
print(LabelPart400ResponseError.to_json())

# convert the object into a dict
label_part400_response_error_dict = label_part400_response_error_instance.to_dict()
# create an instance of LabelPart400ResponseError from a dict
label_part400_response_error_from_dict = LabelPart400ResponseError.from_dict(label_part400_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


