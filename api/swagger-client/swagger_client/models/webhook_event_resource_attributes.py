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

class WebhookEventResourceAttributes(object):
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
        'event_type': 'AllOfWebhookEventResourceAttributesEventType',
        'created_at': 'datetime'
    }

    attribute_map = {
        'event_type': 'eventType',
        'created_at': 'createdAt'
    }

    def __init__(self, event_type=None, created_at=None):  # noqa: E501
        """WebhookEventResourceAttributes - a model defined in Swagger"""  # noqa: E501
        self._event_type = None
        self._created_at = None
        self.discriminator = None
        self.event_type = event_type
        self.created_at = created_at

    @property
    def event_type(self):
        """Gets the event_type of this WebhookEventResourceAttributes.  # noqa: E501

        The type of this event. This can be used to determine what action to take in response to the event.   # noqa: E501

        :return: The event_type of this WebhookEventResourceAttributes.  # noqa: E501
        :rtype: AllOfWebhookEventResourceAttributesEventType
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this WebhookEventResourceAttributes.

        The type of this event. This can be used to determine what action to take in response to the event.   # noqa: E501

        :param event_type: The event_type of this WebhookEventResourceAttributes.  # noqa: E501
        :type: AllOfWebhookEventResourceAttributesEventType
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def created_at(self):
        """Gets the created_at of this WebhookEventResourceAttributes.  # noqa: E501

        The date-time at which this event was generated.   # noqa: E501

        :return: The created_at of this WebhookEventResourceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookEventResourceAttributes.

        The date-time at which this event was generated.   # noqa: E501

        :param created_at: The created_at of this WebhookEventResourceAttributes.  # noqa: E501
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
        if issubclass(WebhookEventResourceAttributes, dict):
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
        if not isinstance(other, WebhookEventResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other