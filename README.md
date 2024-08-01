# Upstox Python SDK for API v2

[![PyPI](https://img.shields.io/pypi/v/upstox-python-sdk?label=upstox-python-sdk)](https://pypi.python.org/pypi/upstox-python-sdk)

## Introduction

The official Python client for communicating with the <a href="https://upstox.com/uplink/">Upstox API</a>.

Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection. 

- API version: v2
- Package version: 2.4.4
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project.

## Documentation.

<a href="https://upstox.com/developer/api-documentation">Upstox API Documentation</a>

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install upstox-python-sdk
```
(you may need to run `pip` with root permission: `sudo pip install upstox-python-sdk`)

Then import the package:
```python
import upstox_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import upstox_client
```

## Examples

[Sample Implementations](examples/) can be found within `/examples` folder.

- [Websocket Market data](examples/websocket/market_data/)
- [Websocket Order updates](examples/websocket/order_updates/)

## Documentation for API Endpoints

All URIs are relative to *https://api.upstox.com/v2/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChargeApi* | [**get_brokerage**](docs/ChargeApi.md#get_brokerage) | **GET** /v2/charges/brokerage | Brokerage details
*HistoryApi* | [**get_historical_candle_data**](docs/HistoryApi.md#get_historical_candle_data) | **GET** /v2/historical-candle/{instrumentKey}/{interval}/{to_date} | Historical candle data
*HistoryApi* | [**get_historical_candle_data1**](docs/HistoryApi.md#get_historical_candle_data1) | **GET** /v2/historical-candle/{instrumentKey}/{interval}/{to_date}/{from_date} | Historical candle data
*HistoryApi* | [**get_intra_day_candle_data**](docs/HistoryApi.md#get_intra_day_candle_data) | **GET** /v2/historical-candle/intraday/{instrumentKey}/{interval} | Intra day candle data
*LoginApi* | [**authorize**](docs/LoginApi.md#authorize) | **GET** /v2/login/authorization/dialog | Authorize API
*LoginApi* | [**logout**](docs/LoginApi.md#logout) | **DELETE** /v2/logout | Logout
*LoginApi* | [**token**](docs/LoginApi.md#token) | **POST** /v2/login/authorization/token | Get token API
*MarketHolidaysAndTimingsApi* | [**get_exchange_timings**](docs/MarketHolidaysAndTimingsApi.md#get_exchange_timings) | **GET** /v2/market/timings/{date} | Get Exchange Timings on particular date
*MarketHolidaysAndTimingsApi* | [**get_holiday**](docs/MarketHolidaysAndTimingsApi.md#get_holiday) | **GET** /v2/market/holidays/{date} | Get Holiday on particular date
*MarketHolidaysAndTimingsApi* | [**get_holidays**](docs/MarketHolidaysAndTimingsApi.md#get_holidays) | **GET** /v2/market/holidays | Get Holiday list of current year
*MarketHolidaysAndTimingsApi* | [**get_market_status**](docs/MarketHolidaysAndTimingsApi.md#get_market_status) | **GET** /v2/market/status/{exchange} | Get Market status for particular exchange
*MarketQuoteApi* | [**get_full_market_quote**](docs/MarketQuoteApi.md#get_full_market_quote) | **GET** /v2/market-quote/quotes | Market quotes and instruments - Full market quotes
*MarketQuoteApi* | [**get_market_quote_ohlc**](docs/MarketQuoteApi.md#get_market_quote_ohlc) | **GET** /v2/market-quote/ohlc | Market quotes and instruments - OHLC quotes
*MarketQuoteApi* | [**ltp**](docs/MarketQuoteApi.md#ltp) | **GET** /v2/market-quote/ltp | Market quotes and instruments - LTP quotes.
*OptionsApi* | [**get_option_contracts**](docs/OptionsApi.md#get_option_contracts) | **GET** /v2/option/contract | Get option contracts
*OptionsApi* | [**get_put_call_option_chain**](docs/OptionsApi.md#get_put_call_option_chain) | **GET** /v2/option/chain | Get option chain
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | **DELETE** /v2/order/cancel | Cancel order
*OrderApi* | [**get_order_book**](docs/OrderApi.md#get_order_book) | **GET** /v2/order/retrieve-all | Get order book
*OrderApi* | [**get_order_details**](docs/OrderApi.md#get_order_details) | **GET** /v2/order/history | Get order history
*OrderApi* | [**get_trade_history**](docs/OrderApi.md#get_trade_history) | **GET** /v2/order/trades/get-trades-for-day | Get trades
*OrderApi* | [**get_trades_by_order**](docs/OrderApi.md#get_trades_by_order) | **GET** /v2/order/trades | Get trades for order
*OrderApi* | [**modify_order**](docs/OrderApi.md#modify_order) | **PUT** /v2/order/modify | Modify order
*OrderApi* | [**place_order**](docs/OrderApi.md#place_order) | **POST** /v2/order/place | Place order
*PortfolioApi* | [**convert_positions**](docs/PortfolioApi.md#convert_positions) | **PUT** /v2/portfolio/convert-position | Convert Positions
*PortfolioApi* | [**get_holdings**](docs/PortfolioApi.md#get_holdings) | **GET** /v2/portfolio/long-term-holdings | Get Holdings
*PortfolioApi* | [**get_positions**](docs/PortfolioApi.md#get_positions) | **GET** /v2/portfolio/short-term-positions | Get Positions
*TradeProfitAndLossApi* | [**get_profit_and_loss_charges**](docs/TradeProfitAndLossApi.md#get_profit_and_loss_charges) | **GET** /v2/trade/profit-loss/charges | Get profit and loss on trades
*TradeProfitAndLossApi* | [**get_trade_wise_profit_and_loss_data**](docs/TradeProfitAndLossApi.md#get_trade_wise_profit_and_loss_data) | **GET** /v2/trade/profit-loss/data | Get Trade-wise Profit and Loss Report Data
*TradeProfitAndLossApi* | [**get_trade_wise_profit_and_loss_meta_data**](docs/TradeProfitAndLossApi.md#get_trade_wise_profit_and_loss_meta_data) | **GET** /v2/trade/profit-loss/metadata | Get profit and loss meta data on trades
*UserApi* | [**get_profile**](docs/UserApi.md#get_profile) | **GET** /v2/user/profile | Get profile
*UserApi* | [**get_user_fund_margin**](docs/UserApi.md#get_user_fund_margin) | **GET** /v2/user/get-funds-and-margin | Get User Fund And Margin
*WebsocketApi* | [**get_market_data_feed**](docs/WebsocketApi.md#get_market_data_feed) | **GET** /v2/feed/market-data-feed | Market Data Feed
*WebsocketApi* | [**get_market_data_feed_authorize**](docs/WebsocketApi.md#get_market_data_feed_authorize) | **GET** /v2/feed/market-data-feed/authorize | Market Data Feed Authorize
*WebsocketApi* | [**get_portfolio_stream_feed**](docs/WebsocketApi.md#get_portfolio_stream_feed) | **GET** /v2/feed/portfolio-stream-feed | Portfolio Stream Feed
*WebsocketApi* | [**get_portfolio_stream_feed_authorize**](docs/WebsocketApi.md#get_portfolio_stream_feed_authorize) | **GET** /v2/feed/portfolio-stream-feed/authorize | Portfolio Stream Feed Authorize

## Documentation for Feeder Functions

Connecting to the WebSocket for market and portfolio updates is streamlined through two primary Feeder functions:

1. **MarketDataStreamer**: Offers real-time market updates, providing a seamless way to receive instantaneous information on various market instruments.
2. **PortfolioDataStreamer**: Delivers updates related to the user's orders, enhancing the ability to track order status and portfolio changes effectively.

Both functions are designed to simplify the process of subscribing to essential data streams, ensuring users have quick and easy access to the information they need.

### Detailed Explanation of Feeder Interface

### MarketDataStreamer

The `MarketDataStreamer` interface is designed for effortless connection to the market WebSocket, enabling users to receive instantaneous updates on various instruments. The following example demonstrates how to quickly set up and start receiving market updates for selected instrument keys:

```python
import upstox_client

def on_message(message):
    print(message)


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration), ["NSE_INDEX|Nifty 50", "NSE_INDEX|Nifty Bank"], "full")

    streamer.on("message", on_message)

    streamer.connect()


