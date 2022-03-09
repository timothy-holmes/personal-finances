# swagger_client.UtilityEndpointsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**util_ping_get**](UtilityEndpointsApi.md#util_ping_get) | **GET** /util/ping | Ping

# **util_ping_get**
> PingResponse util_ping_get()

Ping

Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP `200` status is returned. On failure an HTTP `401` error response is returned. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UtilityEndpointsApi(swagger_client.ApiClient(configuration))

try:
    # Ping
    api_response = api_instance.util_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityEndpointsApi->util_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

