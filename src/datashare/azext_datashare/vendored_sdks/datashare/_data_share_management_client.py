# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import DataShareManagementClientConfiguration
from .operations import AccountOperations
from .operations import ConsumerInvitationOperations
from .operations import DataSetOperations
from .operations import DataSetMappingOperations
from .operations import InvitationOperations
from .operations import OperationOperations
from .operations import ShareOperations
from .operations import ProviderShareSubscriptionOperations
from .operations import ShareSubscriptionOperations
from .operations import ConsumerSourceDataSetOperations
from .operations import SynchronizationSettingOperations
from .operations import TriggerOperations
from . import models


class DataShareManagementClient(object):
    """Creates a Microsoft.DataShare management client.

    :ivar account: AccountOperations operations
    :vartype account: azure.mgmt.datashare.operations.AccountOperations
    :ivar consumer_invitation: ConsumerInvitationOperations operations
    :vartype consumer_invitation: azure.mgmt.datashare.operations.ConsumerInvitationOperations
    :ivar data_set: DataSetOperations operations
    :vartype data_set: azure.mgmt.datashare.operations.DataSetOperations
    :ivar data_set_mapping: DataSetMappingOperations operations
    :vartype data_set_mapping: azure.mgmt.datashare.operations.DataSetMappingOperations
    :ivar invitation: InvitationOperations operations
    :vartype invitation: azure.mgmt.datashare.operations.InvitationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.datashare.operations.OperationOperations
    :ivar share: ShareOperations operations
    :vartype share: azure.mgmt.datashare.operations.ShareOperations
    :ivar provider_share_subscription: ProviderShareSubscriptionOperations operations
    :vartype provider_share_subscription: azure.mgmt.datashare.operations.ProviderShareSubscriptionOperations
    :ivar share_subscription: ShareSubscriptionOperations operations
    :vartype share_subscription: azure.mgmt.datashare.operations.ShareSubscriptionOperations
    :ivar consumer_source_data_set: ConsumerSourceDataSetOperations operations
    :vartype consumer_source_data_set: azure.mgmt.datashare.operations.ConsumerSourceDataSetOperations
    :ivar synchronization_setting: SynchronizationSettingOperations operations
    :vartype synchronization_setting: azure.mgmt.datashare.operations.SynchronizationSettingOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: azure.mgmt.datashare.operations.TriggerOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataShareManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.account = AccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_invitation = ConsumerInvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_set = DataSetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_set_mapping = DataSetMappingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitation = InvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider_share_subscription = ProviderShareSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_subscription = ShareSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_source_data_set = ConsumerSourceDataSetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.synchronization_setting = SynchronizationSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataShareManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
