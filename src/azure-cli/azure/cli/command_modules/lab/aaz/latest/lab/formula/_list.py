# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "lab formula list",
    is_preview=True,
)
class List(AAZCommand):
    """List formulas in a given lab.
    """

    _aaz_info = {
        "version": "2018-09-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/formulas", "2018-09-15"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.lab_name = AAZStrArg(
            options=["--lab-name"],
            help="The name of the lab.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Specify the $expand query. Example: 'properties($select=description)'",
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply to the operation. Example: '$filter=contains(name,'myName')",
        )
        _args_schema.orderby = AAZStrArg(
            options=["--orderby"],
            help="The ordering expression for the results, using OData notation. Example: '$orderby=name desc'",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="The maximum number of resources to return from the operation. Example: '$top=10'",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FormulasList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class FormulasList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/formulas",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "labName", self.ctx.args.lab_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$orderby", self.ctx.args.orderby,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2018-09-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.author = AAZStrType(
                flags={"read_only": True},
            )
            properties.creation_date = AAZStrType(
                serialized_name="creationDate",
                flags={"read_only": True},
            )
            properties.description = AAZStrType()
            properties.formula_content = AAZObjectType(
                serialized_name="formulaContent",
            )
            properties.os_type = AAZStrType(
                serialized_name="osType",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.unique_identifier = AAZStrType(
                serialized_name="uniqueIdentifier",
                flags={"read_only": True},
            )
            properties.vm = AAZObjectType()

            formula_content = cls._schema_on_200.value.Element.properties.formula_content
            formula_content.location = AAZStrType()
            formula_content.name = AAZStrType()
            formula_content.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            formula_content.tags = AAZDictType()

            properties = cls._schema_on_200.value.Element.properties.formula_content.properties
            properties.allow_claim = AAZBoolType(
                serialized_name="allowClaim",
            )
            properties.artifacts = AAZListType()
            properties.bulk_creation_parameters = AAZObjectType(
                serialized_name="bulkCreationParameters",
            )
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
            )
            properties.custom_image_id = AAZStrType(
                serialized_name="customImageId",
            )
            properties.data_disk_parameters = AAZListType(
                serialized_name="dataDiskParameters",
            )
            properties.disallow_public_ip_address = AAZBoolType(
                serialized_name="disallowPublicIpAddress",
            )
            properties.environment_id = AAZStrType(
                serialized_name="environmentId",
            )
            properties.expiration_date = AAZStrType(
                serialized_name="expirationDate",
            )
            properties.gallery_image_reference = AAZObjectType(
                serialized_name="galleryImageReference",
            )
            properties.is_authentication_with_ssh_key = AAZBoolType(
                serialized_name="isAuthenticationWithSshKey",
            )
            properties.lab_subnet_name = AAZStrType(
                serialized_name="labSubnetName",
            )
            properties.lab_virtual_network_id = AAZStrType(
                serialized_name="labVirtualNetworkId",
            )
            properties.network_interface = AAZObjectType(
                serialized_name="networkInterface",
            )
            properties.notes = AAZStrType()
            properties.owner_object_id = AAZStrType(
                serialized_name="ownerObjectId",
            )
            properties.owner_user_principal_name = AAZStrType(
                serialized_name="ownerUserPrincipalName",
            )
            properties.password = AAZStrType(
                flags={"secret": True},
            )
            properties.plan_id = AAZStrType(
                serialized_name="planId",
            )
            properties.schedule_parameters = AAZListType(
                serialized_name="scheduleParameters",
            )
            properties.size = AAZStrType()
            properties.ssh_key = AAZStrType(
                serialized_name="sshKey",
                flags={"secret": True},
            )
            properties.storage_type = AAZStrType(
                serialized_name="storageType",
            )
            properties.user_name = AAZStrType(
                serialized_name="userName",
            )

            artifacts = cls._schema_on_200.value.Element.properties.formula_content.properties.artifacts
            artifacts.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.formula_content.properties.artifacts.Element
            _element.artifact_id = AAZStrType(
                serialized_name="artifactId",
            )
            _element.artifact_title = AAZStrType(
                serialized_name="artifactTitle",
            )
            _element.deployment_status_message = AAZStrType(
                serialized_name="deploymentStatusMessage",
            )
            _element.install_time = AAZStrType(
                serialized_name="installTime",
            )
            _element.parameters = AAZListType()
            _element.status = AAZStrType()
            _element.vm_extension_status_message = AAZStrType(
                serialized_name="vmExtensionStatusMessage",
            )

            parameters = cls._schema_on_200.value.Element.properties.formula_content.properties.artifacts.Element.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.formula_content.properties.artifacts.Element.parameters.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            bulk_creation_parameters = cls._schema_on_200.value.Element.properties.formula_content.properties.bulk_creation_parameters
            bulk_creation_parameters.instance_count = AAZIntType(
                serialized_name="instanceCount",
            )

            data_disk_parameters = cls._schema_on_200.value.Element.properties.formula_content.properties.data_disk_parameters
            data_disk_parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.formula_content.properties.data_disk_parameters.Element
            _element.attach_new_data_disk_options = AAZObjectType(
                serialized_name="attachNewDataDiskOptions",
            )
            _element.existing_lab_disk_id = AAZStrType(
                serialized_name="existingLabDiskId",
            )
            _element.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )

            attach_new_data_disk_options = cls._schema_on_200.value.Element.properties.formula_content.properties.data_disk_parameters.Element.attach_new_data_disk_options
            attach_new_data_disk_options.disk_name = AAZStrType(
                serialized_name="diskName",
            )
            attach_new_data_disk_options.disk_size_gi_b = AAZIntType(
                serialized_name="diskSizeGiB",
            )
            attach_new_data_disk_options.disk_type = AAZStrType(
                serialized_name="diskType",
            )

            gallery_image_reference = cls._schema_on_200.value.Element.properties.formula_content.properties.gallery_image_reference
            gallery_image_reference.offer = AAZStrType()
            gallery_image_reference.os_type = AAZStrType(
                serialized_name="osType",
            )
            gallery_image_reference.publisher = AAZStrType()
            gallery_image_reference.sku = AAZStrType()
            gallery_image_reference.version = AAZStrType()

            network_interface = cls._schema_on_200.value.Element.properties.formula_content.properties.network_interface
            network_interface.dns_name = AAZStrType(
                serialized_name="dnsName",
            )
            network_interface.private_ip_address = AAZStrType(
                serialized_name="privateIpAddress",
            )
            network_interface.public_ip_address = AAZStrType(
                serialized_name="publicIpAddress",
            )
            network_interface.public_ip_address_id = AAZStrType(
                serialized_name="publicIpAddressId",
            )
            network_interface.rdp_authority = AAZStrType(
                serialized_name="rdpAuthority",
            )
            network_interface.shared_public_ip_address_configuration = AAZObjectType(
                serialized_name="sharedPublicIpAddressConfiguration",
            )
            network_interface.ssh_authority = AAZStrType(
                serialized_name="sshAuthority",
            )
            network_interface.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )
            network_interface.virtual_network_id = AAZStrType(
                serialized_name="virtualNetworkId",
            )

            shared_public_ip_address_configuration = cls._schema_on_200.value.Element.properties.formula_content.properties.network_interface.shared_public_ip_address_configuration
            shared_public_ip_address_configuration.inbound_nat_rules = AAZListType(
                serialized_name="inboundNatRules",
            )

            inbound_nat_rules = cls._schema_on_200.value.Element.properties.formula_content.properties.network_interface.shared_public_ip_address_configuration.inbound_nat_rules
            inbound_nat_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.formula_content.properties.network_interface.shared_public_ip_address_configuration.inbound_nat_rules.Element
            _element.backend_port = AAZIntType(
                serialized_name="backendPort",
            )
            _element.frontend_port = AAZIntType(
                serialized_name="frontendPort",
            )
            _element.transport_protocol = AAZStrType(
                serialized_name="transportProtocol",
            )

            schedule_parameters = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters
            schedule_parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()

            properties = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties
            properties.daily_recurrence = AAZObjectType(
                serialized_name="dailyRecurrence",
            )
            properties.hourly_recurrence = AAZObjectType(
                serialized_name="hourlyRecurrence",
            )
            properties.notification_settings = AAZObjectType(
                serialized_name="notificationSettings",
            )
            properties.status = AAZStrType()
            properties.target_resource_id = AAZStrType(
                serialized_name="targetResourceId",
            )
            properties.task_type = AAZStrType(
                serialized_name="taskType",
            )
            properties.time_zone_id = AAZStrType(
                serialized_name="timeZoneId",
            )
            properties.weekly_recurrence = AAZObjectType(
                serialized_name="weeklyRecurrence",
            )

            daily_recurrence = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties.daily_recurrence
            daily_recurrence.time = AAZStrType()

            hourly_recurrence = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties.hourly_recurrence
            hourly_recurrence.minute = AAZIntType()

            notification_settings = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties.notification_settings
            notification_settings.email_recipient = AAZStrType(
                serialized_name="emailRecipient",
            )
            notification_settings.notification_locale = AAZStrType(
                serialized_name="notificationLocale",
            )
            notification_settings.status = AAZStrType()
            notification_settings.time_in_minutes = AAZIntType(
                serialized_name="timeInMinutes",
            )
            notification_settings.webhook_url = AAZStrType(
                serialized_name="webhookUrl",
            )

            weekly_recurrence = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties.weekly_recurrence
            weekly_recurrence.time = AAZStrType()
            weekly_recurrence.weekdays = AAZListType()

            weekdays = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.properties.weekly_recurrence.weekdays
            weekdays.Element = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.formula_content.properties.schedule_parameters.Element.tags
            tags.Element = AAZStrType()

            tags = cls._schema_on_200.value.Element.properties.formula_content.tags
            tags.Element = AAZStrType()

            vm = cls._schema_on_200.value.Element.properties.vm
            vm.lab_vm_id = AAZStrType(
                serialized_name="labVmId",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
