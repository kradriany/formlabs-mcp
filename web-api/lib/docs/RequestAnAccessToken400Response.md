# RequestAnAccessToken400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from formlabs_web_api.models.request_an_access_token400_response import RequestAnAccessToken400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAnAccessToken400Response from a JSON string
request_an_access_token400_response_instance = RequestAnAccessToken400Response.from_json(json)
# print the JSON string representation of the object
print(RequestAnAccessToken400Response.to_json())

# convert the object into a dict
request_an_access_token400_response_dict = request_an_access_token400_response_instance.to_dict()
# create an instance of RequestAnAccessToken400Response from a dict
request_an_access_token400_response_from_dict = RequestAnAccessToken400Response.from_dict(request_an_access_token400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


