# swagger_client.AccountsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /accounts | List accounts
[**accounts_id_get**](AccountsApi.md#accounts_id_get) | **GET** /accounts/{id} | Retrieve account

# **accounts_get**
> ListAccountsResponse accounts_get(page_size=page_size, filter_account_type=filter_account_type, filter_ownership_type=filter_ownership_type)

List accounts

Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the `prev` and `next` links where present. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The number of records to return in each page.  (optional)
filter_account_type = swagger_client.AccountTypeEnum() # AccountTypeEnum | The type of account for which to return records. This can be used to filter Savers from spending accounts.  (optional)
filter_ownership_type = swagger_client.OwnershipTypeEnum() # OwnershipTypeEnum | The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  (optional)

try:
    # List accounts
    api_response = api_instance.accounts_get(page_size=page_size, filter_account_type=filter_account_type, filter_ownership_type=filter_ownership_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 
 **filter_account_type** | [**AccountTypeEnum**](.md)| The type of account for which to return records. This can be used to filter Savers from spending accounts.  | [optional] 
 **filter_ownership_type** | [**OwnershipTypeEnum**](.md)| The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts.  | [optional] 

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_id_get**
> GetAccountResponse accounts_id_get(id)

Retrieve account

Retrieve a specific account by providing its unique identifier. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the account. 

try:
    # Retrieve account
    api_response = api_instance.accounts_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the account.  | 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

