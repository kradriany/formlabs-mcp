# formlabs_web_api.EventsApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_list**](EventsApi.md#events_list) | **GET** /developer/v1/events/ | 


# **events_list**
> PaginatedUserEventReadOnlyList events_list(cartridge=cartridge, date__gt=date__gt, date__lt=date__lt, page=page, per_page=per_page, print_run=print_run, printer=printer, tank=tank, type=type)



List of all events associated with my account

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.paginated_user_event_read_only_list import PaginatedUserEventReadOnlyList
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.EventsApi(api_client)
    cartridge = 'cartridge_example' # str | Filter by resin cartridge serial (optional)
    date__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter by date greater than date specified (ISO 8601 Format) (optional)
    date__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter by date less than date specified (ISO 8601 Format) (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    per_page = 56 # int | Number of results to return per page. (optional)
    print_run = 'print_run_example' # str | Filter by print id (optional)
    printer = 'printer_example' # str | Filter by printer serial (optional)
    tank = 'tank_example' # str | Filter by resin tank serial (optional)
    type = 'type_example' # str | Filter by Event Type `RESIN_LOW` or `PRINT_START` or `PRINT_FINISHED` or `PRINT_ABORTED` or `PRINT_ERROR` or `PRINT_PAUSED` or `PRINT_RESUMED` or `PRINT_RESOLUTION_REQUEST` or `PRINT_RESOLUTION` or `MANY_PRINT_ERRORS` or `PASSWORD_RESET` or `PRINTER_REGISTERED` or `PRINTER_DEREGISTERED`  (optional)

    try:
        api_response = api_instance.events_list(cartridge=cartridge, date__gt=date__gt, date__lt=date__lt, page=page, per_page=per_page, print_run=print_run, printer=printer, tank=tank, type=type)
        print("The response of EventsApi->events_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartridge** | **str**| Filter by resin cartridge serial | [optional] 
 **date__gt** | **datetime**| Filter by date greater than date specified (ISO 8601 Format) | [optional] 
 **date__lt** | **datetime**| Filter by date less than date specified (ISO 8601 Format) | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **per_page** | **int**| Number of results to return per page. | [optional] 
 **print_run** | **str**| Filter by print id | [optional] 
 **printer** | **str**| Filter by printer serial | [optional] 
 **tank** | **str**| Filter by resin tank serial | [optional] 
 **type** | **str**| Filter by Event Type &#x60;RESIN_LOW&#x60; or &#x60;PRINT_START&#x60; or &#x60;PRINT_FINISHED&#x60; or &#x60;PRINT_ABORTED&#x60; or &#x60;PRINT_ERROR&#x60; or &#x60;PRINT_PAUSED&#x60; or &#x60;PRINT_RESUMED&#x60; or &#x60;PRINT_RESOLUTION_REQUEST&#x60; or &#x60;PRINT_RESOLUTION&#x60; or &#x60;MANY_PRINT_ERRORS&#x60; or &#x60;PASSWORD_RESET&#x60; or &#x60;PRINTER_REGISTERED&#x60; or &#x60;PRINTER_DEREGISTERED&#x60;  | [optional] 

### Return type

[**PaginatedUserEventReadOnlyList**](PaginatedUserEventReadOnlyList.md)

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

