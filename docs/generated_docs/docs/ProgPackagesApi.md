# interdbclient.ProgPackagesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prog_packages_create**](ProgPackagesApi.md#prog_packages_create) | **POST** /prog-packages/ | 
[**prog_packages_delete**](ProgPackagesApi.md#prog_packages_delete) | **DELETE** /prog-packages/{id}/ | 
[**prog_packages_list**](ProgPackagesApi.md#prog_packages_list) | **GET** /prog-packages/ | 
[**prog_packages_partial_update**](ProgPackagesApi.md#prog_packages_partial_update) | **PATCH** /prog-packages/{id}/ | 
[**prog_packages_read**](ProgPackagesApi.md#prog_packages_read) | **GET** /prog-packages/{id}/ | 
[**prog_packages_update**](ProgPackagesApi.md#prog_packages_update) | **PUT** /prog-packages/{id}/ | 


# **prog_packages_create**
> Package prog_packages_create(data)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
data = interdbclient.Package() # Package | 

try:
    api_response = api_instance.prog_packages_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packages_delete**
> prog_packages_delete(id)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.

try:
    api_instance.prog_packages_delete(id)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packages_list**
> list[Package] prog_packages_list(name=name, search=search, ordering=ordering)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.prog_packages_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Package]**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packages_partial_update**
> Package prog_packages_partial_update(id, data)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.
data = interdbclient.Package() # Package | 

try:
    api_response = api_instance.prog_packages_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packages_read**
> Package prog_packages_read(id)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.

try:
    api_response = api_instance.prog_packages_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packages_update**
> Package prog_packages_update(id, data)



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
api_instance = interdbclient.ProgPackagesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package.
data = interdbclient.Package() # Package | 

try:
    api_response = api_instance.prog_packages_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagesApi->prog_packages_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

