# interdbclient.InterInfoinfosApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inter_infoinfos_create**](InterInfoinfosApi.md#inter_infoinfos_create) | **POST** /inter-infoinfos/ | 
[**inter_infoinfos_delete**](InterInfoinfosApi.md#inter_infoinfos_delete) | **DELETE** /inter-infoinfos/{id}/ | 
[**inter_infoinfos_list**](InterInfoinfosApi.md#inter_infoinfos_list) | **GET** /inter-infoinfos/ | 
[**inter_infoinfos_partial_update**](InterInfoinfosApi.md#inter_infoinfos_partial_update) | **PATCH** /inter-infoinfos/{id}/ | 
[**inter_infoinfos_read**](InterInfoinfosApi.md#inter_infoinfos_read) | **GET** /inter-infoinfos/{id}/ | 
[**inter_infoinfos_update**](InterInfoinfosApi.md#inter_infoinfos_update) | **PUT** /inter-infoinfos/{id}/ | 


# **inter_infoinfos_create**
> InfoInfo inter_infoinfos_create(data)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
data = interdbclient.InfoInfo() # InfoInfo | 

try:
    api_response = api_instance.inter_infoinfos_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InfoInfo**](InfoInfo.md)|  | 

### Return type

[**InfoInfo**](InfoInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_infoinfos_delete**
> inter_infoinfos_delete(id)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this info info.

try:
    api_instance.inter_infoinfos_delete(id)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this info info. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_infoinfos_list**
> list[InfoInfo] inter_infoinfos_list(first_info_infsource=first_info_infsource, second_info_infsource=second_info_infsource, search=search, ordering=ordering)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
first_info_infsource = 'first_info_infsource_example' # str |  (optional)
second_info_infsource = 'second_info_infsource_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.inter_infoinfos_list(first_info_infsource=first_info_infsource, second_info_infsource=second_info_infsource, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_info_infsource** | **str**|  | [optional] 
 **second_info_infsource** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[InfoInfo]**](InfoInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_infoinfos_partial_update**
> InfoInfo inter_infoinfos_partial_update(id, data)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this info info.
data = interdbclient.InfoInfo() # InfoInfo | 

try:
    api_response = api_instance.inter_infoinfos_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this info info. | 
 **data** | [**InfoInfo**](InfoInfo.md)|  | 

### Return type

[**InfoInfo**](InfoInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_infoinfos_read**
> InfoInfo inter_infoinfos_read(id)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this info info.

try:
    api_response = api_instance.inter_infoinfos_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this info info. | 

### Return type

[**InfoInfo**](InfoInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inter_infoinfos_update**
> InfoInfo inter_infoinfos_update(id, data)



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
api_instance = interdbclient.InterInfoinfosApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this info info.
data = interdbclient.InfoInfo() # InfoInfo | 

try:
    api_response = api_instance.inter_infoinfos_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InterInfoinfosApi->inter_infoinfos_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this info info. | 
 **data** | [**InfoInfo**](InfoInfo.md)|  | 

### Return type

[**InfoInfo**](InfoInfo.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

