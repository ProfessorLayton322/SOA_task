# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: content.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcontent.proto\x12\x0f\x63ontent_service\x1a\x1fgoogle/protobuf/timestamp.proto\"7\n\x11\x43reatePostRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\x04\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\x19\n\x06PostId\x12\x0f\n\x07post_id\x18\x01 \x01(\x04\"J\n\x0f\x45\x64itPostRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\x04\x12\x0f\n\x07post_id\x18\x02 \x01(\x04\x12\x13\n\x0bnew_content\x18\x03 \x01(\t\"y\n\x0c\x45\x64itResponse\x12\x34\n\x06result\x18\x01 \x01(\x0e\x32$.content_service.EditResponse.Result\"3\n\x06Result\x12\x06\n\x02Ok\x10\x00\x12\x0f\n\x0bMissingPost\x10\x01\x12\x10\n\x0cNoPermission\x10\x02\x32\xac\x01\n\x0e\x43ontentService\x12K\n\nCreatePost\x12\".content_service.CreatePostRequest\x1a\x17.content_service.PostId\"\x00\x12M\n\x08\x45\x64itPost\x12 .content_service.EditPostRequest\x1a\x1d.content_service.EditResponse\"\x00\x42\x18Z\x16proto/;content_serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\026proto/;content_service'
  _globals['_CREATEPOSTREQUEST']._serialized_start=67
  _globals['_CREATEPOSTREQUEST']._serialized_end=122
  _globals['_POSTID']._serialized_start=124
  _globals['_POSTID']._serialized_end=149
  _globals['_EDITPOSTREQUEST']._serialized_start=151
  _globals['_EDITPOSTREQUEST']._serialized_end=225
  _globals['_EDITRESPONSE']._serialized_start=227
  _globals['_EDITRESPONSE']._serialized_end=348
  _globals['_EDITRESPONSE_RESULT']._serialized_start=297
  _globals['_EDITRESPONSE_RESULT']._serialized_end=348
  _globals['_CONTENTSERVICE']._serialized_start=351
  _globals['_CONTENTSERVICE']._serialized_end=523
# @@protoc_insertion_point(module_scope)
