# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/types/Value.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x66\x65\x61st/types/Value.proto\x12\x0b\x66\x65\x61st.types\"\x97\x02\n\tValueType\"\x89\x02\n\x04\x45num\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x42YTES\x10\x01\x12\n\n\x06STRING\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\n\n\x06\x44OUBLE\x10\x05\x12\t\n\x05\x46LOAT\x10\x06\x12\x08\n\x04\x42OOL\x10\x07\x12\x12\n\x0eUNIX_TIMESTAMP\x10\x08\x12\x0e\n\nBYTES_LIST\x10\x0b\x12\x0f\n\x0bSTRING_LIST\x10\x0c\x12\x0e\n\nINT32_LIST\x10\r\x12\x0e\n\nINT64_LIST\x10\x0e\x12\x0f\n\x0b\x44OUBLE_LIST\x10\x0f\x12\x0e\n\nFLOAT_LIST\x10\x10\x12\r\n\tBOOL_LIST\x10\x11\x12\x17\n\x13UNIX_TIMESTAMP_LIST\x10\x12\x12\x08\n\x04NULL\x10\x13\"\x82\x05\n\x05Value\x12\x13\n\tbytes_val\x18\x01 \x01(\x0cH\x00\x12\x14\n\nstring_val\x18\x02 \x01(\tH\x00\x12\x13\n\tint32_val\x18\x03 \x01(\x05H\x00\x12\x13\n\tint64_val\x18\x04 \x01(\x03H\x00\x12\x14\n\ndouble_val\x18\x05 \x01(\x01H\x00\x12\x13\n\tfloat_val\x18\x06 \x01(\x02H\x00\x12\x12\n\x08\x62ool_val\x18\x07 \x01(\x08H\x00\x12\x1c\n\x12unix_timestamp_val\x18\x08 \x01(\x03H\x00\x12\x30\n\x0e\x62ytes_list_val\x18\x0b \x01(\x0b\x32\x16.feast.types.BytesListH\x00\x12\x32\n\x0fstring_list_val\x18\x0c \x01(\x0b\x32\x17.feast.types.StringListH\x00\x12\x30\n\x0eint32_list_val\x18\r \x01(\x0b\x32\x16.feast.types.Int32ListH\x00\x12\x30\n\x0eint64_list_val\x18\x0e \x01(\x0b\x32\x16.feast.types.Int64ListH\x00\x12\x32\n\x0f\x64ouble_list_val\x18\x0f \x01(\x0b\x32\x17.feast.types.DoubleListH\x00\x12\x30\n\x0e\x66loat_list_val\x18\x10 \x01(\x0b\x32\x16.feast.types.FloatListH\x00\x12.\n\rbool_list_val\x18\x11 \x01(\x0b\x32\x15.feast.types.BoolListH\x00\x12\x39\n\x17unix_timestamp_list_val\x18\x12 \x01(\x0b\x32\x16.feast.types.Int64ListH\x00\x12%\n\x08null_val\x18\x13 \x01(\x0e\x32\x11.feast.types.NullH\x00\x42\x05\n\x03val\"\x18\n\tBytesList\x12\x0b\n\x03val\x18\x01 \x03(\x0c\"\x19\n\nStringList\x12\x0b\n\x03val\x18\x01 \x03(\t\"\x18\n\tInt32List\x12\x0b\n\x03val\x18\x01 \x03(\x05\"\x18\n\tInt64List\x12\x0b\n\x03val\x18\x01 \x03(\x03\"\x19\n\nDoubleList\x12\x0b\n\x03val\x18\x01 \x03(\x01\"\x18\n\tFloatList\x12\x0b\n\x03val\x18\x01 \x03(\x02\"\x17\n\x08\x42oolList\x12\x0b\n\x03val\x18\x01 \x03(\x08\"0\n\rRepeatedValue\x12\x1f\n\x03val\x18\x01 \x03(\x0b\x32\x12.feast.types.Value*\x10\n\x04Null\x12\x08\n\x04NULL\x10\x00\x42Q\n\x11\x66\x65\x61st.proto.typesB\nValueProtoZ0github.com/feast-dev/feast/go/protos/feast/typesb\x06proto3')

