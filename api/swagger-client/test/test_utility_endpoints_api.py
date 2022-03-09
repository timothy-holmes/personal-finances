# coding: utf-8

"""
    Up API

    The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.utility_endpoints_api import UtilityEndpointsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUtilityEndpointsApi(unittest.TestCase):
    """UtilityEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = UtilityEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_util_ping_get(self):
        """Test case for util_ping_get

        Ping  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
