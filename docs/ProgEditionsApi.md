# interdbclient.ProgEditionsApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prog_editions_create**](ProgEditionsApi.md#prog_editions_create) | **POST** /prog-editions/ | 
[**prog_editions_delete**](ProgEditionsApi.md#prog_editions_delete) | **DELETE** /prog-editions/{id}/ | 
[**prog_editions_list**](ProgEditionsApi.md#prog_editions_list) | **GET** /prog-editions/ | 
[**prog_editions_partial_update**](ProgEditionsApi.md#prog_editions_partial_update) | **PATCH** /prog-editions/{id}/ | 
[**prog_editions_read**](ProgEditionsApi.md#prog_editions_read) | **GET** /prog-editions/{id}/ | 
[**prog_editions_update**](ProgEditionsApi.md#prog_editions_update) | **PUT** /prog-editions/{id}/ | 


# **prog_editions_create**
> ProgEdition prog_editions_create(data)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
data = interdbclient.ProgEdition() # ProgEdition | 

try:
    api_response = api_instance.prog_editions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProgEdition**](ProgEdition.md)|  | 

### Return type

[**ProgEdition**](ProgEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_editions_delete**
> prog_editions_delete(id)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.

try:
    api_instance.prog_editions_delete(id)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_delete: %s\n" % e)
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

# **prog_editions_list**
> list[ProgEdition] prog_editions_list(name=name, search=search, ordering=ordering)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
name = 'name_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.prog_editions_list(name=name, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[ProgEdition]**](ProgEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_editions_partial_update**
> ProgEdition prog_editions_partial_update(id, data)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.
data = interdbclient.ProgEdition() # ProgEdition | 

try:
    api_response = api_instance.prog_editions_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 
 **data** | [**ProgEdition**](ProgEdition.md)|  | 

### Return type

[**ProgEdition**](ProgEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_editions_read**
> ProgEdition prog_editions_read(id)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.

try:
    api_response = api_instance.prog_editions_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 

### Return type

[**ProgEdition**](ProgEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_editions_update**
> ProgEdition prog_editions_update(id, data)



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
api_instance = interdbclient.ProgEditionsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this edition.
data = interdbclient.ProgEdition() # ProgEdition | 

try:
    api_response = api_instance.prog_editions_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgEditionsApi->prog_editions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this edition. | 
 **data** | [**ProgEdition**](ProgEdition.md)|  | 

### Return type

[**ProgEdition**](ProgEdition.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

