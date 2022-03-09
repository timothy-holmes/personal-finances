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

class PingResponseMeta(object):
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
        'id': 'str',
        'status_emoji': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status_emoji': 'statusEmoji'
    }

    def __init__(self, id=None, status_emoji=None):  # noqa: E501
        """PingResponseMeta - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status_emoji = None
        self.discriminator = None
        self.id = id
        self.status_emoji = status_emoji

    @property
    def id(self):
        """Gets the id of this PingResponseMeta.  # noqa: E501

        The unique identifier of the authenticated customer.   # noqa: E501

        :return: The id of this PingResponseMeta.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PingResponseMeta.

        The unique identifier of the authenticated customer.   # noqa: E501

        :param id: The id of this PingResponseMeta.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status_emoji(self):
        """Gets the status_emoji of this PingResponseMeta.  # noqa: E501

        A cute emoji that represents the response status.   # noqa: E501

        :return: The status_emoji of this PingResponseMeta.  # noqa: E501
        :rtype: str
        """
        return self._status_emoji

    @status_emoji.setter
    def status_emoji(self, status_emoji):
        """Sets the status_emoji of this PingResponseMeta.

        A cute emoji that represents the response status.   # noqa: E501

        :param status_emoji: The status_emoji of this PingResponseMeta.  # noqa: E501
        :type: str
        """
        if status_emoji is None:
            raise ValueError("Invalid value for `status_emoji`, must not be `None`")  # noqa: E501

        self._status_emoji = status_emoji

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
        if issubclass(PingResponseMeta, dict):
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
        if not isinstance(other, PingResponseMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other