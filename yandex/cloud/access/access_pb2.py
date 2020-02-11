# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/access/access.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/access/access.proto',
  package='yandex.cloud.access',
  syntax='proto3',
  serialized_options=_b('\n\027yandex.cloud.api.accessZ>github.com/yandex-cloud/go-genproto/yandex/cloud/access;access'),
  serialized_pb=_b('\n yandex/cloud/access/access.proto\x12\x13yandex.cloud.access\x1a\x1dyandex/cloud/validation.proto\"-\n\x07Subject\x12\x14\n\x02id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x0c\n\x04type\x18\x02 \x01(\t\"_\n\rAccessBinding\x12\x19\n\x07role_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x33\n\x07subject\x18\x02 \x01(\x0b\x32\x1c.yandex.cloud.access.SubjectB\x04\xe8\xc7\x31\x01\"t\n\x19ListAccessBindingsRequest\x12\x19\n\x0bresource_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"r\n\x1aListAccessBindingsResponse\x12;\n\x0f\x61\x63\x63\x65ss_bindings\x18\x01 \x03(\x0b\x32\".yandex.cloud.access.AccessBinding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"x\n\x18SetAccessBindingsRequest\x12\x19\n\x0bresource_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x41\n\x0f\x61\x63\x63\x65ss_bindings\x18\x02 \x03(\x0b\x32\".yandex.cloud.access.AccessBindingB\x04\xe8\xc7\x31\x01\"0\n\x19SetAccessBindingsMetadata\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\"\x86\x01\n\x1bUpdateAccessBindingsRequest\x12\x19\n\x0bresource_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12L\n\x15\x61\x63\x63\x65ss_binding_deltas\x18\x02 \x03(\x0b\x32\'.yandex.cloud.access.AccessBindingDeltaB\x04\xe8\xc7\x31\x01\"3\n\x1cUpdateAccessBindingsMetadata\x12\x13\n\x0bresource_id\x18\x01 \x01(\t\"\x96\x01\n\x12\x41\x63\x63\x65ssBindingDelta\x12>\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32(.yandex.cloud.access.AccessBindingActionB\x04\xe8\xc7\x31\x01\x12@\n\x0e\x61\x63\x63\x65ss_binding\x18\x02 \x01(\x0b\x32\".yandex.cloud.access.AccessBindingB\x04\xe8\xc7\x31\x01*Q\n\x13\x41\x63\x63\x65ssBindingAction\x12%\n!ACCESS_BINDING_ACTION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x42Y\n\x17yandex.cloud.api.accessZ>github.com/yandex-cloud/go-genproto/yandex/cloud/access;accessb\x06proto3')
  ,
  dependencies=[yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])

_ACCESSBINDINGACTION = _descriptor.EnumDescriptor(
  name='AccessBindingAction',
  full_name='yandex.cloud.access.AccessBindingAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCESS_BINDING_ACTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=981,
  serialized_end=1062,
)
_sym_db.RegisterEnumDescriptor(_ACCESSBINDINGACTION)

AccessBindingAction = enum_type_wrapper.EnumTypeWrapper(_ACCESSBINDINGACTION)
ACCESS_BINDING_ACTION_UNSPECIFIED = 0
ADD = 1
REMOVE = 2



_SUBJECT = _descriptor.Descriptor(
  name='Subject',
  full_name='yandex.cloud.access.Subject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.access.Subject.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.access.Subject.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=133,
)


_ACCESSBINDING = _descriptor.Descriptor(
  name='AccessBinding',
  full_name='yandex.cloud.access.AccessBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='yandex.cloud.access.AccessBinding.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\004<=50'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='yandex.cloud.access.AccessBinding.subject', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=230,
)


_LISTACCESSBINDINGSREQUEST = _descriptor.Descriptor(
  name='ListAccessBindingsRequest',
  full_name='yandex.cloud.access.ListAccessBindingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.access.ListAccessBindingsRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.access.ListAccessBindingsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\372\3071\006<=1000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.access.ListAccessBindingsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\005<=100'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=348,
)


_LISTACCESSBINDINGSRESPONSE = _descriptor.Descriptor(
  name='ListAccessBindingsResponse',
  full_name='yandex.cloud.access.ListAccessBindingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_bindings', full_name='yandex.cloud.access.ListAccessBindingsResponse.access_bindings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.access.ListAccessBindingsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=464,
)


_SETACCESSBINDINGSREQUEST = _descriptor.Descriptor(
  name='SetAccessBindingsRequest',
  full_name='yandex.cloud.access.SetAccessBindingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.access.SetAccessBindingsRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_bindings', full_name='yandex.cloud.access.SetAccessBindingsRequest.access_bindings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=466,
  serialized_end=586,
)


_SETACCESSBINDINGSMETADATA = _descriptor.Descriptor(
  name='SetAccessBindingsMetadata',
  full_name='yandex.cloud.access.SetAccessBindingsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.access.SetAccessBindingsMetadata.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=636,
)


_UPDATEACCESSBINDINGSREQUEST = _descriptor.Descriptor(
  name='UpdateAccessBindingsRequest',
  full_name='yandex.cloud.access.UpdateAccessBindingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.access.UpdateAccessBindingsRequest.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_binding_deltas', full_name='yandex.cloud.access.UpdateAccessBindingsRequest.access_binding_deltas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=639,
  serialized_end=773,
)


_UPDATEACCESSBINDINGSMETADATA = _descriptor.Descriptor(
  name='UpdateAccessBindingsMetadata',
  full_name='yandex.cloud.access.UpdateAccessBindingsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='yandex.cloud.access.UpdateAccessBindingsMetadata.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=826,
)


