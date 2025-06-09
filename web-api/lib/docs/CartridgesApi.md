# formlabs_web_api.CartridgesApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cartridges_list**](CartridgesApi.md#cartridges_list) | **GET** /developer/v1/cartridges/ | 


# **cartridges_list**
> PaginatedCartridgeList cartridges_list(page=page, per_page=per_page)

 List of all resin cartridges associated with my account

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.paginated_cartridge_list import PaginatedCartridgeList
from formlabs_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.formlabs.com
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_web_api.Configuration(
    host = "https://api.formlabs.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.CartridgesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    per_page = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.cartridges_list(page=page, per_page=per_page)
        print("The response of CartridgesApi->cartridges_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CartridgesApi->cartridges_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **per_page** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCartridgeList**](PaginatedCartridgeList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

