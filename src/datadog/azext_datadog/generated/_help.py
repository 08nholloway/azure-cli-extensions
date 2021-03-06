# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['datadog terms'] = """
    type: group
    short-summary: Manage marketplace agreements with datadog
"""

helps['datadog terms list'] = """
    type: command
    short-summary: "List datadog marketplace agreements"
    examples:
      - name: List marketplace agreements
        text: |-
               az datadog terms list
"""

helps['datadog terms create'] = """
    type: command
    short-summary: "Create Datadog marketplace agreement in the subscription."
    parameters:
      - name: --properties
        short-summary: "Represents the properties of the resource."
        long-summary: |
            Usage: --properties publisher=XX product=XX plan=XX license-text-link=XX privacy-policy-link=XX \
retrieve-datetime=XX signature=XX accepted=XX

            publisher: Publisher identifier string.
            product: Product identifier string.
            plan: Plan identifier string.
            license-text-link: Link to HTML with Microsoft and Publisher terms.
            privacy-policy-link: Link to the privacy policy of the publisher.
            retrieve-datetime: Date and time in UTC of when the terms were accepted. This is empty if Accepted is \
false.
            signature: Terms signature.
            accepted: If any version of the terms have been accepted, otherwise false.
    examples:
      - name: MarketplaceAgreements_CreateOrUpdate
        text: |-
               az datadog terms create --properties accepted=true
"""

helps['datadog terms update'] = """
    type: command
    short-summary: "Update Datadog marketplace agreement in the subscription."
    parameters:
      - name: --properties
        short-summary: "Represents the properties of the resource."
        long-summary: |
            Usage: --properties publisher=XX product=XX plan=XX license-text-link=XX privacy-policy-link=XX \
retrieve-datetime=XX signature=XX accepted=XX

            publisher: Publisher identifier string.
            product: Product identifier string.
            plan: Plan identifier string.
            license-text-link: Link to HTML with Microsoft and Publisher terms.
            privacy-policy-link: Link to the privacy policy of the publisher.
            retrieve-datetime: Date and time in UTC of when the terms were accepted. This is empty if Accepted is \
false.
            signature: Terms signature.
            accepted: If any version of the terms have been accepted, otherwise false.
"""

helps['datadog monitor'] = """
    type: group
    short-summary: Manage monitor with datadog
"""

helps['datadog monitor list'] = """
    type: command
    short-summary: "List all monitors under the specified resource group. And List all monitors under the specified \
subscription."
    examples:
      - name: Monitors_ListByResourceGroup
        text: |-
               az datadog monitor list --resource-group "myResourceGroup"
      - name: Monitors_List
        text: |-
               az datadog monitor list
"""

helps['datadog monitor show'] = """
    type: command
    short-summary: "Get the properties of a specific monitor resource."
    examples:
      - name: Monitors_Get
        text: |-
               az datadog monitor show --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor create'] = """
    type: command
    short-summary: "Create a monitor resource."
    parameters:
      - name: --datadog-organization-properties
        short-summary: "Datadog organization properties"
        long-summary: |
            Usage: --datadog-organization-properties linking-auth-code=XX linking-client-id=XX redirect-uri=XX \
api-key=XX application-key=XX enterprise-app-id=XX

            linking-auth-code: The auth code used to linking to an existing datadog organization.
            linking-client-id: The client_id from an existing in exchange for an auth token to link organization.
            redirect-uri: The redirect uri for linking.
            api-key: Api key associated to the Datadog organization.
            application-key: Application key associated to the Datadog organization.
            enterprise-app-id: The Id of the Enterprise App used for Single sign on.
      - name: --user-info
        short-summary: "User info"
        long-summary: |
            Usage: --user-info name=XX email-address=XX phone-number=XX

            name: Name of the user
            email-address: Email of the user used by Datadog for contacting them if needed
            phone-number: Phone number of the user used by Datadog for contacting them if needed
    examples:
      - name: Monitors_Create
        text: |-
               az datadog monitor create --name "myMonitor" --resource-group "myResourceGroup" --location "West US 2" \
--tags Environment="Dev" --user-info name="Alice" email-address="alice@microsoft.com" phone-number="123-456-7890" \
--type "SystemAssigned" --sku-name "payg_v2_Monthly"
      - name: Monitors creation with linking to Datadogo organization.
        text: |-
               az datadog monitor create --name "myMonitor" --resource-group "myResourceGroup" --location "West US 2" \
--datadog-organization-properties api-key=XX application-key=XX --tags Environment="Dev" --user-info name="Alice" \
email-address="alice@microsoft.com" phone-number="123-456-7890" --type "SystemAssigned" --sku-name "Linked"
"""

helps['datadog monitor update'] = """
    type: command
    short-summary: "Update a monitor resource."
    examples:
      - name: Monitors_Update
        text: |-
               az datadog monitor update --name "myMonitor" --tags Environment="Dev" --resource-group \
