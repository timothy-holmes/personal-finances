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

class AccountResourceAttributes(object):
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
        'display_name': 'str',
        'account_type': 'AllOfAccountResourceAttributesAccountType',
        'ownership_type': 'AllOfAccountResourceAttributesOwnershipType',
        'balance': 'AllOfAccountResourceAttributesBalance',
        'created_at': 'datetime'
    }

    attribute_map = {
        'display_name': 'displayName',
        'account_type': 'accountType',
        'ownership_type': 'ownershipType',
        'balance': 'balance',
        'created_at': 'createdAt'
    }

    def __init__(self, display_name=None, account_type=None, ownership_type=None, balance=None, created_at=None):  # noqa: E501
        """AccountResourceAttributes - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._account_type = None
        self._ownership_type = None
        self._balance = None
        self._created_at = None
        self.discriminator = None
        self.display_name = display_name
        self.account_type = account_type
        self.ownership_type = ownership_type
        self.balance = balance
        self.created_at = created_at

    @property
    def display_name(self):
        """Gets the display_name of this AccountResourceAttributes.  # noqa: E501

        The name associated with the account in the Up application.   # noqa: E501

        :return: The display_name of this AccountResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AccountResourceAttributes.

        The name associated with the account in the Up application.   # noqa: E501

        :param display_name: The display_name of this AccountResourceAttributes.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def account_type(self):
        """Gets the account_type of this AccountResourceAttributes.  # noqa: E501

        The bank account type of this account.   # noqa: E501

        :return: The account_type of this AccountResourceAttributes.  # noqa: E501
        :rtype: AllOfAccountResourceAttributesAccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountResourceAttributes.

        The bank account type of this account.   # noqa: E501

        :param account_type: The account_type of this AccountResourceAttributes.  # noqa: E501
        :type: AllOfAccountResourceAttributesAccountType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def ownership_type(self):
        """Gets the ownership_type of this AccountResourceAttributes.  # noqa: E501

        The ownership structure for this account.   # noqa: E501

        :return: The ownership_type of this AccountResourceAttributes.  # noqa: E501
        :rtype: AllOfAccountResourceAttributesOwnershipType
        """
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, ownership_type):
        """Sets the ownership_type of this AccountResourceAttributes.

        The ownership structure for this account.   # noqa: E501

        :param ownership_type: The ownership_type of this AccountResourceAttributes.  # noqa: E501
        :type: AllOfAccountResourceAttributesOwnershipType
        """
        if ownership_type is None:
            raise ValueError("Invalid value for `ownership_type`, must not be `None`")  # noqa: E501

        self._ownership_type = ownership_type

    @property
    def balance(self):
        """Gets the balance of this AccountResourceAttributes.  # noqa: E501

        The available balance of the account, taking into account any amounts that are currently on hold.   # noqa: E501

        :return: The balance of this AccountResourceAttributes.  # noqa: E501
        :rtype: AllOfAccountResourceAttributesBalance
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountResourceAttributes.

        The available balance of the account, taking into account any amounts that are currently on hold.   # noqa: E501

        :param balance: The balance of this AccountResourceAttributes.  # noqa: E501
        :type: AllOfAccountResourceAttributesBalance
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def created_at(self):
        """Gets the created_at of this AccountResourceAttributes.  # noqa: E501

        The date-time at which this account was first opened.   # noqa: E501

        :return: The created_at of this AccountResourceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountResourceAttributes.

        The date-time at which this account was first opened.   # noqa: E501

        :param created_at: The created_at of this AccountResourceAttributes.  # noqa: E501
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
        if issubclass(AccountResourceAttributes, dict):
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
        if not isinstance(other, AccountResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
