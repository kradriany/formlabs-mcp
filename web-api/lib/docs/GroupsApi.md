# formlabs_web_api.GroupsApi

All URIs are relative to *https://api.formlabs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_create**](GroupsApi.md#groups_create) | **POST** /developer/v1/groups/ | 
[**groups_destroy**](GroupsApi.md#groups_destroy) | **DELETE** /developer/v1/groups/{group_id}/ | 
[**groups_list**](GroupsApi.md#groups_list) | **GET** /developer/v1/groups/ | 
[**groups_members_create**](GroupsApi.md#groups_members_create) | **POST** /developer/v1/groups/{group_id}/members/ | 
[**groups_members_destroy**](GroupsApi.md#groups_members_destroy) | **DELETE** /developer/v1/groups/{group_id}/members/ | 
[**groups_members_update**](GroupsApi.md#groups_members_update) | **PUT** /developer/v1/groups/{group_id}/members/ | 
[**groups_partial_update**](GroupsApi.md#groups_partial_update) | **PATCH** /developer/v1/groups/{group_id}/ | 


# **groups_create**
> NewWorkgroup groups_create(partial_work_group_request)



Create a group for my account, and make me an administrator.

### Example

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    partial_work_group_request = formlabs_web_api.PartialWorkGroupRequest() # PartialWorkGroupRequest | 

    try:
        api_response = api_instance.groups_create(partial_work_group_request)
        print("The response of GroupsApi->groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create: %s\n" % e)
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

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this workgroup.

    try:
        api_instance.groups_destroy(group_id)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_destroy: %s\n" % e)
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
> PaginatedWorkgroupList groups_list(page=page, per_page=per_page)



List of all groups for my account.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import formlabs_web_api
from formlabs_web_api.models.paginated_workgroup_list import PaginatedWorkgroupList
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
    api_instance = formlabs_web_api.GroupsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    per_page = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = api_instance.groups_list(page=page, per_page=per_page)
        print("The response of GroupsApi->groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **per_page** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedWorkgroupList**](PaginatedWorkgroupList.md)

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

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Unique UUID connected to the group
    developer_api_group_membership_create_request = formlabs_web_api.DeveloperAPIGroupMembershipCreateRequest() # DeveloperAPIGroupMembershipCreateRequest | 

    try:
        api_response = api_instance.groups_members_create(group_id, developer_api_group_membership_create_request)
        print("The response of GroupsApi->groups_members_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_members_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Unique UUID connected to the group | 
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

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Unique UUID connected to the group
    groups_members_destroy_request = formlabs_web_api.GroupsMembersDestroyRequest() # GroupsMembersDestroyRequest |  (optional)

    try:
        api_instance.groups_members_destroy(group_id, groups_members_destroy_request=groups_members_destroy_request)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_members_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Unique UUID connected to the group | 
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

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    group_id = 'group_id_example' # str | Unique UUID connected to the group
    developer_api_group_membership_update_request = formlabs_web_api.DeveloperAPIGroupMembershipUpdateRequest() # DeveloperAPIGroupMembershipUpdateRequest | 

    try:
        api_response = api_instance.groups_members_update(group_id, developer_api_group_membership_update_request)
        print("The response of GroupsApi->groups_members_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_members_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Unique UUID connected to the group | 
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

* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = formlabs_web_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with formlabs_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_web_api.GroupsApi(api_client)
    group_id = 'group_id_example' # str | A UUID string identifying this workgroup.
    patched_partial_work_group_request = formlabs_web_api.PatchedPartialWorkGroupRequest() # PatchedPartialWorkGroupRequest |  (optional)

    try:
        api_response = api_instance.groups_partial_update(group_id, patched_partial_work_group_request=patched_partial_work_group_request)
        print("The response of GroupsApi->groups_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_partial_update: %s\n" % e)
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

