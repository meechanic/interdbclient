# interdbclient.InterProginfosApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inter_proginfos_create**](InterProginfosApi.md#inter_proginfos_create) | **POST** /inter-proginfos/ | 
[**inter_proginfos_delete**](InterProginfosApi.md#inter_proginfos_delete) | **DELETE** /inter-proginfos/{id}/ | 
[**inter_proginfos_list**](InterProginfosApi.md#inter_proginfos_list) | **GET** /inter-proginfos/ | 
[**inter_proginfos_partial_update**](InterProginfosApi.md#inter_proginfos_partial_update) | **PATCH** /inter-proginfos/{id}/ | 
[**inter_proginfos_read**](InterProginfosApi.md#inter_proginfos_read) | **GET** /inter-proginfos/{id}/ | 
[**inter_proginfos_update**](InterProginfosApi.md#inter_proginfos_update) | **PUT** /inter-proginfos/{id}/ | 


# **inter_proginfos_create**
> ProgInfo inter_proginfos_create(data)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
data = interdbclient.ProgInfo() # ProgInfo | 

try:
    api_response = api_instance.inter_proginfos_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProgInfo**](ProgInfo.md)|  | 

### Return type

[**ProgInfo**](ProgInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_proginfos_delete**
> inter_proginfos_delete(id)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prog info.

try:
    api_instance.inter_proginfos_delete(id)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prog info. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_proginfos_list**
> list[ProgInfo] inter_proginfos_list(prog_package=prog_package, info_infsource=info_infsource, search=search, ordering=ordering)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
prog_package = 'prog_package_example' # str |  (optional)
info_infsource = 'info_infsource_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.inter_proginfos_list(prog_package=prog_package, info_infsource=info_infsource, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prog_package** | **str**|  | [optional] 
 **info_infsource** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[ProgInfo]**](ProgInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_proginfos_partial_update**
> ProgInfo inter_proginfos_partial_update(id, data)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prog info.
data = interdbclient.ProgInfo() # ProgInfo | 

try:
    api_response = api_instance.inter_proginfos_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prog info. | 
 **data** | [**ProgInfo**](ProgInfo.md)|  | 

### Return type

[**ProgInfo**](ProgInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_proginfos_read**
> ProgInfo inter_proginfos_read(id)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prog info.

try:
    api_response = api_instance.inter_proginfos_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prog info. | 

### Return type

[**ProgInfo**](ProgInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_proginfos_update**
> ProgInfo inter_proginfos_update(id, data)



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
api_instance = interdbclient.InterProginfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prog info.
data = interdbclient.ProgInfo() # ProgInfo | 

try:
    api_response = api_instance.inter_proginfos_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterProginfosApi->inter_proginfos_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prog info. | 
 **data** | [**ProgInfo**](ProgInfo.md)|  | 

### Return type

[**ProgInfo**](ProgInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

