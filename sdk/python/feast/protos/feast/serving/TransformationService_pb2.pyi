"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _TransformationServiceType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _TransformationServiceTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_TransformationServiceType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    TRANSFORMATION_SERVICE_TYPE_INVALID: TransformationServiceType.ValueType = ...  # 0
    TRANSFORMATION_SERVICE_TYPE_PYTHON: TransformationServiceType.ValueType = ...  # 1
    TRANSFORMATION_SERVICE_TYPE_CUSTOM: TransformationServiceType.ValueType = ...  # 100
class TransformationServiceType(_TransformationServiceType, metaclass=_TransformationServiceTypeEnumTypeWrapper):
    pass

TRANSFORMATION_SERVICE_TYPE_INVALID: TransformationServiceType.ValueType = ...  # 0
TRANSFORMATION_SERVICE_TYPE_PYTHON: TransformationServiceType.ValueType = ...  # 1
TRANSFORMATION_SERVICE_TYPE_CUSTOM: TransformationServiceType.ValueType = ...  # 100
global___TransformationServiceType = TransformationServiceType


class ValueType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ARROW_VALUE_FIELD_NUMBER: builtins.int
    arrow_value: builtins.bytes = ...
    """Having a oneOf provides forward compatibility if we need to support compound types
    that are not supported by arrow natively.
    """

    def __init__(self,
        *,
        arrow_value : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["arrow_value",b"arrow_value","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arrow_value",b"arrow_value","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["arrow_value"]]: ...
global___ValueType = ValueType

class GetTransformationServiceInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetTransformationServiceInfoRequest = GetTransformationServiceInfoRequest

class GetTransformationServiceInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TRANSFORMATION_SERVICE_TYPE_DETAILS_FIELD_NUMBER: builtins.int
    version: typing.Text = ...
    """Feast version of this transformation service deployment."""

    type: global___TransformationServiceType.ValueType = ...
    """Type of transformation service deployment. This is either Python, or custom"""

    transformation_service_type_details: typing.Text = ...
    def __init__(self,
        *,
        version : typing.Text = ...,
        type : global___TransformationServiceType.ValueType = ...,
        transformation_service_type_details : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["transformation_service_type_details",b"transformation_service_type_details","type",b"type","version",b"version"]) -> None: ...
global___GetTransformationServiceInfoResponse = GetTransformationServiceInfoResponse

class TransformFeaturesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ON_DEMAND_FEATURE_VIEW_NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    TRANSFORMATION_INPUT_FIELD_NUMBER: builtins.int
    on_demand_feature_view_name: typing.Text = ...
    project: typing.Text = ...
    @property
    def transformation_input(self) -> global___ValueType: ...
    def __init__(self,
        *,
        on_demand_feature_view_name : typing.Text = ...,
        project : typing.Text = ...,
        transformation_input : typing.Optional[global___ValueType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["transformation_input",b"transformation_input"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["on_demand_feature_view_name",b"on_demand_feature_view_name","project",b"project","transformation_input",b"transformation_input"]) -> None: ...
global___TransformFeaturesRequest = TransformFeaturesRequest

class TransformFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSFORMATION_OUTPUT_FIELD_NUMBER: builtins.int
    @property
    def transformation_output(self) -> global___ValueType: ...
    def __init__(self,
        *,
        transformation_output : typing.Optional[global___ValueType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["transformation_output",b"transformation_output"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["transformation_output",b"transformation_output"]) -> None: ...
global___TransformFeaturesResponse = TransformFeaturesResponse