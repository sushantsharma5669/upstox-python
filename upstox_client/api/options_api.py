# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from upstox_client.api_client import ApiClient


class OptionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_option_contracts(self, instrument_key, **kwargs):  # noqa: E501
        """Get option contracts  # noqa: E501

        This API provides the functionality to retrieve the option contracts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts(instrument_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_key: Instrument key for an underlying symbol (required)
        :param str expiry_date: Expiry date in format: YYYY-mm-dd
        :return: GetOptionContractResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_option_contracts_with_http_info(instrument_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_option_contracts_with_http_info(instrument_key, **kwargs)  # noqa: E501
            return data

    def get_option_contracts_with_http_info(self, instrument_key, **kwargs):  # noqa: E501
        """Get option contracts  # noqa: E501

        This API provides the functionality to retrieve the option contracts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_option_contracts_with_http_info(instrument_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_key: Instrument key for an underlying symbol (required)
        :param str expiry_date: Expiry date in format: YYYY-mm-dd
        :return: GetOptionContractResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_key', 'expiry_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_option_contracts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_key' is set
        if ('instrument_key' not in params or
                params['instrument_key'] is None):
            raise ValueError("Missing the required parameter `instrument_key` when calling `get_option_contracts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_key' in params:
            query_params.append(('instrument_key', params['instrument_key']))  # noqa: E501
        if 'expiry_date' in params:
            query_params.append(('expiry_date', params['expiry_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAUTH2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/option/contract', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOptionContractResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_put_call_option_chain(self, instrument_key, expiry_date, **kwargs):  # noqa: E501
        """Get option chain  # noqa: E501

        This API provides the functionality to retrieve the option chain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_put_call_option_chain(instrument_key, expiry_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_key: Instrument key for an underlying symbol (required)
        :param str expiry_date: Expiry date in format: YYYY-mm-dd (required)
        :return: GetOptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_put_call_option_chain_with_http_info(instrument_key, expiry_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_put_call_option_chain_with_http_info(instrument_key, expiry_date, **kwargs)  # noqa: E501
            return data

    def get_put_call_option_chain_with_http_info(self, instrument_key, expiry_date, **kwargs):  # noqa: E501
        """Get option chain  # noqa: E501

        This API provides the functionality to retrieve the option chain  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_put_call_option_chain_with_http_info(instrument_key, expiry_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instrument_key: Instrument key for an underlying symbol (required)
        :param str expiry_date: Expiry date in format: YYYY-mm-dd (required)
        :return: GetOptionChainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_key', 'expiry_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_put_call_option_chain" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_key' is set
        if ('instrument_key' not in params or
                params['instrument_key'] is None):
            raise ValueError("Missing the required parameter `instrument_key` when calling `get_put_call_option_chain`")  # noqa: E501
        # verify the required parameter 'expiry_date' is set
        if ('expiry_date' not in params or
                params['expiry_date'] is None):
            raise ValueError("Missing the required parameter `expiry_date` when calling `get_put_call_option_chain`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'instrument_key' in params:
            query_params.append(('instrument_key', params['instrument_key']))  # noqa: E501
        if 'expiry_date' in params:
            query_params.append(('expiry_date', params['expiry_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAUTH2']  # noqa: E501

        return self.api_client.call_api(
            '/v2/option/chain', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetOptionChainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)