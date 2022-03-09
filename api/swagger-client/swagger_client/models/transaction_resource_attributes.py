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

class TransactionResourceAttributes(object):
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
        'status': 'AllOfTransactionResourceAttributesStatus',
        'raw_text': 'str',
        'description': 'str',
        'message': 'str',
        'is_categorizable': 'bool',
        'hold_info': 'AllOfTransactionResourceAttributesHoldInfo',
        'round_up': 'AllOfTransactionResourceAttributesRoundUp',
        'cashback': 'AllOfTransactionResourceAttributesCashback',
        'amount': 'AllOfTransactionResourceAttributesAmount',
        'foreign_amount': 'AllOfTransactionResourceAttributesForeignAmount',
        'settled_at': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'raw_text': 'rawText',
        'description': 'description',
        'message': 'message',
        'is_categorizable': 'isCategorizable',
        'hold_info': 'holdInfo',
        'round_up': 'roundUp',
        'cashback': 'cashback',
        'amount': 'amount',
        'foreign_amount': 'foreignAmount',
        'settled_at': 'settledAt',
        'created_at': 'createdAt'
    }

    def __init__(self, status=None, raw_text=None, description=None, message=None, is_categorizable=None, hold_info=None, round_up=None, cashback=None, amount=None, foreign_amount=None, settled_at=None, created_at=None):  # noqa: E501
        """TransactionResourceAttributes - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._raw_text = None
        self._description = None
        self._message = None
        self._is_categorizable = None
        self._hold_info = None
        self._round_up = None
        self._cashback = None
        self._amount = None
        self._foreign_amount = None
        self._settled_at = None
        self._created_at = None
        self.discriminator = None
        self.status = status
        self.raw_text = raw_text
        self.description = description
        self.message = message
        self.is_categorizable = is_categorizable
        self.hold_info = hold_info
        self.round_up = round_up
        self.cashback = cashback
        self.amount = amount
        self.foreign_amount = foreign_amount
        self.settled_at = settled_at
        self.created_at = created_at

    @property
    def status(self):
        """Gets the status of this TransactionResourceAttributes.  # noqa: E501

        The current processing status of this transaction, according to whether or not this transaction has settled or is still held.   # noqa: E501

        :return: The status of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionResourceAttributes.

        The current processing status of this transaction, according to whether or not this transaction has settled or is still held.   # noqa: E501

        :param status: The status of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def raw_text(self):
        """Gets the raw_text of this TransactionResourceAttributes.  # noqa: E501

        The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases.   # noqa: E501

        :return: The raw_text of this TransactionResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this TransactionResourceAttributes.

        The original, unprocessed text of the transaction. This is often not a perfect indicator of the actual merchant, but it is useful for reconciliation purposes in some cases.   # noqa: E501

        :param raw_text: The raw_text of this TransactionResourceAttributes.  # noqa: E501
        :type: str
        """
        if raw_text is None:
            raise ValueError("Invalid value for `raw_text`, must not be `None`")  # noqa: E501

        self._raw_text = raw_text

    @property
    def description(self):
        """Gets the description of this TransactionResourceAttributes.  # noqa: E501

        A short description for this transaction. Usually the merchant name for purchases.   # noqa: E501

        :return: The description of this TransactionResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionResourceAttributes.

        A short description for this transaction. Usually the merchant name for purchases.   # noqa: E501

        :param description: The description of this TransactionResourceAttributes.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def message(self):
        """Gets the message of this TransactionResourceAttributes.  # noqa: E501

        Attached message for this transaction, such as a payment message, or a transfer note.   # noqa: E501

        :return: The message of this TransactionResourceAttributes.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TransactionResourceAttributes.

        Attached message for this transaction, such as a payment message, or a transfer note.   # noqa: E501

        :param message: The message of this TransactionResourceAttributes.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def is_categorizable(self):
        """Gets the is_categorizable of this TransactionResourceAttributes.  # noqa: E501

        Boolean flag set to true on transactions that support the use of categories.   # noqa: E501

        :return: The is_categorizable of this TransactionResourceAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._is_categorizable

    @is_categorizable.setter
    def is_categorizable(self, is_categorizable):
        """Sets the is_categorizable of this TransactionResourceAttributes.

        Boolean flag set to true on transactions that support the use of categories.   # noqa: E501

        :param is_categorizable: The is_categorizable of this TransactionResourceAttributes.  # noqa: E501
        :type: bool
        """
        if is_categorizable is None:
            raise ValueError("Invalid value for `is_categorizable`, must not be `None`")  # noqa: E501

        self._is_categorizable = is_categorizable

    @property
    def hold_info(self):
        """Gets the hold_info of this TransactionResourceAttributes.  # noqa: E501

        If this transaction is currently in the `HELD` status, or was ever in the `HELD` status, the `amount` and `foreignAmount` of the transaction while `HELD`.   # noqa: E501

        :return: The hold_info of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesHoldInfo
        """
        return self._hold_info

    @hold_info.setter
    def hold_info(self, hold_info):
        """Sets the hold_info of this TransactionResourceAttributes.

        If this transaction is currently in the `HELD` status, or was ever in the `HELD` status, the `amount` and `foreignAmount` of the transaction while `HELD`.   # noqa: E501

        :param hold_info: The hold_info of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesHoldInfo
        """
        if hold_info is None:
            raise ValueError("Invalid value for `hold_info`, must not be `None`")  # noqa: E501

        self._hold_info = hold_info

    @property
    def round_up(self):
        """Gets the round_up of this TransactionResourceAttributes.  # noqa: E501

        Details of how this transaction was rounded-up. If no Round Up was applied this field will be `null`.   # noqa: E501

        :return: The round_up of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesRoundUp
        """
        return self._round_up

    @round_up.setter
    def round_up(self, round_up):
        """Sets the round_up of this TransactionResourceAttributes.

        Details of how this transaction was rounded-up. If no Round Up was applied this field will be `null`.   # noqa: E501

        :param round_up: The round_up of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesRoundUp
        """
        if round_up is None:
            raise ValueError("Invalid value for `round_up`, must not be `None`")  # noqa: E501

        self._round_up = round_up

    @property
    def cashback(self):
        """Gets the cashback of this TransactionResourceAttributes.  # noqa: E501

        If all or part of this transaction was instantly reimbursed in the form of cashback, details of the reimbursement.   # noqa: E501

        :return: The cashback of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesCashback
        """
        return self._cashback

    @cashback.setter
    def cashback(self, cashback):
        """Sets the cashback of this TransactionResourceAttributes.

        If all or part of this transaction was instantly reimbursed in the form of cashback, details of the reimbursement.   # noqa: E501

        :param cashback: The cashback of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesCashback
        """
        if cashback is None:
            raise ValueError("Invalid value for `cashback`, must not be `None`")  # noqa: E501

        self._cashback = cashback

    @property
    def amount(self):
        """Gets the amount of this TransactionResourceAttributes.  # noqa: E501

        The amount of this transaction in Australian dollars. For transactions that were once `HELD` but are now `SETTLED`, refer to the `holdInfo` field for the original `amount` the transaction was `HELD` at.   # noqa: E501

        :return: The amount of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionResourceAttributes.

        The amount of this transaction in Australian dollars. For transactions that were once `HELD` but are now `SETTLED`, refer to the `holdInfo` field for the original `amount` the transaction was `HELD` at.   # noqa: E501

        :param amount: The amount of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def foreign_amount(self):
        """Gets the foreign_amount of this TransactionResourceAttributes.  # noqa: E501

        The foreign currency amount of this transaction. This field will be `null` for domestic transactions. The amount was converted to the AUD amount reflected in the `amount` of this transaction. Refer to the `holdInfo` field for the original `foreignAmount` the transaction was `HELD` at.   # noqa: E501

        :return: The foreign_amount of this TransactionResourceAttributes.  # noqa: E501
        :rtype: AllOfTransactionResourceAttributesForeignAmount
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """Sets the foreign_amount of this TransactionResourceAttributes.

        The foreign currency amount of this transaction. This field will be `null` for domestic transactions. The amount was converted to the AUD amount reflected in the `amount` of this transaction. Refer to the `holdInfo` field for the original `foreignAmount` the transaction was `HELD` at.   # noqa: E501

        :param foreign_amount: The foreign_amount of this TransactionResourceAttributes.  # noqa: E501
        :type: AllOfTransactionResourceAttributesForeignAmount
        """
        if foreign_amount is None:
            raise ValueError("Invalid value for `foreign_amount`, must not be `None`")  # noqa: E501

        self._foreign_amount = foreign_amount

    @property
    def settled_at(self):
        """Gets the settled_at of this TransactionResourceAttributes.  # noqa: E501

        The date-time at which this transaction settled. This field will be `null` for transactions that are currently in the `HELD` status.   # noqa: E501

        :return: The settled_at of this TransactionResourceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._settled_at

    @settled_at.setter
    def settled_at(self, settled_at):
        """Sets the settled_at of this TransactionResourceAttributes.

        The date-time at which this transaction settled. This field will be `null` for transactions that are currently in the `HELD` status.   # noqa: E501

        :param settled_at: The settled_at of this TransactionResourceAttributes.  # noqa: E501
        :type: datetime
        """
        if settled_at is None:
            raise ValueError("Invalid value for `settled_at`, must not be `None`")  # noqa: E501

        self._settled_at = settled_at

    @property
    def created_at(self):
        """Gets the created_at of this TransactionResourceAttributes.  # noqa: E501

        The date-time at which this transaction was first encountered.   # noqa: E501

        :return: The created_at of this TransactionResourceAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransactionResourceAttributes.

        The date-time at which this transaction was first encountered.   # noqa: E501

        :param created_at: The created_at of this TransactionResourceAttributes.  # noqa: E501
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
        if issubclass(TransactionResourceAttributes, dict):
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
        if not isinstance(other, TransactionResourceAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
