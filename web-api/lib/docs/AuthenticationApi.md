# formlabs_web_api.AuthenticationApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_an_access_token**](AuthenticationApi.md#request_an_access_token) | **POST** /developer/v1/o/token/ | 
[**revoke_an_access_token**](AuthenticationApi.md#revoke_an_access_token) | **POST** /developer/v1/o/revoke_token/ | 


# **request_an_access_token**
> RequestAnAccessToken200Response request_an_access_token(grant_type, client_id, client_secret)


To log in to the Dashboard Developer API, you need to request an access token.
This token is used to authenticate your requests to the API.
You can request an access token by providing your client ID and client secret.
            

### Example


```python
import formlabs_web_api
from formlabs_web_api.models.request_an_access_token200_response import RequestAnAccessToken200Response
from formlabs_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.formlabs.com
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_web_api.Configuration(
    host = "https://api.formlabs.com"
)


# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.AuthenticationApi(api_client)
    grant_type = 'grant_type_example' # str | The type of grant being used. Currently only `client_credentials` is supported
    client_id = 'client_id_example' # str | Your Client ID.
    client_secret = 'client_secret_example' # str | Your Client Secret.

    try:
        api_response = api_instance.request_an_access_token(grant_type, client_id, client_secret)
        print("The response of AuthenticationApi->request_an_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->request_an_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The type of grant being used. Currently only &#x60;client_credentials&#x60; is supported | 
 **client_id** | **str**| Your Client ID. | 
 **client_secret** | **str**| Your Client Secret. | 

### Return type

[**RequestAnAccessToken200Response**](RequestAnAccessToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid credentials |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_an_access_token**
> revoke_an_access_token(token, client_id, client_secret)


You can log out from your current authenticated session by revoking the access token.
When successfully revoked, the API does not return any response.
As aforementioned, once you send a request to revoke the specified access token,
this token can no longer be used to make requests to the Dashboard Developer API.
Please retrieve a new access token to start using the API again.
            

### Example


```python
import formlabs_web_api
from formlabs_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.formlabs.com
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_web_api.Configuration(
    host = "https://api.formlabs.com"
)


# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.AuthenticationApi(api_client)
    token = 'token_example' # str | Your access token.
    client_id = 'client_id_example' # str | Your client ID.
    client_secret = 'client_secret_example' # str | Your client secret.

    try:
        api_instance.revoke_an_access_token(token, client_id, client_secret)
    except Exception as e:
        print("Exception when calling AuthenticationApi->revoke_an_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Your access token. | 
 **client_id** | **str**| Your client ID. | 
 **client_secret** | **str**| Your client secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