"myResourceGroup"
"""

helps['datadog monitor delete'] = """
    type: command
    short-summary: "Delete a monitor resource."
    examples:
      - name: Monitors_Delete
        text: |-
               az datadog monitor delete --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor get-default-key'] = """
    type: command
    short-summary: "Get the default api key."
    examples:
      - name: Monitors_GetDefaultKey
        text: |-
               az datadog monitor get-default-key --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor list-api-key'] = """
    type: command
    short-summary: "List the api keys for a given monitor resource."
    examples:
      - name: Monitors_ListApiKeys
        text: |-
               az datadog monitor list-api-key --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor list-host'] = """
    type: command
    short-summary: "List the hosts for a given monitor resource."
    examples:
      - name: Monitors_ListHosts
        text: |-
               az datadog monitor list-host --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor list-linked-resource'] = """
    type: command
    short-summary: "List all Azure resources associated to the same Datadog organization as the target resource."
    examples:
      - name: Monitors_ListLinkedResources
        text: |-
               az datadog monitor list-linked-resource --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor list-monitored-resource'] = """
    type: command
    short-summary: "List the resources currently being monitored by the Datadog monitor resource."
    examples:
      - name: Monitors_ListMonitoredResources
        text: |-
               az datadog monitor list-monitored-resource --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor refresh-set-password-link'] = """
    type: command
    short-summary: "Refresh the set password link and return a latest one."
    examples:
      - name: Monitors_RefreshSetPasswordLink
        text: |-
               az datadog monitor refresh-set-password-link --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog monitor set-default-key'] = """
    type: command
    short-summary: "Set the default api key."
    examples:
      - name: Monitors_SetDefaultKey
        text: |-
               az datadog monitor set-default-key --monitor-name "myMonitor" --key "1111111111111111aaaaaaaaaaaaaaaa" \
--resource-group "myResourceGroup"
"""

helps['datadog monitor wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datadog monitor is met.
    examples:
      - name: Pause executing next line of CLI script until the datadog monitor is successfully created.
        text: |-
               az datadog monitor wait --name "myMonitor" --resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the datadog monitor is successfully deleted.
        text: |-
               az datadog monitor wait --name "myMonitor" --resource-group "myResourceGroup" --deleted
"""

helps['datadog tag-rule'] = """
    type: group
    short-summary: Manage tag rule with datadog
"""

helps['datadog tag-rule list'] = """
    type: command
    short-summary: "List the tag rules for a given monitor resource."
    examples:
      - name: TagRules_List
        text: |-
               az datadog tag-rule list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog tag-rule show'] = """
    type: command
    short-summary: "Get a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Get
        text: |-
               az datadog tag-rule show --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default"
"""

helps['datadog tag-rule create'] = """
    type: command
    short-summary: "Create a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing metrics. If empty, all resources will be \
captured. If only Exclude action is specified, the rules will apply to the list of all available resources. If Include \
actions are specified, the rules will only include resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
      - name: --log-rules-filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendResourceLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --log-rules-filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --log-rules-filtering-tags argument.
    examples:
      - name: TagRules_CreateOrUpdate
        text: |-
               az datadog tag-rule create --monitor-name "myMonitor" --log-rules-filtering-tags name="Environment" \
action="Include" value="Prod" --log-rules-filtering-tags name="Environment" action="Exclude" value="Dev" \
--send-aad-logs false --send-resource-logs true --send-subscription-logs true --resource-group "myResourceGroup" \
--rule-set-name "default"
"""

helps['datadog tag-rule update'] = """
    type: command
    short-summary: "Update a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing metrics. If empty, all resources will be \
captured. If only Exclude action is specified, the rules will apply to the list of all available resources. If Include \
actions are specified, the rules will only include resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
      - name: --log-rules-filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendResourceLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --log-rules-filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --log-rules-filtering-tags argument.
"""

helps['datadog sso-config'] = """
    type: group
    short-summary: Manage sso config with datadog
"""

helps['datadog sso-config list'] = """
    type: command
    short-summary: "List the single sign-on configurations for a given monitor resource."
    examples:
      - name: SingleSignOnConfigurations_List
        text: |-
               az datadog sso-config list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['datadog sso-config show'] = """
    type: command
    short-summary: "Gets the datadog single sign-on resource for the given Monitor."
    examples:
      - name: SingleSignOnConfigurations_Get
        text: |-
               az datadog sso-config show --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup"
"""

helps['datadog sso-config create'] = """
    type: command
    short-summary: "Configures single-sign-on for this resource."
    parameters:
      - name: --properties
        long-summary: |
            Usage: --properties provisioning-state=XX single-sign-on-state=XX enterprise-app-id=XX

            single-sign-on-state: Various states of the SSO resource
            enterprise-app-id: The Id of the Enterprise App used for Single sign-on.
    examples:
      - name: SingleSignOnConfigurations_CreateOrUpdate
        text: |-
               az datadog sso-config create --configuration-name "default" --monitor-name "myMonitor" --properties \
enterprise-app-id="00000000-0000-0000-0000-000000000000" single-sign-on-state="Enable" --resource-group \
"myResourceGroup"
"""

helps['datadog sso-config update'] = """
    type: command
    short-summary: "Configures single-sign-on for this resource."
    parameters:
      - name: --properties
        long-summary: |
            Usage: --properties provisioning-state=XX single-sign-on-state=XX enterprise-app-id=XX

            single-sign-on-state: Various states of the SSO resource
            enterprise-app-id: The Id of the Enterprise App used for Single sign-on.
"""

helps['datadog sso-config wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datadog sso-config is met.
    examples:
      - name: Pause executing next line of CLI script until the datadog sso-config is successfully created.
        text: |-
               az datadog sso-config wait --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup" --created
      - name: Pause executing next line of CLI script until the datadog sso-config is successfully updated.
        text: |-
               az datadog sso-config wait --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup" --updated
"""
