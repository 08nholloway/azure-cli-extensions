# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ProviderShareSubscriptionOperations(object):
    """ProviderShareSubscriptionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datashare.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_by_share(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        provider_share_subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProviderShareSubscription"
        """Get share subscription in a provider share.

        Get share subscription in a provider share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription.
        :type provider_share_subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderShareSubscription"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self.get_by_share.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'providerShareSubscriptionId': self._serialize.url("provider_share_subscription_id", provider_share_subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProviderShareSubscription', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_share.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}'}

    def list_by_share(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        skip_token=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProviderShareSubscriptionList"
        """List share subscriptions in a provider share.

        List of available share subscriptions to a provider share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param skip_token: Continuation Token.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscriptionList or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscriptionList
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderShareSubscriptionList"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_share.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str'),
                    'shareName': self._serialize.url("share_name", share_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skip_token is not None:
                query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ProviderShareSubscriptionList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DataShareError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_share.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions'}

    def _revoke_initial(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        provider_share_subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProviderShareSubscription"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderShareSubscription"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self._revoke_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'providerShareSubscriptionId': self._serialize.url("provider_share_subscription_id", provider_share_subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ProviderShareSubscription', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('ProviderShareSubscription', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _revoke_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke'}

    def begin_revoke(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        provider_share_subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProviderShareSubscription"
        """Revoke share subscription in a provider share.

        Revoke share subscription in a provider share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription.
        :type provider_share_subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns ProviderShareSubscription
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.datashare.models.ProviderShareSubscription]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderShareSubscription"]
        raw_result = self._revoke_initial(
            resource_group_name=resource_group_name,
            account_name=account_name,
            share_name=share_name,
            provider_share_subscription_id=provider_share_subscription_id,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('ProviderShareSubscription', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'},  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_revoke.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke'}

    def reinstate(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        share_name,  # type: str
        provider_share_subscription_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProviderShareSubscription"
        """Reinstate share subscription in a provider share.

        Reinstate share subscription in a provider share.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param account_name: The name of the share account.
        :type account_name: str
        :param share_name: The name of the share.
        :type share_name: str
        :param provider_share_subscription_id: To locate shareSubscription.
        :type provider_share_subscription_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProviderShareSubscription or the result of cls(response)
        :rtype: ~azure.mgmt.datashare.models.ProviderShareSubscription
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProviderShareSubscription"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2019-11-01"

        # Construct URL
        url = self.reinstate.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'shareName': self._serialize.url("share_name", share_name, 'str'),
            'providerShareSubscriptionId': self._serialize.url("provider_share_subscription_id", provider_share_subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DataShareError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProviderShareSubscription', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    reinstate.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/reinstate'}
