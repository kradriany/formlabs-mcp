# formlabs_web_api.PrinterGroupsApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_bulk_add_printers_create**](PrinterGroupsApi.md#groups_bulk_add_printers_create) | **POST** /developer/v1/groups/bulk-add-printers/ | 
[**groups_create**](PrinterGroupsApi.md#groups_create) | **POST** /developer/v1/groups/ | 
[**groups_destroy**](PrinterGroupsApi.md#groups_destroy) | **DELETE** /developer/v1/groups/{group_id}/ | 
[**groups_list**](PrinterGroupsApi.md#groups_list) | **GET** /developer/v1/groups/ | 
[**groups_members_create**](PrinterGroupsApi.md#groups_members_create) | **POST** /developer/v1/groups/{group_id}/members/ | 
[**groups_members_destroy**](PrinterGroupsApi.md#groups_members_destroy) | **DELETE** /developer/v1/groups/{group_id}/members/ | 
[**groups_members_update**](PrinterGroupsApi.md#groups_members_update) | **PUT** /developer/v1/groups/{group_id}/members/ | 
[**groups_partial_update**](PrinterGroupsApi.md#groups_partial_update) | **PATCH** /developer/v1/groups/{group_id}/ | 
[**groups_queue_list**](PrinterGroupsApi.md#groups_queue_list) | **GET** /developer/v1/groups/{group_id}/queue/ | 


# **groups_bulk_add_printers_create**
> groups_bulk_add_printers_create(developer_api_groups_bulk_add_printers_request)



Move Printer(s) to a Printer Group.   **Notes:** Request sender needs to be admin of target group and all of the Printers’ groups.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_api_groups_bulk_add_printers_request import DeveloperAPIGroupsBulkAddPrintersRequest
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    developer_api_groups_bulk_add_printers_request = {"target_group":"61e94a6e-8012-42fa-8fa7-642d2587bef0","printers":["SweetMatcha","CornyCaffeine"]} # DeveloperAPIGroupsBulkAddPrintersRequest | 

    try:
        api_instance.groups_bulk_add_printers_create(developer_api_groups_bulk_add_printers_request)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_bulk_add_printers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer_api_groups_bulk_add_printers_request** | [**DeveloperAPIGroupsBulkAddPrintersRequest**](DeveloperAPIGroupsBulkAddPrintersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create**
> NewWorkgroup groups_create(partial_work_group_request)



Create a group for my account, and make me an administrator.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.new_workgroup import NewWorkgroup
from formlabs_web_api.models.partial_work_group_request import PartialWorkGroupRequest
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    partial_work_group_request = formlabs_web_api.PartialWorkGroupRequest() # PartialWorkGroupRequest | 

    try:
        api_response = api_instance.groups_create(partial_work_group_request)
        print("The response of PrinterGroupsApi->groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partial_work_group_request** | [**PartialWorkGroupRequest**](PartialWorkGroupRequest.md)|  | 

### Return type

[**NewWorkgroup**](NewWorkgroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_destroy**
> groups_destroy(group_id)



Delete a group administered by my account.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this workgroup.

    try:
        api_instance.groups_destroy(group_id)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this workgroup. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_list**
> List[Workgroup] groups_list()



List of all groups for my account.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.workgroup import Workgroup
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)

    try:
        api_response = api_instance.groups_list()
        print("The response of PrinterGroupsApi->groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Workgroup]**](Workgroup.md)

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

# **groups_members_create**
> WorkgroupMembership groups_members_create(group_id, developer_api_group_membership_create_request)



Invite a user into my group.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_api_group_membership_create_request import DeveloperAPIGroupMembershipCreateRequest
from formlabs_web_api.models.workgroup_membership import WorkgroupMembership
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this Printer Group
    developer_api_group_membership_create_request = formlabs_web_api.DeveloperAPIGroupMembershipCreateRequest() # DeveloperAPIGroupMembershipCreateRequest | 

    try:
        api_response = api_instance.groups_members_create(group_id, developer_api_group_membership_create_request)
        print("The response of PrinterGroupsApi->groups_members_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this Printer Group | 
 **developer_api_group_membership_create_request** | [**DeveloperAPIGroupMembershipCreateRequest**](DeveloperAPIGroupMembershipCreateRequest.md)|  | 

### Return type

[**WorkgroupMembership**](WorkgroupMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_members_destroy**
> groups_members_destroy(group_id, groups_members_destroy_request=groups_members_destroy_request)



Delete a membership in an administered group.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.groups_members_destroy_request import GroupsMembersDestroyRequest
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this Printer Group
    groups_members_destroy_request = formlabs_web_api.GroupsMembersDestroyRequest() # GroupsMembersDestroyRequest |  (optional)

    try:
        api_instance.groups_members_destroy(group_id, groups_members_destroy_request=groups_members_destroy_request)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_members_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this Printer Group | 
 **groups_members_destroy_request** | [**GroupsMembersDestroyRequest**](GroupsMembersDestroyRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_members_update**
> WorkgroupMembership groups_members_update(group_id, developer_api_group_membership_update_request)



Update a membership in an administered group.   **Warning: You cannot revoke the administrator right of yourself if there are no other administrators!**

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_api_group_membership_update_request import DeveloperAPIGroupMembershipUpdateRequest
from formlabs_web_api.models.workgroup_membership import WorkgroupMembership
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this Printer Group
    developer_api_group_membership_update_request = formlabs_web_api.DeveloperAPIGroupMembershipUpdateRequest() # DeveloperAPIGroupMembershipUpdateRequest | 

    try:
        api_response = api_instance.groups_members_update(group_id, developer_api_group_membership_update_request)
        print("The response of PrinterGroupsApi->groups_members_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this Printer Group | 
 **developer_api_group_membership_update_request** | [**DeveloperAPIGroupMembershipUpdateRequest**](DeveloperAPIGroupMembershipUpdateRequest.md)|  | 

### Return type

[**WorkgroupMembership**](WorkgroupMembership.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_partial_update**
> Workgroup groups_partial_update(group_id, patched_partial_work_group_request=patched_partial_work_group_request)



Update a group administered by my account.

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.patched_partial_work_group_request import PatchedPartialWorkGroupRequest
from formlabs_web_api.models.workgroup import Workgroup
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this workgroup.
    patched_partial_work_group_request = formlabs_web_api.PatchedPartialWorkGroupRequest() # PatchedPartialWorkGroupRequest |  (optional)

    try:
        api_response = api_instance.groups_partial_update(group_id, patched_partial_work_group_request=patched_partial_work_group_request)
        print("The response of PrinterGroupsApi->groups_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this workgroup. | 
 **patched_partial_work_group_request** | [**PatchedPartialWorkGroupRequest**](PatchedPartialWorkGroupRequest.md)|  | [optional] 

### Return type

[**Workgroup**](Workgroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_queue_list**
> List[DeveloperAPIMyCloudQueueItems] groups_queue_list(group_id)



 List of all items in the queue of a group. A Printer Group can only have a queue if the group has Fleet Control turned on. For non-Fleet Control groups, the queue is always empty and the call returns empty.          

### Example

* Bearer Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.developer_apimy_cloud_queue_items import DeveloperAPIMyCloudQueueItems
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
    api_instance = formlabs_web_api.PrinterGroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this Printer Group

    try:
        api_response = api_instance.groups_queue_list(group_id)
        print("The response of PrinterGroupsApi->groups_queue_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrinterGroupsApi->groups_queue_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| A UUID string identifying this Printer Group | 

### Return type

[**List[DeveloperAPIMyCloudQueueItems]**](DeveloperAPIMyCloudQueueItems.md)

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

