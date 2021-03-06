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

class CategoryResource(object):
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
        'attributes': 'CategoryResourceAttributes',
        'relationships': 'CategoryResourceRelationships',
        'links': 'AccountResourceLinks'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'attributes': 'attributes',
        'relationships': 'relationships',
        'links': 'links'
    }

    def __init__(self, type=None, id=None, attributes=None, relationships=None, links=None):  # noqa: E501
        """CategoryResource - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._attributes = None
        self._relationships = None
        self._links = None
        self.discriminator = None
        self.type = type
        self.id = id
        self.attributes = attributes
        self.relationships = relationships
        if links is not None:
            self.links = links

    @property
    def type(self):
        """Gets the type of this CategoryResource.  # noqa: E501

        The type of this resource: `categories`  # noqa: E501

        :return: The type of this CategoryResource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CategoryResource.

        The type of this resource: `categories`  # noqa: E501

        :param type: The type of this CategoryResource.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this CategoryResource.  # noqa: E501

        The unique identifier for this category. This is a human-readable but URL-safe value.   # noqa: E501

        :return: The id of this CategoryResource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CategoryResource.

        The unique identifier for this category. This is a human-readable but URL-safe value.   # noqa: E501

        :param id: The id of this CategoryResource.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def attributes(self):
        """Gets the attributes of this CategoryResource.  # noqa: E501


        :return: The attributes of this CategoryResource.  # noqa: E501
        :rtype: CategoryResourceAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CategoryResource.


        :param attributes: The attributes of this CategoryResource.  # noqa: E501
        :type: CategoryResourceAttributes
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def relationships(self):
        """Gets the relationships of this CategoryResource.  # noqa: E501


        :return: The relationships of this CategoryResource.  # noqa: E501
        :rtype: CategoryResourceRelationships
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this CategoryResource.


        :param relationships: The relationships of this CategoryResource.  # noqa: E501
        :type: CategoryResourceRelationships
        """
        if relationships is None:
            raise ValueError("Invalid value for `relationships`, must not be `None`")  # noqa: E501

        self._relationships = relationships

    @property
    def links(self):
        """Gets the links of this CategoryResource.  # noqa: E501


        :return: The links of this CategoryResource.  # noqa: E501
        :rtype: AccountResourceLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CategoryResource.


        :param links: The links of this CategoryResource.  # noqa: E501
        :type: AccountResourceLinks
        """

        self._links = links

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
        if issubclass(CategoryResource, dict):
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
        if not isinstance(other, CategoryResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
