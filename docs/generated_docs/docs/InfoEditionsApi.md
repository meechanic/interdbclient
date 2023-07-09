# interdbclient.InfoEditionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_editions_create**](InfoEditionsApi.md#info_editions_create) | **POST** /info-editions/ | 
[**info_editions_delete**](InfoEditionsApi.md#info_editions_delete) | **DELETE** /info-editions/{id}/ | 
[**info_editions_list**](InfoEditionsApi.md#info_editions_list) | **GET** /info-editions/ | 
[**info_editions_partial_update**](InfoEditionsApi.md#info_editions_partial_update) | **PATCH** /info-editions/{id}/ | 
[**info_editions_read**](InfoEditionsApi.md#info_editions_read) | **GET** /info-editions/{id}/ | 
[**info_editions_update**](InfoEditionsApi.md#info_editions_update) | **PUT** /info-editions/{id}/ | 


# **info_editions_create**
> InfoEdition info_editions_create(data)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
data = interdbclient.InfoEdition() # InfoEdition | 

try:
    api_response = api_instance.info_editions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**InfoEdition**](InfoEdition.md)|  | 

### Return type

[**InfoEdition**](InfoEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_editions_delete**
> info_editions_delete(id)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.

try:
    api_instance.info_editions_delete(id)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_editions_list**
> list[InfoEdition] info_editions_list(name=name, search=search, ordering=ordering)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.info_editions_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[InfoEdition]**](InfoEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_editions_partial_update**
> InfoEdition info_editions_partial_update(id, data)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.
data = interdbclient.InfoEdition() # InfoEdition | 

try:
    api_response = api_instance.info_editions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 
 **data** | [**InfoEdition**](InfoEdition.md)|  | 

### Return type

[**InfoEdition**](InfoEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_editions_read**
> InfoEdition info_editions_read(id)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.

try:
    api_response = api_instance.info_editions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 

### Return type

[**InfoEdition**](InfoEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_editions_update**
> InfoEdition info_editions_update(id, data)



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
api_instance = interdbclient.InfoEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.
data = interdbclient.InfoEdition() # InfoEdition | 

try:
    api_response = api_instance.info_editions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoEditionsApi->info_editions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 
 **data** | [**InfoEdition**](InfoEdition.md)|  | 

### Return type

[**InfoEdition**](InfoEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

