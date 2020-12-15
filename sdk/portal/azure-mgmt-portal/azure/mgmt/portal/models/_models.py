# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Configuration(Resource):
    """Tenant configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param enforce_private_markdown_storage: When flag is set to true Markdown tile will require
     external storage configuration (URI). The inline content configuration will be prohibited.
    :type enforce_private_markdown_storage: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'enforce_private_markdown_storage': {'key': 'properties.enforcePrivateMarkdownStorage', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Configuration, self).__init__(**kwargs)
        self.enforce_private_markdown_storage = kwargs.get('enforce_private_markdown_storage', None)


class ConfigurationList(msrest.serialization.Model):
    """List of tenant configurations.

    :param value: The array of tenant configurations.
    :type value: list[~azure.mgmt.portal.models.Configuration]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Configuration]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class Dashboard(msrest.serialization.Model):
    """The shared dashboard resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param lenses: The dashboard lenses.
    :type lenses: list[~azure.mgmt.portal.models.DashboardLens]
    :param metadata: The dashboard metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'lenses': {'key': 'properties.lenses', 'type': '[DashboardLens]'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Dashboard, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)
        self.lenses = kwargs.get('lenses', None)
        self.metadata = kwargs.get('metadata', None)


class DashboardLens(msrest.serialization.Model):
    """A dashboard lens.

    All required parameters must be populated in order to send to Azure.

    :param order: Required. The lens order.
    :type order: int
    :param parts: Required. The dashboard parts.
    :type parts: list[~azure.mgmt.portal.models.DashboardParts]
    :param metadata: The dashboard len's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'order': {'required': True},
        'parts': {'required': True},
    }

    _attribute_map = {
        'order': {'key': 'order', 'type': 'int'},
        'parts': {'key': 'parts', 'type': '[DashboardParts]'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DashboardLens, self).__init__(**kwargs)
        self.order = kwargs['order']
        self.parts = kwargs['parts']
        self.metadata = kwargs.get('metadata', None)


class DashboardListResult(msrest.serialization.Model):
    """List of dashboards.

    :param value: The array of custom resource provider manifests.
    :type value: list[~azure.mgmt.portal.models.Dashboard]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Dashboard]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DashboardListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class DashboardPartMetadata(msrest.serialization.Model):
    """A dashboard part metadata.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MarkdownPartMetadata.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The type of dashboard part.Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Extension/HubsExtension/PartType/MarkdownPart': 'MarkdownPartMetadata'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DashboardPartMetadata, self).__init__(**kwargs)
        self.type = None  # type: Optional[str]


class DashboardParts(msrest.serialization.Model):
    """A dashboard part.

    All required parameters must be populated in order to send to Azure.

    :param position: Required. The dashboard's part position.
    :type position: ~azure.mgmt.portal.models.DashboardPartsPosition
    :param metadata: The dashboard part's metadata.
    :type metadata: ~azure.mgmt.portal.models.DashboardPartMetadata
    """

    _validation = {
        'position': {'required': True},
    }

    _attribute_map = {
        'position': {'key': 'position', 'type': 'DashboardPartsPosition'},
        'metadata': {'key': 'metadata', 'type': 'DashboardPartMetadata'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DashboardParts, self).__init__(**kwargs)
        self.position = kwargs['position']
        self.metadata = kwargs.get('metadata', None)


class DashboardPartsPosition(msrest.serialization.Model):
    """The dashboard's part position.

    All required parameters must be populated in order to send to Azure.

    :param x: Required. The dashboard's part x coordinate.
    :type x: int
    :param y: Required. The dashboard's part y coordinate.
    :type y: int
    :param row_span: Required. The dashboard's part row span.
    :type row_span: int
    :param col_span: Required. The dashboard's part column span.
    :type col_span: int
    :param metadata: The dashboard part's metadata.
    :type metadata: dict[str, object]
    """

    _validation = {
        'x': {'required': True},
        'y': {'required': True},
        'row_span': {'required': True},
        'col_span': {'required': True},
    }

    _attribute_map = {
        'x': {'key': 'x', 'type': 'int'},
        'y': {'key': 'y', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'},
        'col_span': {'key': 'colSpan', 'type': 'int'},
        'metadata': {'key': 'metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DashboardPartsPosition, self).__init__(**kwargs)
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.row_span = kwargs['row_span']
        self.col_span = kwargs['col_span']
        self.metadata = kwargs.get('metadata', None)


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: int
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~azure.mgmt.portal.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~azure.mgmt.portal.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class MarkdownPartMetadata(DashboardPartMetadata):
    """Markdown part metadata.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The type of dashboard part.Constant filled by server.
    :type type: str
    :param inputs: Input to dashboard part.
    :type inputs: list[object]
    :param settings: Markdown part settings.
    :type settings: ~azure.mgmt.portal.models.MarkdownPartMetadataSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[object]'},
        'settings': {'key': 'settings', 'type': 'MarkdownPartMetadataSettings'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MarkdownPartMetadata, self).__init__(**kwargs)
        self.type = 'Extension/HubsExtension/PartType/MarkdownPart'  # type: str
        self.inputs = kwargs.get('inputs', None)
        self.settings = kwargs.get('settings', None)


class MarkdownPartMetadataSettings(msrest.serialization.Model):
    """Markdown part settings.

    :param content: The content of markdown part.
    :type content: ~azure.mgmt.portal.models.MarkdownPartMetadataSettingsContent
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'MarkdownPartMetadataSettingsContent'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MarkdownPartMetadataSettings, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)


class MarkdownPartMetadataSettingsContent(msrest.serialization.Model):
    """The content of markdown part.

    :param settings: The setting of the content of markdown part.
    :type settings: ~azure.mgmt.portal.models.MarkdownPartMetadataSettingsContentSettings
    """

    _attribute_map = {
        'settings': {'key': 'settings', 'type': 'MarkdownPartMetadataSettingsContentSettings'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MarkdownPartMetadataSettingsContent, self).__init__(**kwargs)
        self.settings = kwargs.get('settings', None)


class MarkdownPartMetadataSettingsContentSettings(msrest.serialization.Model):
    """The setting of the content of markdown part.

    :param content: The content of the markdown part.
    :type content: str
    :param title: The title of the markdown part.
    :type title: str
    :param subtitle: The subtitle of the markdown part.
    :type subtitle: str
    :param markdown_source: The source of the content of the markdown part.
    :type markdown_source: int
    :param markdown_uri: The uri of markdown content.
    :type markdown_uri: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'subtitle': {'key': 'subtitle', 'type': 'str'},
        'markdown_source': {'key': 'markdownSource', 'type': 'int'},
        'markdown_uri': {'key': 'markdownUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MarkdownPartMetadataSettingsContentSettings, self).__init__(**kwargs)
        self.content = kwargs.get('content', None)
        self.title = kwargs.get('title', None)
        self.subtitle = kwargs.get('subtitle', None)
        self.markdown_source = kwargs.get('markdown_source', None)
        self.markdown_uri = kwargs.get('markdown_uri', None)


class PatchableDashboard(msrest.serialization.Model):
    """The shared dashboard resource definition.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param lenses: The dashboard lenses.
    :type lenses: list[~azure.mgmt.portal.models.DashboardLens]
    :param metadata: The dashboard metadata.
    :type metadata: dict[str, object]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'lenses': {'key': 'properties.lenses', 'type': '[DashboardLens]'},
        'metadata': {'key': 'properties.metadata', 'type': '{object}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PatchableDashboard, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.lenses = kwargs.get('lenses', None)
        self.metadata = kwargs.get('metadata', None)


class ProxyResource(Resource):
    """The resource model definition for an Azure Resource Manager proxy resource. It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operations of this resource provider.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param is_data_action: Indicates whether the operation applies to data-plane.
    :type is_data_action: str
    :param display: Display metadata associated with the operation.
    :type display: ~azure.mgmt.portal.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft Custom Providers.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """Results of the request to list operations.

    :param value: List of operations supported by this resource provider.
    :type value: list[~azure.mgmt.portal.models.ResourceProviderOperation]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class Violation(msrest.serialization.Model):
    """Violation information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id of the item that violates tenant configuration.
    :vartype id: str
    :ivar user_id: Id of the user who owns violated item.
    :vartype user_id: str
    :ivar error_message: Error message.
    :vartype error_message: str
    """

    _validation = {
        'id': {'readonly': True},
        'user_id': {'readonly': True},
        'error_message': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Violation, self).__init__(**kwargs)
        self.id = None
        self.user_id = None
        self.error_message = None


class ViolationsList(msrest.serialization.Model):
    """List of list of items that violate tenant's configuration.

    :param value: The array of violations.
    :type value: list[~azure.mgmt.portal.models.Violation]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Violation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ViolationsList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
