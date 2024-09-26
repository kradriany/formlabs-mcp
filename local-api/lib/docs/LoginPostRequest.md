# LoginPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**access_token** | **str** |  | 

## Example

```python
from formlabs_local_api.models.login_post_request import LoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginPostRequest from a JSON string
login_post_request_instance = LoginPostRequest.from_json(json)
# print the JSON string representation of the object
print(LoginPostRequest.to_json())

# convert the object into a dict
login_post_request_dict = login_post_request_instance.to_dict()
# create an instance of LoginPostRequest from a dict
login_post_request_from_dict = LoginPostRequest.from_dict(login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


