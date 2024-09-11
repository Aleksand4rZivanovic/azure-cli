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
    "lab vm wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/virtualmachines/{}", "2018-09-15"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

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
            id_part="name",
        )
        _args_schema.name = AAZStrArg(
            options=["--name"],
            help="The name of the virtual machine.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualMachinesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class VirtualMachinesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualmachines/{name}",
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
                    "name", self.ctx.args.name,
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.allow_claim = AAZBoolType(
                serialized_name="allowClaim",
            )
            properties.applicable_schedule = AAZObjectType(
                serialized_name="applicableSchedule",
                flags={"read_only": True},
            )
            properties.artifact_deployment_status = AAZObjectType(
                serialized_name="artifactDeploymentStatus",
                flags={"read_only": True},
            )
            properties.artifacts = AAZListType()
            properties.compute_id = AAZStrType(
                serialized_name="computeId",
                flags={"read_only": True},
            )
            properties.compute_vm = AAZObjectType(
                serialized_name="computeVm",
                flags={"read_only": True},
            )
            properties.created_by_user = AAZStrType(
                serialized_name="createdByUser",
                flags={"read_only": True},
            )
            properties.created_by_user_id = AAZStrType(
                serialized_name="createdByUserId",
                flags={"read_only": True},
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
            properties.fqdn = AAZStrType(
                flags={"read_only": True},
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
            properties.last_known_power_state = AAZStrType(
                serialized_name="lastKnownPowerState",
                flags={"read_only": True},
            )
            properties.network_interface = AAZObjectType(
                serialized_name="networkInterface",
            )
            properties.notes = AAZStrType()
            properties.os_type = AAZStrType(
                serialized_name="osType",
                flags={"read_only": True},
            )
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
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
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
            properties.unique_identifier = AAZStrType(
                serialized_name="uniqueIdentifier",
                flags={"read_only": True},
            )
            properties.user_name = AAZStrType(
                serialized_name="userName",
            )
            properties.virtual_machine_creation_source = AAZStrType(
                serialized_name="virtualMachineCreationSource",
                flags={"read_only": True},
            )

            applicable_schedule = cls._schema_on_200.properties.applicable_schedule
            applicable_schedule.id = AAZStrType(
                flags={"read_only": True},
            )
            applicable_schedule.location = AAZStrType()
            applicable_schedule.name = AAZStrType(
                flags={"read_only": True},
            )
            applicable_schedule.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            applicable_schedule.tags = AAZDictType()
            applicable_schedule.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.applicable_schedule.properties
            properties.lab_vms_shutdown = AAZObjectType(
                serialized_name="labVmsShutdown",
            )
            _WaitHelper._build_schema_schedule_read(properties.lab_vms_shutdown)
            properties.lab_vms_startup = AAZObjectType(
                serialized_name="labVmsStartup",
            )
            _WaitHelper._build_schema_schedule_read(properties.lab_vms_startup)

            tags = cls._schema_on_200.properties.applicable_schedule.tags
            tags.Element = AAZStrType()

            artifact_deployment_status = cls._schema_on_200.properties.artifact_deployment_status
            artifact_deployment_status.artifacts_applied = AAZIntType(
                serialized_name="artifactsApplied",
            )
            artifact_deployment_status.deployment_status = AAZStrType(
                serialized_name="deploymentStatus",
            )
            artifact_deployment_status.total_artifacts = AAZIntType(
                serialized_name="totalArtifacts",
            )

            artifacts = cls._schema_on_200.properties.artifacts
            artifacts.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.artifacts.Element
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

            parameters = cls._schema_on_200.properties.artifacts.Element.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.artifacts.Element.parameters.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            compute_vm = cls._schema_on_200.properties.compute_vm
            compute_vm.data_disk_ids = AAZListType(
                serialized_name="dataDiskIds",
            )
            compute_vm.data_disks = AAZListType(
                serialized_name="dataDisks",
            )
            compute_vm.network_interface_id = AAZStrType(
                serialized_name="networkInterfaceId",
            )
            compute_vm.os_disk_id = AAZStrType(
                serialized_name="osDiskId",
            )
            compute_vm.os_type = AAZStrType(
                serialized_name="osType",
            )
            compute_vm.statuses = AAZListType()
            compute_vm.vm_size = AAZStrType(
                serialized_name="vmSize",
            )

            data_disk_ids = cls._schema_on_200.properties.compute_vm.data_disk_ids
            data_disk_ids.Element = AAZStrType()

            data_disks = cls._schema_on_200.properties.compute_vm.data_disks
            data_disks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.compute_vm.data_disks.Element
            _element.disk_size_gi_b = AAZIntType(
                serialized_name="diskSizeGiB",
            )
            _element.disk_uri = AAZStrType(
                serialized_name="diskUri",
            )
            _element.managed_disk_id = AAZStrType(
                serialized_name="managedDiskId",
            )
            _element.name = AAZStrType()

            statuses = cls._schema_on_200.properties.compute_vm.statuses
            statuses.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.compute_vm.statuses.Element
            _element.code = AAZStrType()
            _element.display_status = AAZStrType(
                serialized_name="displayStatus",
            )
            _element.message = AAZStrType()

            data_disk_parameters = cls._schema_on_200.properties.data_disk_parameters
            data_disk_parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.data_disk_parameters.Element
            _element.attach_new_data_disk_options = AAZObjectType(
                serialized_name="attachNewDataDiskOptions",
            )
            _element.existing_lab_disk_id = AAZStrType(
                serialized_name="existingLabDiskId",
            )
            _element.host_caching = AAZStrType(
                serialized_name="hostCaching",
            )

            attach_new_data_disk_options = cls._schema_on_200.properties.data_disk_parameters.Element.attach_new_data_disk_options
            attach_new_data_disk_options.disk_name = AAZStrType(
                serialized_name="diskName",
            )
            attach_new_data_disk_options.disk_size_gi_b = AAZIntType(
                serialized_name="diskSizeGiB",
            )
            attach_new_data_disk_options.disk_type = AAZStrType(
                serialized_name="diskType",
            )

            gallery_image_reference = cls._schema_on_200.properties.gallery_image_reference
            gallery_image_reference.offer = AAZStrType()
            gallery_image_reference.os_type = AAZStrType(
                serialized_name="osType",
            )
            gallery_image_reference.publisher = AAZStrType()
            gallery_image_reference.sku = AAZStrType()
            gallery_image_reference.version = AAZStrType()

            network_interface = cls._schema_on_200.properties.network_interface
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

            shared_public_ip_address_configuration = cls._schema_on_200.properties.network_interface.shared_public_ip_address_configuration
            shared_public_ip_address_configuration.inbound_nat_rules = AAZListType(
                serialized_name="inboundNatRules",
            )

            inbound_nat_rules = cls._schema_on_200.properties.network_interface.shared_public_ip_address_configuration.inbound_nat_rules
            inbound_nat_rules.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_interface.shared_public_ip_address_configuration.inbound_nat_rules.Element
            _element.backend_port = AAZIntType(
                serialized_name="backendPort",
            )
            _element.frontend_port = AAZIntType(
                serialized_name="frontendPort",
            )
            _element.transport_protocol = AAZStrType(
                serialized_name="transportProtocol",
            )

            schedule_parameters = cls._schema_on_200.properties.schedule_parameters
            schedule_parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.schedule_parameters.Element
            _element.location = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()

            properties = cls._schema_on_200.properties.schedule_parameters.Element.properties
            properties.daily_recurrence = AAZObjectType(
                serialized_name="dailyRecurrence",
            )
            _WaitHelper._build_schema_day_details_read(properties.daily_recurrence)
            properties.hourly_recurrence = AAZObjectType(
                serialized_name="hourlyRecurrence",
            )
            _WaitHelper._build_schema_hour_details_read(properties.hourly_recurrence)
            properties.notification_settings = AAZObjectType(
                serialized_name="notificationSettings",
            )
            _WaitHelper._build_schema_notification_settings_read(properties.notification_settings)
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
            _WaitHelper._build_schema_week_details_read(properties.weekly_recurrence)

            tags = cls._schema_on_200.properties.schedule_parameters.Element.tags
            tags.Element = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_day_details_read = None

    @classmethod
    def _build_schema_day_details_read(cls, _schema):
        if cls._schema_day_details_read is not None:
            _schema.time = cls._schema_day_details_read.time
            return

        cls._schema_day_details_read = _schema_day_details_read = AAZObjectType()

        day_details_read = _schema_day_details_read
        day_details_read.time = AAZStrType()

        _schema.time = cls._schema_day_details_read.time

    _schema_hour_details_read = None

    @classmethod
    def _build_schema_hour_details_read(cls, _schema):
        if cls._schema_hour_details_read is not None:
            _schema.minute = cls._schema_hour_details_read.minute
            return

        cls._schema_hour_details_read = _schema_hour_details_read = AAZObjectType()

        hour_details_read = _schema_hour_details_read
        hour_details_read.minute = AAZIntType()

        _schema.minute = cls._schema_hour_details_read.minute

    _schema_notification_settings_read = None

    @classmethod
    def _build_schema_notification_settings_read(cls, _schema):
        if cls._schema_notification_settings_read is not None:
            _schema.email_recipient = cls._schema_notification_settings_read.email_recipient
            _schema.notification_locale = cls._schema_notification_settings_read.notification_locale
            _schema.status = cls._schema_notification_settings_read.status
            _schema.time_in_minutes = cls._schema_notification_settings_read.time_in_minutes
            _schema.webhook_url = cls._schema_notification_settings_read.webhook_url
            return

        cls._schema_notification_settings_read = _schema_notification_settings_read = AAZObjectType()

        notification_settings_read = _schema_notification_settings_read
        notification_settings_read.email_recipient = AAZStrType(
            serialized_name="emailRecipient",
        )
        notification_settings_read.notification_locale = AAZStrType(
            serialized_name="notificationLocale",
        )
        notification_settings_read.status = AAZStrType()
        notification_settings_read.time_in_minutes = AAZIntType(
            serialized_name="timeInMinutes",
        )
        notification_settings_read.webhook_url = AAZStrType(
            serialized_name="webhookUrl",
        )

        _schema.email_recipient = cls._schema_notification_settings_read.email_recipient
        _schema.notification_locale = cls._schema_notification_settings_read.notification_locale
        _schema.status = cls._schema_notification_settings_read.status
        _schema.time_in_minutes = cls._schema_notification_settings_read.time_in_minutes
        _schema.webhook_url = cls._schema_notification_settings_read.webhook_url

    _schema_schedule_read = None

    @classmethod
    def _build_schema_schedule_read(cls, _schema):
        if cls._schema_schedule_read is not None:
            _schema.id = cls._schema_schedule_read.id
            _schema.location = cls._schema_schedule_read.location
            _schema.name = cls._schema_schedule_read.name
            _schema.properties = cls._schema_schedule_read.properties
            _schema.tags = cls._schema_schedule_read.tags
            _schema.type = cls._schema_schedule_read.type
            return

        cls._schema_schedule_read = _schema_schedule_read = AAZObjectType()

        schedule_read = _schema_schedule_read
        schedule_read.id = AAZStrType(
            flags={"read_only": True},
        )
        schedule_read.location = AAZStrType()
        schedule_read.name = AAZStrType(
            flags={"read_only": True},
        )
        schedule_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        schedule_read.tags = AAZDictType()
        schedule_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_schedule_read.properties
        properties.created_date = AAZStrType(
            serialized_name="createdDate",
            flags={"read_only": True},
        )
        properties.daily_recurrence = AAZObjectType(
            serialized_name="dailyRecurrence",
        )
        cls._build_schema_day_details_read(properties.daily_recurrence)
        properties.hourly_recurrence = AAZObjectType(
            serialized_name="hourlyRecurrence",
        )
        cls._build_schema_hour_details_read(properties.hourly_recurrence)
        properties.notification_settings = AAZObjectType(
            serialized_name="notificationSettings",
        )
        cls._build_schema_notification_settings_read(properties.notification_settings)
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
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
        properties.unique_identifier = AAZStrType(
            serialized_name="uniqueIdentifier",
            flags={"read_only": True},
        )
        properties.weekly_recurrence = AAZObjectType(
            serialized_name="weeklyRecurrence",
        )
        cls._build_schema_week_details_read(properties.weekly_recurrence)

        tags = _schema_schedule_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_schedule_read.id
        _schema.location = cls._schema_schedule_read.location
        _schema.name = cls._schema_schedule_read.name
        _schema.properties = cls._schema_schedule_read.properties
        _schema.tags = cls._schema_schedule_read.tags
        _schema.type = cls._schema_schedule_read.type

    _schema_week_details_read = None

    @classmethod
    def _build_schema_week_details_read(cls, _schema):
        if cls._schema_week_details_read is not None:
            _schema.time = cls._schema_week_details_read.time
            _schema.weekdays = cls._schema_week_details_read.weekdays
            return

        cls._schema_week_details_read = _schema_week_details_read = AAZObjectType()

        week_details_read = _schema_week_details_read
        week_details_read.time = AAZStrType()
        week_details_read.weekdays = AAZListType()

        weekdays = _schema_week_details_read.weekdays
        weekdays.Element = AAZStrType()

        _schema.time = cls._schema_week_details_read.time
        _schema.weekdays = cls._schema_week_details_read.weekdays


__all__ = ["Wait"]