_ACCESSBINDINGDELTA = _descriptor.Descriptor(
  name='AccessBindingDelta',
  full_name='yandex.cloud.access.AccessBindingDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='yandex.cloud.access.AccessBindingDelta.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_binding', full_name='yandex.cloud.access.AccessBindingDelta.access_binding', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\350\3071\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=829,
  serialized_end=979,
)

_ACCESSBINDING.fields_by_name['subject'].message_type = _SUBJECT
_LISTACCESSBINDINGSRESPONSE.fields_by_name['access_bindings'].message_type = _ACCESSBINDING
_SETACCESSBINDINGSREQUEST.fields_by_name['access_bindings'].message_type = _ACCESSBINDING
_UPDATEACCESSBINDINGSREQUEST.fields_by_name['access_binding_deltas'].message_type = _ACCESSBINDINGDELTA
_ACCESSBINDINGDELTA.fields_by_name['action'].enum_type = _ACCESSBINDINGACTION
_ACCESSBINDINGDELTA.fields_by_name['access_binding'].message_type = _ACCESSBINDING
DESCRIPTOR.message_types_by_name['Subject'] = _SUBJECT
DESCRIPTOR.message_types_by_name['AccessBinding'] = _ACCESSBINDING
DESCRIPTOR.message_types_by_name['ListAccessBindingsRequest'] = _LISTACCESSBINDINGSREQUEST
DESCRIPTOR.message_types_by_name['ListAccessBindingsResponse'] = _LISTACCESSBINDINGSRESPONSE
DESCRIPTOR.message_types_by_name['SetAccessBindingsRequest'] = _SETACCESSBINDINGSREQUEST
DESCRIPTOR.message_types_by_name['SetAccessBindingsMetadata'] = _SETACCESSBINDINGSMETADATA
DESCRIPTOR.message_types_by_name['UpdateAccessBindingsRequest'] = _UPDATEACCESSBINDINGSREQUEST
DESCRIPTOR.message_types_by_name['UpdateAccessBindingsMetadata'] = _UPDATEACCESSBINDINGSMETADATA
DESCRIPTOR.message_types_by_name['AccessBindingDelta'] = _ACCESSBINDINGDELTA
DESCRIPTOR.enum_types_by_name['AccessBindingAction'] = _ACCESSBINDINGACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subject = _reflection.GeneratedProtocolMessageType('Subject', (_message.Message,), {
  'DESCRIPTOR' : _SUBJECT,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.Subject)
  })
_sym_db.RegisterMessage(Subject)

AccessBinding = _reflection.GeneratedProtocolMessageType('AccessBinding', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSBINDING,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.AccessBinding)
  })
_sym_db.RegisterMessage(AccessBinding)

ListAccessBindingsRequest = _reflection.GeneratedProtocolMessageType('ListAccessBindingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCESSBINDINGSREQUEST,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.ListAccessBindingsRequest)
  })
_sym_db.RegisterMessage(ListAccessBindingsRequest)

ListAccessBindingsResponse = _reflection.GeneratedProtocolMessageType('ListAccessBindingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCESSBINDINGSRESPONSE,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.ListAccessBindingsResponse)
  })
_sym_db.RegisterMessage(ListAccessBindingsResponse)

SetAccessBindingsRequest = _reflection.GeneratedProtocolMessageType('SetAccessBindingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETACCESSBINDINGSREQUEST,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.SetAccessBindingsRequest)
  })
_sym_db.RegisterMessage(SetAccessBindingsRequest)

SetAccessBindingsMetadata = _reflection.GeneratedProtocolMessageType('SetAccessBindingsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _SETACCESSBINDINGSMETADATA,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.SetAccessBindingsMetadata)
  })
_sym_db.RegisterMessage(SetAccessBindingsMetadata)

UpdateAccessBindingsRequest = _reflection.GeneratedProtocolMessageType('UpdateAccessBindingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCESSBINDINGSREQUEST,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.UpdateAccessBindingsRequest)
  })
_sym_db.RegisterMessage(UpdateAccessBindingsRequest)

UpdateAccessBindingsMetadata = _reflection.GeneratedProtocolMessageType('UpdateAccessBindingsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEACCESSBINDINGSMETADATA,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.UpdateAccessBindingsMetadata)
  })
_sym_db.RegisterMessage(UpdateAccessBindingsMetadata)

AccessBindingDelta = _reflection.GeneratedProtocolMessageType('AccessBindingDelta', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSBINDINGDELTA,
  '__module__' : 'yandex.cloud.access.access_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.access.AccessBindingDelta)
  })
_sym_db.RegisterMessage(AccessBindingDelta)


DESCRIPTOR._options = None
_SUBJECT.fields_by_name['id']._options = None
_ACCESSBINDING.fields_by_name['role_id']._options = None
_ACCESSBINDING.fields_by_name['subject']._options = None
_LISTACCESSBINDINGSREQUEST.fields_by_name['resource_id']._options = None
_LISTACCESSBINDINGSREQUEST.fields_by_name['page_size']._options = None
_LISTACCESSBINDINGSREQUEST.fields_by_name['page_token']._options = None
_SETACCESSBINDINGSREQUEST.fields_by_name['resource_id']._options = None
_SETACCESSBINDINGSREQUEST.fields_by_name['access_bindings']._options = None
_UPDATEACCESSBINDINGSREQUEST.fields_by_name['resource_id']._options = None
_UPDATEACCESSBINDINGSREQUEST.fields_by_name['access_binding_deltas']._options = None
_ACCESSBINDINGDELTA.fields_by_name['action']._options = None
_ACCESSBINDINGDELTA.fields_by_name['access_binding']._options = None
# @@protoc_insertion_point(module_scope)
