# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/send_encrypted_signature_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/send_encrypted_signature_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nPpogoprotos/networking/platform/responses/send_encrypted_signature_response.proto\x12(pogoprotos.networking.platform.responses\"2\n\x1eSendEncryptedSignatureResponse\x12\x10\n\x08received\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SENDENCRYPTEDSIGNATURERESPONSE = _descriptor.Descriptor(
  name='SendEncryptedSignatureResponse',
  full_name='pogoprotos.networking.platform.responses.SendEncryptedSignatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='received', full_name='pogoprotos.networking.platform.responses.SendEncryptedSignatureResponse.received', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['SendEncryptedSignatureResponse'] = _SENDENCRYPTEDSIGNATURERESPONSE

SendEncryptedSignatureResponse = _reflection.GeneratedProtocolMessageType('SendEncryptedSignatureResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDENCRYPTEDSIGNATURERESPONSE,
  __module__ = 'pogoprotos.networking.platform.responses.send_encrypted_signature_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.SendEncryptedSignatureResponse)
  ))
_sym_db.RegisterMessage(SendEncryptedSignatureResponse)


# @@protoc_insertion_point(module_scope)