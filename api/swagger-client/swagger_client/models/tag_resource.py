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

class TagResource(object):
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
        'type': 'str',
        'id': 'str',
        'relationships': 'AccountResourceRelationships'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'relationships': 'relationships'
    }

    def __init__(self, type=None, id=None, relationships=None):  # noqa: E501
        """TagResource - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._relationships = None
        self.discriminator = None
        self.type = type
        self.id = id
        self.relationships = relationships

    @property
    def type(self):
        """Gets the type of this TagResource.  # noqa: E501

        The type of this resource: `tags`  # noqa: E501

        :return: The type of this TagResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TagResource.

        The type of this resource: `tags`  # noqa: E501

        :param type: The type of this TagResource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this TagResource.  # noqa: E501

        The label of the tag, which also acts as the tag’s unique identifier.   # noqa: E501

        :return: The id of this TagResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TagResource.

        The label of the tag, which also acts as the tag’s unique identifier.   # noqa: E501

        :param id: The id of this TagResource.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def relationships(self):
        """Gets the relationships of this TagResource.  # noqa: E501


        :return: The relationships of this TagResource.  # noqa: E501
        :rtype: AccountResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this TagResource.


        :param relationships: The relationships of this TagResource.  # noqa: E501
        :type: AccountResourceRelationships
        """
        if relationships is None:
            raise ValueError("Invalid value for `relationships`, must not be `None`")  # noqa: E501

        self._relationships = relationships

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
        if issubclass(TagResource, dict):
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
        if not isinstance(other, TagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other