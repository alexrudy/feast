"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import feast.types.Value_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Entity(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SPEC_FIELD_NUMBER: builtins.int
    META_FIELD_NUMBER: builtins.int
    @property
    def spec(self) -> global___EntitySpecV2:
        """User-specified specifications of this entity."""
        pass
    @property
    def meta(self) -> global___EntityMeta:
        """System-populated metadata for this entity."""
        pass
    def __init__(self,
        *,
        spec : typing.Optional[global___EntitySpecV2] = ...,
        meta : typing.Optional[global___EntityMeta] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["meta",b"meta","spec",b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["meta",b"meta","spec",b"spec"]) -> None: ...
global___Entity = Entity

class EntitySpecV2(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    JOIN_KEY_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    OWNER_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Name of the entity."""

    project: typing.Text = ...
    """Name of Feast project that this feature table belongs to."""

    value_type: feast.types.Value_pb2.ValueType.Enum.ValueType = ...
    """Type of the entity."""

    description: typing.Text = ...
    """Description of the entity."""

    join_key: typing.Text = ...
    """Join key for the entity (i.e. name of the column the entity maps to)."""

    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """User defined metadata"""
        pass
    owner: typing.Text = ...
    """Owner of the entity."""

    def __init__(self,
        *,
        name : typing.Text = ...,
        project : typing.Text = ...,
        value_type : feast.types.Value_pb2.ValueType.Enum.ValueType = ...,
        description : typing.Text = ...,
        join_key : typing.Text = ...,
        tags : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        owner : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description","join_key",b"join_key","name",b"name","owner",b"owner","project",b"project","tags",b"tags","value_type",b"value_type"]) -> None: ...
global___EntitySpecV2 = EntitySpecV2

class EntityMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: builtins.int
    @property
    def created_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_updated_timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        created_timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_updated_timestamp : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_timestamp",b"created_timestamp","last_updated_timestamp",b"last_updated_timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_timestamp",b"created_timestamp","last_updated_timestamp",b"last_updated_timestamp"]) -> None: ...
global___EntityMeta = EntityMeta