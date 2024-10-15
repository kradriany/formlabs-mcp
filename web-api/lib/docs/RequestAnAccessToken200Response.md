# RequestAnAccessToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**scope** | **str** |  | [optional] 

## Example

```python
from formlabs_web_api.models.request_an_access_token200_response import RequestAnAccessToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAnAccessToken200Response from a JSON string
request_an_access_token200_response_instance = RequestAnAccessToken200Response.from_json(json)
# print the JSON string representation of the object
print(RequestAnAccessToken200Response.to_json())

# convert the object into a dict
request_an_access_token200_response_dict = request_an_access_token200_response_instance.to_dict()
# create an instance of RequestAnAccessToken200Response from a dict
request_an_access_token200_response_from_dict = RequestAnAccessToken200Response.from_dict(request_an_access_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