_NULL = DESCRIPTOR.enum_types_by_name['Null']
Null = enum_type_wrapper.EnumTypeWrapper(_NULL)
NULL = 0


_VALUETYPE = DESCRIPTOR.message_types_by_name['ValueType']
_VALUE = DESCRIPTOR.message_types_by_name['Value']
_BYTESLIST = DESCRIPTOR.message_types_by_name['BytesList']
_STRINGLIST = DESCRIPTOR.message_types_by_name['StringList']
_INT32LIST = DESCRIPTOR.message_types_by_name['Int32List']
_INT64LIST = DESCRIPTOR.message_types_by_name['Int64List']
_DOUBLELIST = DESCRIPTOR.message_types_by_name['DoubleList']
_FLOATLIST = DESCRIPTOR.message_types_by_name['FloatList']
_BOOLLIST = DESCRIPTOR.message_types_by_name['BoolList']
_REPEATEDVALUE = DESCRIPTOR.message_types_by_name['RepeatedValue']
_VALUETYPE_ENUM = _VALUETYPE.enum_types_by_name['Enum']
ValueType = _reflection.GeneratedProtocolMessageType('ValueType', (_message.Message,), {
  'DESCRIPTOR' : _VALUETYPE,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.ValueType)
  })
_sym_db.RegisterMessage(ValueType)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Value)
  })
_sym_db.RegisterMessage(Value)

BytesList = _reflection.GeneratedProtocolMessageType('BytesList', (_message.Message,), {
  'DESCRIPTOR' : _BYTESLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.BytesList)
  })
_sym_db.RegisterMessage(BytesList)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.StringList)
  })
_sym_db.RegisterMessage(StringList)

Int32List = _reflection.GeneratedProtocolMessageType('Int32List', (_message.Message,), {
  'DESCRIPTOR' : _INT32LIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Int32List)
  })
_sym_db.RegisterMessage(Int32List)

Int64List = _reflection.GeneratedProtocolMessageType('Int64List', (_message.Message,), {
  'DESCRIPTOR' : _INT64LIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Int64List)
  })
_sym_db.RegisterMessage(Int64List)

DoubleList = _reflection.GeneratedProtocolMessageType('DoubleList', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLELIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.DoubleList)
  })
_sym_db.RegisterMessage(DoubleList)

FloatList = _reflection.GeneratedProtocolMessageType('FloatList', (_message.Message,), {
  'DESCRIPTOR' : _FLOATLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.FloatList)
  })
_sym_db.RegisterMessage(FloatList)

BoolList = _reflection.GeneratedProtocolMessageType('BoolList', (_message.Message,), {
  'DESCRIPTOR' : _BOOLLIST,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.BoolList)
  })
_sym_db.RegisterMessage(BoolList)

RepeatedValue = _reflection.GeneratedProtocolMessageType('RepeatedValue', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDVALUE,
  '__module__' : 'feast.types.Value_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.RepeatedValue)
  })
_sym_db.RegisterMessage(RepeatedValue)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021feast.proto.typesB\nValueProtoZ0github.com/feast-dev/feast/go/protos/feast/types'
  _NULL._serialized_start=1200
  _NULL._serialized_end=1216
  _VALUETYPE._serialized_start=41
  _VALUETYPE._serialized_end=320
  _VALUETYPE_ENUM._serialized_start=55
  _VALUETYPE_ENUM._serialized_end=320
  _VALUE._serialized_start=323
  _VALUE._serialized_end=965
  _BYTESLIST._serialized_start=967
  _BYTESLIST._serialized_end=991
  _STRINGLIST._serialized_start=993
  _STRINGLIST._serialized_end=1018
  _INT32LIST._serialized_start=1020
  _INT32LIST._serialized_end=1044
  _INT64LIST._serialized_start=1046
  _INT64LIST._serialized_end=1070
  _DOUBLELIST._serialized_start=1072
  _DOUBLELIST._serialized_end=1097
  _FLOATLIST._serialized_start=1099
  _FLOATLIST._serialized_end=1123
  _BOOLLIST._serialized_start=1125
  _BOOLLIST._serialized_end=1148
  _REPEATEDVALUE._serialized_start=1150
  _REPEATEDVALUE._serialized_end=1198
# @@protoc_insertion_point(module_scope)