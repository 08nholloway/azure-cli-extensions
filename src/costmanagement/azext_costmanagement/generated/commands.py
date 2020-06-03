# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

# from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):
    pass

#     from azext_costmanagement.generated._client_factory import cf_view
#     costmanagement_view = CliCommandType(
#         operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._view_operations#ViewOperations.{'
#         '}',
#         client_factory=cf_view)
#     with self.command_group('costmanagement view', costmanagement_view, client_factory=cf_view,
#                             is_experimental=True) as g:
#         g.custom_command('list', 'costmanagement_view_list')
#         g.custom_show_command('show', 'costmanagement_view_show')
#         g.custom_command('create', 'costmanagement_view_create')
#         g.custom_command('delete', 'costmanagement_view_delete')

#     from azext_costmanagement.generated._client_factory import cf_alert
#     costmanagement_alert = CliCommandType(
#         operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._alert_operations#AlertOperations'
#         '.{}',
#         client_factory=cf_alert)
#     with self.command_group('costmanagement alert', costmanagement_alert, client_factory=cf_alert,
#                             is_experimental=True) as g:
#         g.custom_command('list', 'costmanagement_alert_list')
#         g.custom_command('list-external', 'costmanagement_alert_list_external')

#     from azext_costmanagement.generated._client_factory import cf_forecast
#     costmanagement_forecast = CliCommandType(
#         operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._forecast_operations#ForecastOper'
#         'ations.{}',
#         client_factory=cf_forecast)
#     with self.command_group('costmanagement forecast', costmanagement_forecast, client_factory=cf_forecast,
#                             is_experimental=True) as g:
#         g.custom_command('external-cloud-provider-usage', 'costmanagement_forecast_external_cloud_provider_usage')
#         g.custom_command('usage', 'costmanagement_forecast_usage')

#     from azext_costmanagement.generated._client_factory import cf_dimension
#     costmanagement_dimension = CliCommandType(
#         operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._dimension_operations#DimensionOp'
#         'erations.{}',
#         client_factory=cf_dimension)
#     with self.command_group('costmanagement dimension', costmanagement_dimension, client_factory=cf_dimension,
#                             is_experimental=True) as g:
#         g.custom_command('list', 'costmanagement_dimension_list')
#         g.custom_command('by-external-cloud-provider-type',
#                          'costmanagement_dimension_by_external_cloud_provider_type')

#     from azext_costmanagement.generated._client_factory import cf_query
#     costmanagement_query = CliCommandType(
#         operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._query_operations#QueryOperations'
#         '.{}',
#         client_factory=cf_query)
#     with self.command_group('costmanagement query', costmanagement_query, client_factory=cf_query,
#                             is_experimental=True) as g:
#         g.custom_command('usage', 'costmanagement_query_usage')
#         g.custom_command('usage-by-external-cloud-provider-type', 'costmanagement_query_usage_by_external_cloud_provide'
#                          'r_type')

    # from azext_costmanagement.generated._client_factory import cf_export
    # costmanagement_export = CliCommandType(
    #     operations_tmpl='azext_costmanagement.vendored_sdks.costmanagement.operations._export_operations#ExportOperatio'
    #     'ns.{}',
    #     client_factory=cf_export)
    # with self.command_group('costmanagement export', costmanagement_export, client_factory=cf_export,
    #                         is_experimental=True) as g:
    #     g.custom_command('list', 'costmanagement_export_list')
    #     g.custom_show_command('show', 'costmanagement_export_show')
    #     g.custom_command('create', 'costmanagement_export_create')
    #     g.custom_command('update', 'costmanagement_export_update')
    #     g.custom_command('delete', 'costmanagement_export_delete')
    #     g.custom_command('execute', 'costmanagement_export_execute')