# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x03gen\"\x13\n\x11ServerInfoRequest\"\x8a\x01\n\x12ServerInfoResponse\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\x16\n\x0eserver_version\x18\x02 \x01(\t\x12\x15\n\rserver_status\x18\x03 \x01(\t\x12\x19\n\x11server_start_time\x18\x04 \x01(\t\x12\x15\n\rserver_uptime\x18\x05 \x01(\t2L\n\x06Server\x12\x42\n\rGetServerInfo\x12\x16.gen.ServerInfoRequest\x1a\x17.gen.ServerInfoResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SERVERINFOREQUEST']._serialized_start=21
  _globals['_SERVERINFOREQUEST']._serialized_end=40
  _globals['_SERVERINFORESPONSE']._serialized_start=43
  _globals['_SERVERINFORESPONSE']._serialized_end=181
  _globals['_SERVER']._serialized_start=183
  _globals['_SERVER']._serialized_end=259
# @@protoc_insertion_point(module_scope)
