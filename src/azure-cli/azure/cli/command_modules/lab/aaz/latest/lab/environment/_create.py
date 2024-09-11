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
    "lab environment create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create an existing environment. This operation can take a while to complete.
    """

    _aaz_info = {
        "version": "2018-09-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devtestlab/labs/{}/users/{}/environments/{}", "2018-09-15"],
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
        _args_schema.lab_name = AAZStrArg(
            options=["--lab-name"],
            help="The name of the lab.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the environment.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.user_name = AAZStrArg(
            options=["--user-name"],
            help="The name of the user profile.",
            required=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="The tags of the resource.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "DtlEnvironment"

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.deployment_properties = AAZObjectArg(
            options=["--deployment-properties"],
            arg_group="Properties",
            help="The deployment properties of the environment.",
        )

        deployment_properties = cls._args_schema.deployment_properties
        deployment_properties.arm_template_id = AAZStrArg(
            options=["arm-template-id"],
            help="The Azure Resource Manager template's identifier.",
        )
        deployment_properties.parameters = AAZListArg(
            options=["parameters"],
            help="The parameters of the Azure Resource Manager template.",
        )

        parameters = cls._args_schema.deployment_properties.parameters
        parameters.Element = AAZObjectArg()

        _element = cls._args_schema.deployment_properties.parameters.Element
        _element.name = AAZStrArg(
            options=["name"],
            help="The name of the template parameter.",
        )
        _element.value = AAZStrArg(
            options=["value"],
            help="The value of the template parameter.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.EnvironmentsCreateOrUpdate(ctx=self.ctx)()
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

    class EnvironmentsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/users/{userName}/environments/{name}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                **self.serialize_url_param(
                    "userName", self.ctx.args.user_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("deploymentProperties", AAZObjectType, ".deployment_properties")

            deployment_properties = _builder.get(".properties.deploymentProperties")
            if deployment_properties is not None:
                deployment_properties.set_prop("armTemplateId", AAZStrType, ".arm_template_id")
                deployment_properties.set_prop("parameters", AAZListType, ".parameters")

            parameters = _builder.get(".properties.deploymentProperties.parameters")
            if parameters is not None:
                parameters.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.deploymentProperties.parameters[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("value", AAZStrType, ".value")

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
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.arm_template_display_name = AAZStrType(
                serialized_name="armTemplateDisplayName",
            )
            properties.created_by_user = AAZStrType(
                serialized_name="createdByUser",
                flags={"read_only": True},
            )
            properties.deployment_properties = AAZObjectType(
                serialized_name="deploymentProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_group_id = AAZStrType(
                serialized_name="resourceGroupId",
                flags={"read_only": True},
            )
            properties.unique_identifier = AAZStrType(
                serialized_name="uniqueIdentifier",
                flags={"read_only": True},
            )

            deployment_properties = cls._schema_on_200_201.properties.deployment_properties
            deployment_properties.arm_template_id = AAZStrType(
                serialized_name="armTemplateId",
            )
            deployment_properties.parameters = AAZListType()

            parameters = cls._schema_on_200_201.properties.deployment_properties.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.deployment_properties.parameters.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
