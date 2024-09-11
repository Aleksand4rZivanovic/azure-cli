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
    "lab vnet get",
    is_preview=True,
)
class Get(AAZCommand):
    """Get virtual network.
    """

    _aaz_info = {
        "version": "2018-09-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/virtualnetworks/{}", "2018-09-15"],
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
            help="The name of the virtual network.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="Specify the $expand query. Example: 'properties($expand=externalSubnets)'",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworksGet(ctx=self.ctx)()
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

    class VirtualNetworksGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/virtualnetworks/{name}",
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
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.allowed_subnets = AAZListType(
                serialized_name="allowedSubnets",
            )
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
                flags={"read_only": True},
            )
            properties.description = AAZStrType()
            properties.external_provider_resource_id = AAZStrType(
                serialized_name="externalProviderResourceId",
            )
            properties.external_subnets = AAZListType(
                serialized_name="externalSubnets",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.subnet_overrides = AAZListType(
                serialized_name="subnetOverrides",
            )
            properties.unique_identifier = AAZStrType(
                serialized_name="uniqueIdentifier",
                flags={"read_only": True},
            )

            allowed_subnets = cls._schema_on_200.properties.allowed_subnets
            allowed_subnets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.allowed_subnets.Element
            _element.allow_public_ip = AAZStrType(
                serialized_name="allowPublicIp",
            )
            _element.lab_subnet_name = AAZStrType(
                serialized_name="labSubnetName",
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            external_subnets = cls._schema_on_200.properties.external_subnets
            external_subnets.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.external_subnets.Element
            _element.id = AAZStrType()
            _element.name = AAZStrType()

            subnet_overrides = cls._schema_on_200.properties.subnet_overrides
            subnet_overrides.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.subnet_overrides.Element
            _element.lab_subnet_name = AAZStrType(
                serialized_name="labSubnetName",
            )
            _element.resource_id = AAZStrType(
                serialized_name="resourceId",
            )
            _element.shared_public_ip_address_configuration = AAZObjectType(
                serialized_name="sharedPublicIpAddressConfiguration",
            )
            _element.use_in_vm_creation_permission = AAZStrType(
                serialized_name="useInVmCreationPermission",
            )
            _element.use_public_ip_address_permission = AAZStrType(
                serialized_name="usePublicIpAddressPermission",
            )
            _element.virtual_network_pool_name = AAZStrType(
                serialized_name="virtualNetworkPoolName",
            )

            shared_public_ip_address_configuration = cls._schema_on_200.properties.subnet_overrides.Element.shared_public_ip_address_configuration
            shared_public_ip_address_configuration.allowed_ports = AAZListType(
                serialized_name="allowedPorts",
            )

            allowed_ports = cls._schema_on_200.properties.subnet_overrides.Element.shared_public_ip_address_configuration.allowed_ports
            allowed_ports.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.subnet_overrides.Element.shared_public_ip_address_configuration.allowed_ports.Element
            _element.backend_port = AAZIntType(
                serialized_name="backendPort",
            )
            _element.transport_protocol = AAZStrType(
                serialized_name="transportProtocol",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _GetHelper:
    """Helper class for Get"""


__all__ = ["Get"]
