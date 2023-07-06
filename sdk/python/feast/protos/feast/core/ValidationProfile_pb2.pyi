"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GEValidationProfiler(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class UserDefinedProfiler(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        BODY_FIELD_NUMBER: builtins.int
        body: builtins.bytes = ...
        """The python-syntax function body (serialized by dill)"""

        def __init__(self,
            *,
            body : builtins.bytes = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["body",b"body"]) -> None: ...

    PROFILER_FIELD_NUMBER: builtins.int
    @property
    def profiler(self) -> global___GEValidationProfiler.UserDefinedProfiler: ...
    def __init__(self,
        *,
        profiler : typing.Optional[global___GEValidationProfiler.UserDefinedProfiler] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["profiler",b"profiler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["profiler",b"profiler"]) -> None: ...
global___GEValidationProfiler = GEValidationProfiler

class GEValidationProfile(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXPECTATION_SUITE_FIELD_NUMBER: builtins.int
    expectation_suite: builtins.bytes = ...
    """JSON-serialized ExpectationSuite object"""

    def __init__(self,
        *,
        expectation_suite : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["expectation_suite",b"expectation_suite"]) -> None: ...
global___GEValidationProfile = GEValidationProfile

class ValidationReference(google.protobuf.message.Message):
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
    REFERENCE_DATASET_NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    GE_PROFILER_FIELD_NUMBER: builtins.int
    GE_PROFILE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """Unique name of validation reference within the project"""

    reference_dataset_name: typing.Text = ...
    """Name of saved dataset used as reference dataset"""

    project: typing.Text = ...
    """Name of Feast project that this object source belongs to"""

    description: typing.Text = ...
    """Description of the validation reference"""

    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]:
        """User defined metadata"""
        pass
    @property
    def ge_profiler(self) -> global___GEValidationProfiler: ...
    @property
    def ge_profile(self) -> global___GEValidationProfile: ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        reference_dataset_name : typing.Text = ...,
        project : typing.Text = ...,
        description : typing.Text = ...,
        tags : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ge_profiler : typing.Optional[global___GEValidationProfiler] = ...,
        ge_profile : typing.Optional[global___GEValidationProfile] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["cached_profile",b"cached_profile","ge_profile",b"ge_profile","ge_profiler",b"ge_profiler","profiler",b"profiler"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cached_profile",b"cached_profile","description",b"description","ge_profile",b"ge_profile","ge_profiler",b"ge_profiler","name",b"name","profiler",b"profiler","project",b"project","reference_dataset_name",b"reference_dataset_name","tags",b"tags"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["cached_profile",b"cached_profile"]) -> typing.Optional[typing_extensions.Literal["ge_profile"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["profiler",b"profiler"]) -> typing.Optional[typing_extensions.Literal["ge_profiler"]]: ...
global___ValidationReference = ValidationReference
