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

class TransactionResourceRelationshipsCategoryLinks(object):
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
        '_self': 'str',
        'related': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'related': 'related'
    }

    def __init__(self, _self=None, related=None):  # noqa: E501
        """TransactionResourceRelationshipsCategoryLinks - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._related = None
        self.discriminator = None
        self._self = _self
        if related is not None:
            self.related = related

    @property
    def _self(self):
        """Gets the _self of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501

        The link to retrieve or modify linkage between this resources and the related resource(s) in this relationship.   # noqa: E501

        :return: The _self of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this TransactionResourceRelationshipsCategoryLinks.

        The link to retrieve or modify linkage between this resources and the related resource(s) in this relationship.   # noqa: E501

        :param _self: The _self of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501
        :type: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def related(self):
        """Gets the related of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501

        The link to retrieve the related resource(s) in this relationship.   # noqa: E501

        :return: The related of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501
        :rtype: str
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this TransactionResourceRelationshipsCategoryLinks.

        The link to retrieve the related resource(s) in this relationship.   # noqa: E501

        :param related: The related of this TransactionResourceRelationshipsCategoryLinks.  # noqa: E501
        :type: str
        """

        self._related = related

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
        if issubclass(TransactionResourceRelationshipsCategoryLinks, dict):
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
        if not isinstance(other, TransactionResourceRelationshipsCategoryLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
