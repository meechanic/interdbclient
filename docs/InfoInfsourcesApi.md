# interdbclient.InfoInfsourcesApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_infsources_create**](InfoInfsourcesApi.md#info_infsources_create) | **POST** /info-infsources/ | 
[**info_infsources_delete**](InfoInfsourcesApi.md#info_infsources_delete) | **DELETE** /info-infsources/{id}/ | 
[**info_infsources_list**](InfoInfsourcesApi.md#info_infsources_list) | **GET** /info-infsources/ | 
[**info_infsources_partial_update**](InfoInfsourcesApi.md#info_infsources_partial_update) | **PATCH** /info-infsources/{id}/ | 
[**info_infsources_read**](InfoInfsourcesApi.md#info_infsources_read) | **GET** /info-infsources/{id}/ | 
[**info_infsources_update**](InfoInfsourcesApi.md#info_infsources_update) | **PUT** /info-infsources/{id}/ | 


# **info_infsources_create**
> Infsource info_infsources_create(data)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
data = interdbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.info_infsources_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_infsources_delete**
> info_infsources_delete(id)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.

try:
    api_instance.info_infsources_delete(id)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_infsources_list**
> list[Infsource] info_infsources_list(name=name, search=search, ordering=ordering)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.info_infsources_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[Infsource]**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_infsources_partial_update**
> Infsource info_infsources_partial_update(id, data)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.
data = interdbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.info_infsources_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_infsources_read**
> Infsource info_infsources_read(id)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.

try:
    api_response = api_instance.info_infsources_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_infsources_update**
> Infsource info_infsources_update(id, data)



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
api_instance = interdbclient.InfoInfsourcesApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this infsource.
data = interdbclient.Infsource() # Infsource | 

try:
    api_response = api_instance.info_infsources_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoInfsourcesApi->info_infsources_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this infsource. | 
 **data** | [**Infsource**](Infsource.md)|  | 

### Return type

[**Infsource**](Infsource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

