# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WebhookDeliveryLogResourceAttributes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request': 'WebhookDeliveryLogResourceAttributesRequest',
        'response': 'WebhookDeliveryLogResourceAttributesResponse',
        'delivery_status': 'AllOfWebhookDeliveryLogResourceAttributesDeliveryStatus',
        'created_at': 'datetime'
    }

    attribute_map = {
        'request': 'request',
        'response': 'response',
        'delivery_status': 'deliveryStatus',
        'created_at': 'createdAt'
    }

    def __init__(self, request=None, response=None, delivery_status=None, created_at=None):  # noqa: E501
        """WebhookDeliveryLogResourceAttributes - a model defined in Swagger"""  # noqa: E501
        self._request = None
        self._response = None
        self._delivery_status = None
        self._created_at = None
        self.discriminator = None
        self.request = request
        self.response = response
        self.delivery_status = delivery_status
        self.created_at = created_at

    @property
    def request(self):
        """Gets the request of this WebhookDeliveryLogResourceAttributes.  # noqa: E501


        :return: The request of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :rtype: WebhookDeliveryLogResourceAttributesRequest
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this WebhookDeliveryLogResourceAttributes.


        :param request: The request of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :type: WebhookDeliveryLogResourceAttributesRequest
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def response(self):
        """Gets the response of this WebhookDeliveryLogResourceAttributes.  # noqa: E501


        :return: The response of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :rtype: WebhookDeliveryLogResourceAttributesResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this WebhookDeliveryLogResourceAttributes.


        :param response: The response of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :type: WebhookDeliveryLogResourceAttributesResponse
        """
        if response is None:
            raise ValueError("Invalid value for `response`, must not be `None`")  # noqa: E501

        self._response = response

    @property
    def delivery_status(self):
        """Gets the delivery_status of this WebhookDeliveryLogResourceAttributes.  # noqa: E501

        The success or failure status of this delivery attempt.   # noqa: E501

        :return: The delivery_status of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :rtype: AllOfWebhookDeliveryLogResourceAttributesDeliveryStatus
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this WebhookDeliveryLogResourceAttributes.

        The success or failure status of this delivery attempt.   # noqa: E501

        :param delivery_status: The delivery_status of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :type: AllOfWebhookDeliveryLogResourceAttributesDeliveryStatus
        """
        if delivery_status is None:
            raise ValueError("Invalid value for `delivery_status`, must not be `None`")  # noqa: E501

        self._delivery_status = delivery_status

    @property
    def created_at(self):
        """Gets the created_at of this WebhookDeliveryLogResourceAttributes.  # noqa: E501

        The date-time at which this log entry was created.   # noqa: E501

        :return: The created_at of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookDeliveryLogResourceAttributes.

        The date-time at which this log entry was created.   # noqa: E501

        :param created_at: The created_at of this WebhookDeliveryLogResourceAttributes.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebhookDeliveryLogResourceAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebhookDeliveryLogResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
