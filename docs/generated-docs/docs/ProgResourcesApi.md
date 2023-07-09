# interdbclient.ProgResourcesApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prog_resources_create**](ProgResourcesApi.md#prog_resources_create) | **POST** /prog-resources/ | 
[**prog_resources_delete**](ProgResourcesApi.md#prog_resources_delete) | **DELETE** /prog-resources/{id}/ | 
[**prog_resources_list**](ProgResourcesApi.md#prog_resources_list) | **GET** /prog-resources/ | 
[**prog_resources_partial_update**](ProgResourcesApi.md#prog_resources_partial_update) | **PATCH** /prog-resources/{id}/ | 
[**prog_resources_read**](ProgResourcesApi.md#prog_resources_read) | **GET** /prog-resources/{id}/ | 
[**prog_resources_update**](ProgResourcesApi.md#prog_resources_update) | **PUT** /prog-resources/{id}/ | 


# **prog_resources_create**
> ProgResource prog_resources_create(data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
data = interdbclient.ProgResource() # ProgResource | 

try:
    api_response = api_instance.prog_resources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProgResource**](ProgResource.md)|  | 

### Return type

[**ProgResource**](ProgResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_resources_delete**
> prog_resources_delete(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_instance.prog_resources_delete(id)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_resources_list**
> list[ProgResource] prog_resources_list(text=text, search=search, ordering=ordering)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
text = 'text_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.prog_resources_list(text=text, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[ProgResource]**](ProgResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_resources_partial_update**
> ProgResource prog_resources_partial_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = interdbclient.ProgResource() # ProgResource | 

try:
    api_response = api_instance.prog_resources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**ProgResource**](ProgResource.md)|  | 

### Return type

[**ProgResource**](ProgResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_resources_read**
> ProgResource prog_resources_read(id)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_response = api_instance.prog_resources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 

### Return type

[**ProgResource**](ProgResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_resources_update**
> ProgResource prog_resources_update(id, data)



API endpoint that represents a list of objects.

### Example
```python
from __future__ import print_function
import time
import interdbclient
from interdbclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = interdbclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = interdbclient.ProgResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = interdbclient.ProgResource() # ProgResource | 

try:
    api_response = api_instance.prog_resources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgResourcesApi->prog_resources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**ProgResource**](ProgResource.md)|  | 

### Return type

[**ProgResource**](ProgResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