if __name__ == "__main__":
    main()
```

In this example, you first authenticate using an access token, then instantiate MarketDataStreamer with specific instrument keys and a subscription mode. Upon connecting, the streamer listens for market updates, which are logged to the console as they arrive.

Feel free to adjust the access token placeholder and any other specifics to better fit your actual implementation or usage scenario.

### Exploring the MarketDataStreamer Functionality

#### Modes
- **ltpc**: ltpc provides information solely about the most recent trade, encompassing details such as the last trade price, time of the last trade, quantity traded, and the closing price from the previous day.
- **full**: The full option offers comprehensive information, including the latest trade prices, D5 depth, 1-minute, 30-minute, and daily candlestick data, along with some additional details.

#### Functions
1. **constructor MarketDataStreamer(apiClient, instrumentKeys, mode)**: Initializes the streamer with optional instrument keys and mode (`full` or `ltpc`).
2. **connect()**: Establishes the WebSocket connection.
3. **subscribe(instrumentKeys, mode)**: Subscribes to updates for given instrument keys in the specified mode. Both parameters are mandatory.
4. **unsubscribe(instrumentKeys)**: Stops updates for the specified instrument keys.
5. **changeMode(instrumentKeys, mode)**: Switches the mode for already subscribed instrument keys.
6. **disconnect()**: Ends the active WebSocket connection.
7. **auto_reconnect(enable, interval, retryCount)**: Customizes auto-reconnect functionality. Parameters include a flag to enable/disable it, the interval(in seconds) between attempts, and the maximum number of retries.

#### Events
- **open**: Emitted upon successful connection establishment.
- **close**: Indicates the WebSocket connection has been closed.
- **message**: Delivers market updates.
- **error**: Signals an error has occurred.
- **reconnecting**: Announced when a reconnect attempt is initiated.
- **autoReconnectStopped**: Informs when auto-reconnect efforts have ceased after exhausting the retry count.

The following documentation includes examples to illustrate the usage of these functions and events, providing a practical understanding of how to interact with the MarketDataStreamer effectively.

<br/>

1. Subscribing to Market Data on Connection Open with MarketDataStreamer

```python
import upstox_client

