# swagger_client.TagsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | List tags
[**transactions_transaction_id_relationships_tags_delete**](TagsApi.md#transactions_transaction_id_relationships_tags_delete) | **DELETE** /transactions/{transactionId}/relationships/tags | Remove tags from transaction
[**transactions_transaction_id_relationships_tags_post**](TagsApi.md#transactions_transaction_id_relationships_tags_post) | **POST** /transactions/{transactionId}/relationships/tags | Add tags to transaction

# **tags_get**
> ListTagsResponse tags_get(page_size=page_size)

List tags

Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered lexicographically. The `transactions` relationship for each tag exposes a link to get the transactions with the given tag. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The number of records to return in each page.  (optional)

try:
    # List tags
    api_response = api_instance.tags_get(page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 

### Return type

[**ListTagsResponse**](ListTagsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_relationships_tags_delete**
> transactions_transaction_id_relationships_tags_delete(transaction_id)

Remove tags from transaction

Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP `204` is returned on success. The associated tags, along with this request URL, are also exposed via the `tags` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | The unique identifier for the transaction. 

try:
    # Remove tags from transaction
    api_instance.transactions_transaction_id_relationships_tags_delete(transaction_id)
except ApiException as e:
    print("Exception when calling TagsApi->transactions_transaction_id_relationships_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_relationships_tags_post**
> transactions_transaction_id_relationships_tags_post(transaction_id, body=body)

Add tags to transaction

Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP `204` is returned on success. The associated tags, along with this request URL, are also exposed via the `tags` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | The unique identifier for the transaction. 
body = swagger_client.UpdateTransactionTagsRequest() # UpdateTransactionTagsRequest |  (optional)

try:
    # Add tags to transaction
    api_instance.transactions_transaction_id_relationships_tags_post(transaction_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->transactions_transaction_id_relationships_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 
 **body** | [**UpdateTransactionTagsRequest**](UpdateTransactionTagsRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

