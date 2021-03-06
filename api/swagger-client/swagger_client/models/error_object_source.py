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

class ErrorObjectSource(object):
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
        'parameter': 'str',
        'pointer': 'str'
    }

    attribute_map = {
        'parameter': 'parameter',
        'pointer': 'pointer'
    }

    def __init__(self, parameter=None, pointer=None):  # noqa: E501
        """ErrorObjectSource - a model defined in Swagger"""  # noqa: E501
        self._parameter = None
        self._pointer = None
        self.discriminator = None
        if parameter is not None:
            self.parameter = parameter
        if pointer is not None:
            self.pointer = pointer

    @property
    def parameter(self):
        """Gets the parameter of this ErrorObjectSource.  # noqa: E501

        If this error relates to a query parameter, the name of the parameter.   # noqa: E501

        :return: The parameter of this ErrorObjectSource.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ErrorObjectSource.

        If this error relates to a query parameter, the name of the parameter.   # noqa: E501

        :param parameter: The parameter of this ErrorObjectSource.  # noqa: E501
        :type: str
        """

        self._parameter = parameter

    @property
    def pointer(self):
        """Gets the pointer of this ErrorObjectSource.  # noqa: E501

        If this error relates to an attribute in the request body, a rfc-6901 JSON pointer to the attribute.   # noqa: E501

        :return: The pointer of this ErrorObjectSource.  # noqa: E501
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this ErrorObjectSource.

        If this error relates to an attribute in the request body, a rfc-6901 JSON pointer to the attribute.   # noqa: E501

        :param pointer: The pointer of this ErrorObjectSource.  # noqa: E501
        :type: str
        """

        self._pointer = pointer

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
        if issubclass(ErrorObjectSource, dict):
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
        if not isinstance(other, ErrorObjectSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
