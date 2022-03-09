# swagger_client.WebhooksApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_get**](WebhooksApi.md#webhooks_get) | **GET** /webhooks | List webhooks
[**webhooks_id_delete**](WebhooksApi.md#webhooks_id_delete) | **DELETE** /webhooks/{id} | Delete webhook
[**webhooks_id_get**](WebhooksApi.md#webhooks_id_get) | **GET** /webhooks/{id} | Retrieve webhook
[**webhooks_post**](WebhooksApi.md#webhooks_post) | **POST** /webhooks | Create webhook
[**webhooks_webhook_id_logs_get**](WebhooksApi.md#webhooks_webhook_id_logs_get) | **GET** /webhooks/{webhookId}/logs | List webhook logs
[**webhooks_webhook_id_ping_post**](WebhooksApi.md#webhooks_webhook_id_ping_post) | **POST** /webhooks/{webhookId}/ping | Ping webhook

# **webhooks_get**
> ListWebhooksResponse webhooks_get(page_size=page_size)

List webhooks

Retrieve a list of configured webhooks. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered oldest first to newest last. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
page_size = 56 # int | The number of records to return in each page.  (optional)

try:
    # List webhooks
    api_response = api_instance.webhooks_get(page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_delete**
> webhooks_id_delete(id)

Delete webhook

Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the webhook. 

try:
    # Delete webhook
    api_instance.webhooks_id_delete(id)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the webhook.  | 

### Return type

void (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_id_get**
> GetWebhookResponse webhooks_id_get(id)

Retrieve webhook

Retrieve a specific webhook by providing its unique identifier. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the webhook. 

try:
    # Retrieve webhook
    api_response = api_instance.webhooks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the webhook.  | 

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_post**
> CreateWebhookResponse webhooks_post(body=body)

Create webhook

Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded `POST` requests. The URL must respond with a HTTP `200` status on success.  There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.  Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a `200` status. The response includes a `secretKey` attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the `secretKey` is lost, simply create a new webhook with the same URL, capture its `secretKey` and then delete the original webhook. See [Handling webhook events](#callback_post_webhookURL) for details on how to process webhook events.  It is probably a good idea to test the webhook by [sending it a `PING` event](#post_webhooks_webhookId_ping) after creating it. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWebhookRequest() # CreateWebhookRequest |  (optional)

try:
    # Create webhook
    api_response = api_instance.webhooks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | [optional] 

### Return type

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_webhook_id_logs_get**
> ListWebhookDeliveryLogsResponse webhooks_webhook_id_logs_get(webhook_id, page_size=page_size)

List webhook logs

Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is [paginated](#pagination) and can be scrolled by following the `next` and `prev` links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | The unique identifier for the webhook. 
page_size = 56 # int | The number of records to return in each page.  (optional)

try:
    # List webhook logs
    api_response = api_instance.webhooks_webhook_id_logs_get(webhook_id, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_webhook_id_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier for the webhook.  | 
 **page_size** | **int**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhookDeliveryLogsResponse**](ListWebhookDeliveryLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_webhook_id_ping_post**
> WebhookEventCallback webhooks_webhook_id_ping_post(webhook_id)

Ping webhook

Send a `PING` event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.WebhooksApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | The unique identifier for the webhook. 

try:
    # Ping webhook
    api_response = api_instance.webhooks_webhook_id_ping_post(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_webhook_id_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier for the webhook.  | 

### Return type

[**WebhookEventCallback**](WebhookEventCallback.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

