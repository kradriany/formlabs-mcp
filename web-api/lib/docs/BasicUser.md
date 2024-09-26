# BasicUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from formlabs_web_api.models.basic_user import BasicUser

# TODO update the JSON string below
json = "{}"
# create an instance of BasicUser from a JSON string
basic_user_instance = BasicUser.from_json(json)
# print the JSON string representation of the object
print(BasicUser.to_json())

# convert the object into a dict
basic_user_dict = basic_user_instance.to_dict()
# create an instance of BasicUser from a dict
basic_user_from_dict = BasicUser.from_dict(basic_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