def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    def on_open():
        streamer.subscribe(
            ["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"], "full")

    def on_message(message):
        print(message)

    streamer.on("open", on_open)
    streamer.on("message", on_message)

    streamer.connect()

if __name__ == "__main__":
    main()
```

<br/>

2. Subscribing to Instruments with Delays

```python
import upstox_client
import time


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    def on_open():
        streamer.subscribe(
            ["NSE_EQ|INE020B01018"], "full")

    # Handle incoming market data messages\
    def on_message(message):
        print(message)

    streamer.on("open", on_open)
    streamer.on("message", on_message)

    streamer.connect()

    time.sleep(5)
    streamer.subscribe(
        ["NSE_EQ|INE467B01029"], "full")


if __name__ == "__main__":
    main()

```

<br/>

3. Subscribing and Unsubscribing to Instruments

```python
import upstox_client
import time


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    def on_open():
        print("Connected. Subscribing to instrument keys.")
        streamer.subscribe(
            ["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"], "full")

    # Handle incoming market data messages\
    def on_message(message):
        print(message)

    streamer.on("open", on_open)
    streamer.on("message", on_message)

    streamer.connect()

    time.sleep(5)
    print("Unsubscribing from instrument keys.")
    streamer.unsubscribe(["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"])


if __name__ == "__main__":
    main()
```

<br/>

4. Subscribe, Change Mode and Unsubscribe

```python
import upstox_client
import time

def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    def on_open():
        print("Connected. Subscribing to instrument keys.")
        streamer.subscribe(
            ["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"], "full")

    # Handle incoming market data messages\
    def on_message(message):
        print(message)

    streamer.on("open", on_open)
    streamer.on("message", on_message)

    streamer.connect()

    time.sleep(5)
    print("Changing subscription mode to ltpc...")
    streamer.change_mode(
        ["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"], "ltpc")

    time.sleep(5)
    print("Unsubscribing from instrument keys.")
    streamer.unsubscribe(["NSE_EQ|INE020B01018", "NSE_EQ|INE467B01029"])


if __name__ == "__main__":
    main()
```

<br/>

5. Disable Auto-Reconnect

```python
import upstox_client
import time


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    def on_reconnection_halt(message):
        print(message)

    streamer.on("autoReconnectStopped", on_reconnection_halt)

    # Disable auto-reconnect feature
    streamer.auto_reconnect(False)

    streamer.connect()


if __name__ == "__main__":
    main()
