# interdbclient.ProgPackagetagsApi

All URIs are relative to *http://interdb.localhost2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prog_packagetags_create**](ProgPackagetagsApi.md#prog_packagetags_create) | **POST** /prog-packagetags/ | 
[**prog_packagetags_delete**](ProgPackagetagsApi.md#prog_packagetags_delete) | **DELETE** /prog-packagetags/{id}/ | 
[**prog_packagetags_list**](ProgPackagetagsApi.md#prog_packagetags_list) | **GET** /prog-packagetags/ | 
[**prog_packagetags_partial_update**](ProgPackagetagsApi.md#prog_packagetags_partial_update) | **PATCH** /prog-packagetags/{id}/ | 
[**prog_packagetags_read**](ProgPackagetagsApi.md#prog_packagetags_read) | **GET** /prog-packagetags/{id}/ | 
[**prog_packagetags_update**](ProgPackagetagsApi.md#prog_packagetags_update) | **PUT** /prog-packagetags/{id}/ | 


# **prog_packagetags_create**
> PackageTag prog_packagetags_create(data)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
data = interdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.prog_packagetags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packagetags_delete**
> prog_packagetags_delete(id)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.

try:
    api_instance.prog_packagetags_delete(id)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packagetags_list**
> list[PackageTag] prog_packagetags_list(key=key, value=value, search=search, ordering=ordering)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
key = 'key_example' # str |  (optional)
value = 'value_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

try:
    api_response = api_instance.prog_packagetags_list(key=key, value=value, search=search, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**list[PackageTag]**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packagetags_partial_update**
> PackageTag prog_packagetags_partial_update(id, data)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.
data = interdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.prog_packagetags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packagetags_read**
> PackageTag prog_packagetags_read(id)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.

try:
    api_response = api_instance.prog_packagetags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prog_packagetags_update**
> PackageTag prog_packagetags_update(id, data)



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
api_instance = interdbclient.ProgPackagetagsApi(interdbclient.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this package tag.
data = interdbclient.PackageTag() # PackageTag | 

try:
    api_response = api_instance.prog_packagetags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProgPackagetagsApi->prog_packagetags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this package tag. | 
 **data** | [**PackageTag**](PackageTag.md)|  | 

### Return type

[**PackageTag**](PackageTag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

