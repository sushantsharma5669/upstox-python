# coding: utf-8

"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api-v2.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import upstox_client
from upstox_client.api.websocket_api import WebsocketApi  # noqa: E501
from upstox_client.rest import ApiException


class TestWebsocketApi(unittest.TestCase):
    """WebsocketApi unit test stubs"""

    def setUp(self):
        self.api = WebsocketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_market_data_feed(self):
        """Test case for get_market_data_feed

        Market Data Feed  # noqa: E501
        """
        pass

    def test_get_market_data_feed_authorize(self):
        """Test case for get_market_data_feed_authorize

        Market Data Feed Authorize  # noqa: E501
        """
        pass

    def test_get_portfolio_stream_feed(self):
        """Test case for get_portfolio_stream_feed

        Portfolio Stream Feed  # noqa: E501
        """
        pass

    def test_get_portfolio_stream_feed_authorize(self):
        """Test case for get_portfolio_stream_feed_authorize

        Portfolio Stream Feed Authorize  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
