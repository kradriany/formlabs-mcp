# LabelPart400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**LabelPart400ResponseError**](LabelPart400ResponseError.md) |  | [optional] 

## Example

```python
from formlabs_local_api.models.label_part400_response import LabelPart400Response

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPart400Response from a JSON string
label_part400_response_instance = LabelPart400Response.from_json(json)
# print the JSON string representation of the object
print(LabelPart400Response.to_json())

# convert the object into a dict
label_part400_response_dict = label_part400_response_instance.to_dict()
# create an instance of LabelPart400Response from a dict
label_part400_response_from_dict = LabelPart400Response.from_dict(label_part400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


