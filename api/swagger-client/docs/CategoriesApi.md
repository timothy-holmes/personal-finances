# swagger_client.CategoriesApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_get**](CategoriesApi.md#categories_get) | **GET** /categories | List categories
[**categories_id_get**](CategoriesApi.md#categories_id_get) | **GET** /categories/{id} | Retrieve category
[**transactions_transaction_id_relationships_category_patch**](CategoriesApi.md#transactions_transaction_id_relationships_category_patch) | **PATCH** /transactions/{transactionId}/relationships/category | Categorize transaction

# **categories_get**
> ListCategoriesResponse categories_get(filter_parent=filter_parent)

List categories

Retrieve a list of all categories and their ancestry. The returned list is not paginated. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
filter_parent = 'filter_parent_example' # str | The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a `404` response.  (optional)

try:
    # List categories
    api_response = api_instance.categories_get(filter_parent=filter_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_parent** | **str**| The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_id_get**
> GetCategoryResponse categories_id_get(id)

Retrieve category

Retrieve a specific category by providing its unique identifier. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the category. 

try:
    # Retrieve category
    api_response = api_instance.categories_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->categories_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the category.  | 

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_transaction_id_relationships_category_patch**
> transactions_transaction_id_relationships_category_patch(transaction_id, body=body)

Categorize transaction

Updates the category associated with a transaction. Only transactions for which `isCategorizable` is set to true support this operation. The `id` is taken from the list exposed on `/categories` and cannot be one of the top-level (parent) categories. To de-categorize a transaction, set the entire `data` key to `null`. An HTTP `204` is returned on success. The associated category, along with its request URL is also exposed via the `category` relationship on the transaction resource returned from `/transactions/{id}`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | The unique identifier for the transaction. 
body = swagger_client.UpdateTransactionCategoryRequest() # UpdateTransactionCategoryRequest |  (optional)

try:
    # Categorize transaction
    api_instance.transactions_transaction_id_relationships_category_patch(transaction_id, body=body)
except ApiException as e:
    print("Exception when calling CategoriesApi->transactions_transaction_id_relationships_category_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier for the transaction.  | 
 **body** | [**UpdateTransactionCategoryRequest**](UpdateTransactionCategoryRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

