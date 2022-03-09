# swagger_client.TransactionsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_account_id_transactions_get**](TransactionsApi.md#accounts_account_id_transactions_get) | **GET** /accounts/{accountId}/transactions | List transactions by account
[**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | List transactions
[**transactions_id_get**](TransactionsApi.md#transactions_id_get) | **GET** /transactions/{id} | Retrieve transaction

# **accounts_account_id_transactions_get**
> ListTransactionsResponse accounts_account_id_transactions_get(account_id, page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)

List transactions by account

Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | The unique identifier for the account. 
page_size = 56 # int | The number of records to return in each page.  (optional)
filter_status = swagger_client.TransactionStatusEnum() # TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`.  (optional)
filter_since = '2013-10-20T19:20:30+01:00' # datetime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
filter_until = '2013-10-20T19:20:30+01:00' # datetime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
filter_category = 'filter_category_example' # str | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response.  (optional)
filter_tag = 'filter_tag_example' # str | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  (optional)

try:
    # List transactions by account
    api_response = api_instance.accounts_account_id_transactions_get(account_id, page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->accounts_account_id_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The unique identifier for the account.  | 
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_status** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filter_since** | **datetime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_until** | **datetime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_category** | **str**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filter_tag** | **str**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> ListTransactionsResponse transactions_get(page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)

List transactions

Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. To narrow the results to a specific date range pass one or both of `filter[since]` and `filter[until]` in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The number of records to return in each page.  (optional)
filter_status = swagger_client.TransactionStatusEnum() # TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`.  (optional)
filter_since = '2013-10-20T19:20:30+01:00' # datetime | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
filter_until = '2013-10-20T19:20:30+01:00' # datetime | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  (optional)
filter_category = 'filter_category_example' # str | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response.  (optional)
filter_tag = 'filter_tag_example' # str | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  (optional)

try:
    # List transactions
    api_response = api_instance.transactions_get(page_size=page_size, filter_status=filter_status, filter_since=filter_since, filter_until=filter_until, filter_category=filter_category, filter_tag=filter_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_status** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filter_since** | **datetime**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_until** | **datetime**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filter_category** | **str**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filter_tag** | **str**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_id_get**
> GetTransactionResponse transactions_id_get(id)

Retrieve transaction

Retrieve a specific transaction by providing its unique identifier. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the transaction. 

try:
    # Retrieve transaction
    api_response = api_instance.transactions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the transaction.  | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

