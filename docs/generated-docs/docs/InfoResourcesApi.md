# interdbclient.InfoResourcesApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_resources_create**](InfoResourcesApi.md#info_resources_create) | **POST** /info-resources/ | 
[**info_resources_delete**](InfoResourcesApi.md#info_resources_delete) | **DELETE** /info-resources/{id}/ | 
[**info_resources_list**](InfoResourcesApi.md#info_resources_list) | **GET** /info-resources/ | 
[**info_resources_partial_update**](InfoResourcesApi.md#info_resources_partial_update) | **PATCH** /info-resources/{id}/ | 
[**info_resources_read**](InfoResourcesApi.md#info_resources_read) | **GET** /info-resources/{id}/ | 
[**info_resources_update**](InfoResourcesApi.md#info_resources_update) | **PUT** /info-resources/{id}/ | 


# **info_resources_create**
> InfoResource info_resources_create(data)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
data = interdbclient.InfoResource() # InfoResource | 

try:
    api_response = api_instance.info_resources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InfoResource**](InfoResource.md)|  | 

### Return type

[**InfoResource**](InfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_resources_delete**
> info_resources_delete(id)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_instance.info_resources_delete(id)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_delete: %s\n" % e)
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

# **info_resources_list**
> list[InfoResource] info_resources_list(text=text, search=search, ordering=ordering)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
text = 'text_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.info_resources_list(text=text, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[InfoResource]**](InfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_resources_partial_update**
> InfoResource info_resources_partial_update(id, data)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = interdbclient.InfoResource() # InfoResource | 

try:
    api_response = api_instance.info_resources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**InfoResource**](InfoResource.md)|  | 

### Return type

[**InfoResource**](InfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_resources_read**
> InfoResource info_resources_read(id)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.

try:
    api_response = api_instance.info_resources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 

### Return type

[**InfoResource**](InfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_resources_update**
> InfoResource info_resources_update(id, data)



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
api_instance = interdbclient.InfoResourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this resource.
data = interdbclient.InfoResource() # InfoResource | 

try:
    api_response = api_instance.info_resources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoResourcesApi->info_resources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this resource. | 
 **data** | [**InfoResource**](InfoResource.md)|  | 

### Return type

[**InfoResource**](InfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

