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
    "cosmosdb postgres cluster create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create a new cluster with servers.

    :example: Create a new single node cluster
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --enable-ha false --coordinator-v-cores 8 --coordinator-server-edition "GeneralPurpose" --coordinator-storage 131072 --enable-shards-on-coord true --node-count 0 --preferred-primary-zone "1" --login-password "password"

    :example: Create a new cluster as a point in time restore
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --point-in-time-utc "2017-12-14T00:00:37.467Z" --source-location "eastus" --source-resource-id "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testGroup/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/source-cluster"

    :example: Create a new cluster as a read replica
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --source-location "eastus" --source-resource-id "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testGroup/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/source-cluster"

    :example: Create a new multi-node cluster
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --enable-ha false --coordinator-v-cores 8 --coordinator-server-edition "GeneralPurpose" --coordinator-storage 131072 --enable-shards-on-coord false --node-count 3 --node-server-edition "MemoryOptimized" --node-v-cores 8 --node-storage 131072 --postgresql-version "15" --preferred-primary-zone "1" --login-password "password"

    :example: Create a new single node Burstable 1 vCore cluster
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --enable-ha false --coordinator-v-cores 1 --coordinator-server-edition "BurstableMemoryOptimized" --coord-public-ip-access true --coordinator-storage 131072 --enable-shards-on-coord true --node-count 0 --preferred-primary-zone "1" --login-password "password"

    :example: Create a new single node Burstable 2 vCores cluster
        az cosmosdb postgres cluster create -n "test-cluster" -g "testGroup" --subscription "ffffffff-ffff-ffff-ffff-ffffffffffff" --enable-ha false --coordinator-v-cores 2 --coordinator-server-edition "BurstableGeneralPurpose" --coord-public-ip-access true --coordinator-storage 131072 --enable-shards-on-coord true --node-count 0 --preferred-primary-zone "1" --login-password "password"
    """

    _aaz_info = {
        "version": "2022-11-08",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dbforpostgresql/servergroupsv2/{}", "2022-11-08"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the cluster.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^(?![0-9]+$)(?!-)[a-z0-9-]{3,40}(?<!-)$",
                max_length=40,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Parameters",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.administrator_login_password = AAZPasswordArg(
            options=["--login-password", "--administrator-login-password"],
            arg_group="Properties",
            help="The password of the administrator login. Required for creation.",
            blank=AAZPromptPasswordInput(
                msg="Password:",
            ),
        )
        _args_schema.citus_version = AAZStrArg(
            options=["--citus-version"],
            arg_group="Properties",
            help="The Citus extension version on all cluster servers.",
        )
        _args_schema.coordinator_enable_public_ip_access = AAZBoolArg(
            options=["--coord-public-ip-access", "--coordinator-enable-public-ip-access"],
            arg_group="Properties",
            help="If public access is enabled on coordinator.",
        )
        _args_schema.coordinator_server_edition = AAZStrArg(
            options=["--coord-server-edition", "--coordinator-server-edition"],
            arg_group="Properties",
            help="The edition of a coordinator server (default: GeneralPurpose). Required for creation.",
        )
        _args_schema.coordinator_storage_quota_in_mb = AAZIntArg(
            options=["--coordinator-storage", "--coordinator-storage-quota-in-mb"],
            arg_group="Properties",
            help="The storage of a server in MB. Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.",
        )
        _args_schema.coordinator_v_cores = AAZIntArg(
            options=["--coordinator-v-cores"],
            arg_group="Properties",
            help="The vCores count of a server (max: 96). Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.",
        )
        _args_schema.enable_ha = AAZBoolArg(
            options=["--enable-ha"],
            arg_group="Properties",
            help="If high availability (HA) is enabled or not for the cluster.",
        )
        _args_schema.enable_shards_on_coordinator = AAZBoolArg(
            options=["--enable-shards-on-coord", "--enable-shards-on-coordinator"],
            arg_group="Properties",
            help="If shards on coordinator is enabled or not for the cluster.",
        )
        _args_schema.maintenance_window = AAZObjectArg(
            options=["--maintenance-window"],
            arg_group="Properties",
            help="Maintenance window of a cluster.",
        )
        _args_schema.node_count = AAZIntArg(
            options=["--node-count"],
            arg_group="Properties",
            help="Worker node count of the cluster. When node count is 0, it represents a single node configuration with the ability to create distributed tables on that node. 2 or more worker nodes represent multi-node configuration. Node count value cannot be 1. Required for creation.",
        )
        _args_schema.node_enable_public_ip_access = AAZBoolArg(
            options=["--node-public-ip-access", "--node-enable-public-ip-access"],
            arg_group="Properties",
            help="If public access is enabled on worker nodes.",
        )
        _args_schema.node_server_edition = AAZStrArg(
            options=["--node-server-edition"],
            arg_group="Properties",
            help="The edition of a node server (default: MemoryOptimized).",
        )
        _args_schema.node_storage_quota_in_mb = AAZIntArg(
            options=["--node-storage", "--node-storage-quota-in-mb"],
            arg_group="Properties",
            help="The storage in MB on each worker node. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.",
        )
        _args_schema.node_v_cores = AAZIntArg(
            options=["--node-v-cores"],
            arg_group="Properties",
            help="The compute in vCores on each worker node (max: 104). See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.",
        )
        _args_schema.point_in_time_utc = AAZDateTimeArg(
            options=["--point-in-time-utc"],
            arg_group="Properties",
            help="Date and time in UTC (ISO8601 format) for cluster restore.",
        )
        _args_schema.postgresql_version = AAZStrArg(
            options=["--postgresql-version"],
            arg_group="Properties",
            help="The major PostgreSQL version on all cluster servers.",
        )
        _args_schema.preferred_primary_zone = AAZStrArg(
            options=["--preferred-primary-zone"],
            arg_group="Properties",
            help="Preferred primary availability zone (AZ) for all cluster servers.",
        )
        _args_schema.source_location = AAZStrArg(
            options=["--source-location"],
            arg_group="Properties",
            help="The Azure region of source cluster for read replica clusters.",
        )
        _args_schema.source_resource_id = AAZStrArg(
            options=["--source-resource-id"],
            arg_group="Properties",
            help="The resource id of source cluster for read replica clusters.",
        )

        maintenance_window = cls._args_schema.maintenance_window
        maintenance_window.custom_window = AAZStrArg(
            options=["custom-window"],
            help="Indicates whether custom maintenance window is enabled or not.",
        )
        maintenance_window.day_of_week = AAZIntArg(
            options=["day-of-week"],
            help="Preferred day of the week for maintenance window.",
        )
        maintenance_window.start_hour = AAZIntArg(
            options=["start-hour"],
            help="Start hour within preferred day of the week for maintenance window.",
        )
        maintenance_window.start_minute = AAZIntArg(
            options=["start-minute"],
            help="Start minute within the start hour for maintenance window.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ClustersCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/serverGroupsv2/{clusterName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
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
                    "api-version", "2022-11-08",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("administratorLoginPassword", AAZStrType, ".administrator_login_password", typ_kwargs={"flags": {"secret": True}})
                properties.set_prop("citusVersion", AAZStrType, ".citus_version")
                properties.set_prop("coordinatorEnablePublicIpAccess", AAZBoolType, ".coordinator_enable_public_ip_access")
                properties.set_prop("coordinatorServerEdition", AAZStrType, ".coordinator_server_edition")
                properties.set_prop("coordinatorStorageQuotaInMb", AAZIntType, ".coordinator_storage_quota_in_mb")
                properties.set_prop("coordinatorVCores", AAZIntType, ".coordinator_v_cores")
                properties.set_prop("enableHa", AAZBoolType, ".enable_ha")
                properties.set_prop("enableShardsOnCoordinator", AAZBoolType, ".enable_shards_on_coordinator")
                properties.set_prop("maintenanceWindow", AAZObjectType, ".maintenance_window")
                properties.set_prop("nodeCount", AAZIntType, ".node_count")
                properties.set_prop("nodeEnablePublicIpAccess", AAZBoolType, ".node_enable_public_ip_access")
                properties.set_prop("nodeServerEdition", AAZStrType, ".node_server_edition")
                properties.set_prop("nodeStorageQuotaInMb", AAZIntType, ".node_storage_quota_in_mb")
                properties.set_prop("nodeVCores", AAZIntType, ".node_v_cores")
                properties.set_prop("pointInTimeUTC", AAZStrType, ".point_in_time_utc")
                properties.set_prop("postgresqlVersion", AAZStrType, ".postgresql_version")
                properties.set_prop("preferredPrimaryZone", AAZStrType, ".preferred_primary_zone")
                properties.set_prop("sourceLocation", AAZStrType, ".source_location")
                properties.set_prop("sourceResourceId", AAZStrType, ".source_resource_id")

            maintenance_window = _builder.get(".properties.maintenanceWindow")
            if maintenance_window is not None:
                maintenance_window.set_prop("customWindow", AAZStrType, ".custom_window")
                maintenance_window.set_prop("dayOfWeek", AAZIntType, ".day_of_week")
                maintenance_window.set_prop("startHour", AAZIntType, ".start_hour")
                maintenance_window.set_prop("startMinute", AAZIntType, ".start_minute")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(_schema_on_200_201.system_data)
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.administrator_login = AAZStrType(
                serialized_name="administratorLogin",
                flags={"read_only": True},
            )
            properties.citus_version = AAZStrType(
                serialized_name="citusVersion",
            )
            properties.coordinator_enable_public_ip_access = AAZBoolType(
                serialized_name="coordinatorEnablePublicIpAccess",
            )
            properties.coordinator_server_edition = AAZStrType(
                serialized_name="coordinatorServerEdition",
            )
            properties.coordinator_storage_quota_in_mb = AAZIntType(
                serialized_name="coordinatorStorageQuotaInMb",
            )
            properties.coordinator_v_cores = AAZIntType(
                serialized_name="coordinatorVCores",
            )
            properties.earliest_restore_time = AAZStrType(
                serialized_name="earliestRestoreTime",
                flags={"read_only": True},
            )
            properties.enable_ha = AAZBoolType(
                serialized_name="enableHa",
            )
            properties.enable_shards_on_coordinator = AAZBoolType(
                serialized_name="enableShardsOnCoordinator",
            )
            properties.maintenance_window = AAZObjectType(
                serialized_name="maintenanceWindow",
            )
            properties.node_count = AAZIntType(
                serialized_name="nodeCount",
            )
            properties.node_enable_public_ip_access = AAZBoolType(
                serialized_name="nodeEnablePublicIpAccess",
            )
            properties.node_server_edition = AAZStrType(
                serialized_name="nodeServerEdition",
            )
            properties.node_storage_quota_in_mb = AAZIntType(
                serialized_name="nodeStorageQuotaInMb",
            )
            properties.node_v_cores = AAZIntType(
                serialized_name="nodeVCores",
            )
            properties.point_in_time_utc = AAZStrType(
                serialized_name="pointInTimeUTC",
            )
            properties.postgresql_version = AAZStrType(
                serialized_name="postgresqlVersion",
            )
            properties.preferred_primary_zone = AAZStrType(
                serialized_name="preferredPrimaryZone",
            )
            properties.private_endpoint_connections = AAZListType(
                serialized_name="privateEndpointConnections",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.read_replicas = AAZListType(
                serialized_name="readReplicas",
                flags={"read_only": True},
            )
            properties.server_names = AAZListType(
                serialized_name="serverNames",
                flags={"read_only": True},
            )
            properties.source_location = AAZStrType(
                serialized_name="sourceLocation",
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
            )
            properties.state = AAZStrType(
                flags={"read_only": True},
            )

            maintenance_window = cls._schema_on_200_201.properties.maintenance_window
            maintenance_window.custom_window = AAZStrType(
                serialized_name="customWindow",
            )
            maintenance_window.day_of_week = AAZIntType(
                serialized_name="dayOfWeek",
            )
            maintenance_window.start_hour = AAZIntType(
                serialized_name="startHour",
            )
            maintenance_window.start_minute = AAZIntType(
                serialized_name="startMinute",
            )

            private_endpoint_connections = cls._schema_on_200_201.properties.private_endpoint_connections
            private_endpoint_connections.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.private_endpoint_connections.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _CreateHelper._build_schema_system_data_read(_element.system_data)
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties
            properties.group_ids = AAZListType(
                serialized_name="groupIds",
            )
            properties.private_endpoint = AAZObjectType(
                serialized_name="privateEndpoint",
            )
            properties.private_link_service_connection_state = AAZObjectType(
                serialized_name="privateLinkServiceConnectionState",
            )

            group_ids = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.group_ids
            group_ids.Element = AAZStrType()

            private_endpoint = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_endpoint
            private_endpoint.id = AAZStrType()

            private_link_service_connection_state = cls._schema_on_200_201.properties.private_endpoint_connections.Element.properties.private_link_service_connection_state
            private_link_service_connection_state.actions_required = AAZStrType(
                serialized_name="actionsRequired",
            )
            private_link_service_connection_state.description = AAZStrType()
            private_link_service_connection_state.status = AAZStrType()

            read_replicas = cls._schema_on_200_201.properties.read_replicas
            read_replicas.Element = AAZStrType()

            server_names = cls._schema_on_200_201.properties.server_names
            server_names.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.server_names.Element
            _element.fully_qualified_domain_name = AAZStrType(
                serialized_name="fullyQualifiedDomainName",
                flags={"read_only": True},
            )
            _element.name = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_system_data_read = None

    @classmethod
    def _build_schema_system_data_read(cls, _schema):
        if cls._schema_system_data_read is not None:
            _schema.created_at = cls._schema_system_data_read.created_at
            _schema.created_by = cls._schema_system_data_read.created_by
            _schema.created_by_type = cls._schema_system_data_read.created_by_type
            _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
            _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
            _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type
            return

        cls._schema_system_data_read = _schema_system_data_read = AAZObjectType(
            flags={"read_only": True}
        )

        system_data_read = _schema_system_data_read
        system_data_read.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data_read.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data_read.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data_read.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data_read.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data_read.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.created_at = cls._schema_system_data_read.created_at
        _schema.created_by = cls._schema_system_data_read.created_by
        _schema.created_by_type = cls._schema_system_data_read.created_by_type
        _schema.last_modified_at = cls._schema_system_data_read.last_modified_at
        _schema.last_modified_by = cls._schema_system_data_read.last_modified_by
        _schema.last_modified_by_type = cls._schema_system_data_read.last_modified_by_type


__all__ = ["Create"]