```

<br/>

6. Modify Auto-Reconnect parameters

```python
import upstox_client


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.MarketDataStreamer(
        upstox_client.ApiClient(configuration))

    # Modify auto-reconnect parameters: enable it, set interval to 10 seconds, and retry count to 3
    streamer.auto_reconnect(True, 10, 3)

    streamer.connect()


if __name__ == "__main__":
    main()
```

<br/>

### PortfolioDataStreamer

Connecting to the Portfolio WebSocket for real-time order updates is straightforward with the PortfolioDataStreamer function. Below is a concise guide to get you started on receiving updates:

```python
import upstox_client

def on_message(message):
    print(message)


def main():
    configuration = upstox_client.Configuration()
    access_token = <ACCESS_TOKEN>
    configuration.access_token = access_token

    streamer = upstox_client.PortfolioDataStreamer(
        upstox_client.ApiClient(configuration))

    streamer.on("message", on_message)

    streamer.connect()


if __name__ == "__main__":
    main()
```
<br/>

You can also enable position and holding updates by providing a boolean value to the constructor of `PortfolioDataStreamer`

```python
import upstox_client
import data_token


def on_message(message):
    print(message)


def on_open():
    print("connection opened")


def main():
    configuration = upstox_client.Configuration()
    configuration.access_token = <ACCESS_TOKEN>

    streamer = upstox_client.PortfolioDataStreamer(upstox_client.ApiClient(configuration),order_update=True,position_update=True,holding_update=True)

    streamer.on("message", on_message)
    streamer.on("open", on_open)
    streamer.connect()


if __name__ == "__main__":
    main()

