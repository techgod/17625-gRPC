# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libraryobjects.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14libraryobjects.proto\x12\x07library\"\xa7\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\"\n\x05genre\x18\x04 \x01(\x0e\x32\x13.library.Book.Genre\x12\x0c\n\x04year\x18\x05 \x01(\x05\"@\n\x05Genre\x12\x0b\n\x07MYSTERY\x10\x00\x12\x0e\n\nNONFICTION\x10\x01\x12\r\n\tBIOGRAPHY\x10\x02\x12\x0b\n\x07\x46\x41NTASY\x10\x03\"\xa5\x01\n\rInventoryItem\x12\x18\n\x10inventory_number\x18\x01 \x01(\x05\x12\x1d\n\x04\x62ook\x18\x02 \x01(\x0b\x32\r.library.BookH\x00\x12-\n\x06status\x18\x03 \x01(\x0e\x32\x1d.library.InventoryItem.Status\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x08\n\x06objectb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'libraryobjects_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=34
  _BOOK._serialized_end=201
  _BOOK_GENRE._serialized_start=137
  _BOOK_GENRE._serialized_end=201
  _INVENTORYITEM._serialized_start=204
  _INVENTORYITEM._serialized_end=369
  _INVENTORYITEM_STATUS._serialized_start=325
  _INVENTORYITEM_STATUS._serialized_end=359
# @@protoc_insertion_point(module_scope)
