# DiscoverDevicesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_seconds** | **int** | Number of seconds to wait when discovering devices | [optional] 
**ip_address** | **str** | Local network IP address to attempt to discover a device at | [optional] 

## Example

```python
from formlabs_local_api.models.discover_devices_post_request import DiscoverDevicesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverDevicesPostRequest from a JSON string
discover_devices_post_request_instance = DiscoverDevicesPostRequest.from_json(json)
# print the JSON string representation of the object
print(DiscoverDevicesPostRequest.to_json())

# convert the object into a dict
discover_devices_post_request_dict = discover_devices_post_request_instance.to_dict()
# create an instance of DiscoverDevicesPostRequest from a dict
discover_devices_post_request_from_dict = DiscoverDevicesPostRequest.from_dict(discover_devices_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