```

<br/>

This example demonstrates initializing the PortfolioDataStreamer, connecting it to the WebSocket, and setting up an event listener to receive and print order updates. Replace <ACCESS_TOKEN> with your valid access token to authenticate the session.

### Exploring the PortfolioDataStreamer Functionality

#### Functions
1. **constructor PortfolioDataStreamer()**: Initializes the streamer.
2. **connect()**: Establishes the WebSocket connection.
6. **disconnect()**: Ends the active WebSocket connection.
7. **auto_reconnect(enable, interval, retryCount)**: Customizes auto-reconnect functionality. Parameters include a flag to enable/disable it, the interval(in seconds) between attempts, and the maximum number of retries.

#### Events
- **open**: Emitted upon successful connection establishment.
- **close**: Indicates the WebSocket connection has been closed.
- **message**: Delivers market updates.
- **error**: Signals an error has occurred.
- **reconnecting**: Announced when a reconnect attempt is initiated.
- **autoReconnectStopped**: Informs when auto-reconnect efforts have ceased after exhausting the retry count.

## Documentation For Models

 - [AnalyticsData](docs/AnalyticsData.md)
 - [ApiGatewayErrorResponse](docs/ApiGatewayErrorResponse.md)
 - [BrokerageData](docs/BrokerageData.md)
 - [BrokerageTaxes](docs/BrokerageTaxes.md)
 - [BrokerageWrapperData](docs/BrokerageWrapperData.md)
 - [CancelOrderData](docs/CancelOrderData.md)
 - [CancelOrderResponse](docs/CancelOrderResponse.md)
 - [ConvertPositionData](docs/ConvertPositionData.md)
 - [ConvertPositionRequest](docs/ConvertPositionRequest.md)
 - [ConvertPositionResponse](docs/ConvertPositionResponse.md)
 - [Depth](docs/Depth.md)
 - [DepthMap](docs/DepthMap.md)
 - [DpPlan](docs/DpPlan.md)
 - [ExchangeTimingData](docs/ExchangeTimingData.md)
 - [GetBrokerageResponse](docs/GetBrokerageResponse.md)
 - [GetExchangeTimingResponse](docs/GetExchangeTimingResponse.md)
 - [GetFullMarketQuoteResponse](docs/GetFullMarketQuoteResponse.md)
 - [GetHistoricalCandleResponse](docs/GetHistoricalCandleResponse.md)
 - [GetHoldingsResponse](docs/GetHoldingsResponse.md)
 - [GetHolidayResponse](docs/GetHolidayResponse.md)
 - [GetIntraDayCandleResponse](docs/GetIntraDayCandleResponse.md)
 - [GetMarketQuoteLastTradedPriceResponse](docs/GetMarketQuoteLastTradedPriceResponse.md)
 - [GetMarketQuoteOHLCResponse](docs/GetMarketQuoteOHLCResponse.md)
 - [GetMarketStatusResponse](docs/GetMarketStatusResponse.md)
 - [GetOptionChainResponse](docs/GetOptionChainResponse.md)
 - [GetOptionContractResponse](docs/GetOptionContractResponse.md)
 - [GetOrderBookResponse](docs/GetOrderBookResponse.md)
 - [GetOrderResponse](docs/GetOrderResponse.md)
 - [GetPositionResponse](docs/GetPositionResponse.md)
 - [GetProfileResponse](docs/GetProfileResponse.md)
 - [GetProfitAndLossChargesResponse](docs/GetProfitAndLossChargesResponse.md)
 - [GetTradeResponse](docs/GetTradeResponse.md)
 - [GetTradeWiseProfitAndLossDataResponse](docs/GetTradeWiseProfitAndLossDataResponse.md)
 - [GetTradeWiseProfitAndLossMetaDataResponse](docs/GetTradeWiseProfitAndLossMetaDataResponse.md)
 - [GetUserFundMarginResponse](docs/GetUserFundMarginResponse.md)
 - [HistoricalCandleData](docs/HistoricalCandleData.md)
 - [HoldingsData](docs/HoldingsData.md)
 - [HolidayData](docs/HolidayData.md)
 - [InstrumentData](docs/InstrumentData.md)
 - [IntraDayCandleData](docs/IntraDayCandleData.md)
 - [LogoutResponse](docs/LogoutResponse.md)
 - [MarketData](docs/MarketData.md)
 - [MarketQuoteOHLC](docs/MarketQuoteOHLC.md)
 - [MarketQuoteSymbol](docs/MarketQuoteSymbol.md)
 - [MarketQuoteSymbolLtp](docs/MarketQuoteSymbolLtp.md)
 - [MarketStatusData](docs/MarketStatusData.md)
 - [ModifyOrderData](docs/ModifyOrderData.md)
 - [ModifyOrderRequest](docs/ModifyOrderRequest.md)
 - [ModifyOrderResponse](docs/ModifyOrderResponse.md)
 - [OAuthClientException](docs/OAuthClientException.md)
 - [OAuthClientExceptionCause](docs/OAuthClientExceptionCause.md)
 - [OAuthClientExceptionCauseStackTrace](docs/OAuthClientExceptionCauseStackTrace.md)
 - [OAuthClientExceptionCauseSuppressed](docs/OAuthClientExceptionCauseSuppressed.md)
 - [Ohlc](docs/Ohlc.md)
 - [OptionStrikeData](docs/OptionStrikeData.md)
 - [OrderBookData](docs/OrderBookData.md)
 - [OrderData](docs/OrderData.md)
 - [OtherTaxes](docs/OtherTaxes.md)
 - [PlaceOrderData](docs/PlaceOrderData.md)
 - [PlaceOrderRequest](docs/PlaceOrderRequest.md)
 - [PlaceOrderResponse](docs/PlaceOrderResponse.md)
 - [PositionData](docs/PositionData.md)
 - [Problem](docs/Problem.md)
 - [ProfileData](docs/ProfileData.md)
 - [ProfitAndLossChargesData](docs/ProfitAndLossChargesData.md)
 - [ProfitAndLossChargesTaxes](docs/ProfitAndLossChargesTaxes.md)
 - [ProfitAndLossChargesWrapperData](docs/ProfitAndLossChargesWrapperData.md)
 - [ProfitAndLossMetaData](docs/ProfitAndLossMetaData.md)
 - [ProfitAndLossMetaDataWrapper](docs/ProfitAndLossMetaDataWrapper.md)
 - [ProfitAndLossOtherChargesTaxes](docs/ProfitAndLossOtherChargesTaxes.md)
 - [PutCallOptionChainData](docs/PutCallOptionChainData.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [TradeData](docs/TradeData.md)
 - [TradeWiseMetaData](docs/TradeWiseMetaData.md)
 - [TradeWiseProfitAndLossData](docs/TradeWiseProfitAndLossData.md)
 - [UserFundMarginData](docs/UserFundMarginData.md)
 - [WebsocketAuthRedirectResponse](docs/WebsocketAuthRedirectResponse.md)
 - [WebsocketAuthRedirectResponseData](docs/WebsocketAuthRedirectResponseData.md)
