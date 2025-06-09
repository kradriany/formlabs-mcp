# formlabs_web_api.PrintersApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**printers_list**](PrintersApi.md#printers_list) | **GET** /developer/v1/printers/ | 
[**printers_retrieve**](PrintersApi.md#printers_retrieve) | **GET** /developer/v1/printers/{printer_serial}/ | 


# **printers_list**
> List[DeveloperAPIMyPrinter] printers_list()

List of all Printers associated with my account

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_apimy_printer import DeveloperAPIMyPrinter
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
    api_instance = formlabs_web_api.PrintersApi(api_client)

    try:
        api_response = api_instance.printers_list()
        print("The response of PrintersApi->printers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintersApi->printers_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DeveloperAPIMyPrinter]**](DeveloperAPIMyPrinter.md)

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

# **printers_retrieve**
> DeveloperAPIMyPrinter printers_retrieve(printer_serial)

Specific Printer associated with my account

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_apimy_printer import DeveloperAPIMyPrinter
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
    api_instance = formlabs_web_api.PrintersApi(api_client)
    printer_serial = 'printer_serial_example' # str | A unique value identifying this printer.

    try:
        api_response = api_instance.printers_retrieve(printer_serial)
        print("The response of PrintersApi->printers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrintersApi->printers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **printer_serial** | **str**| A unique value identifying this printer. | 

### Return type

[**DeveloperAPIMyPrinter**](DeveloperAPIMyPrinter.md)

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

