import os
import sys
# Add current directory to path to use relative path for imports
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import libraryobjects_pb2 as _libraryobjects_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _libraryobjects_pb2.Book
    def __init__(self, book: _Optional[_Union[_libraryobjects_pb2.Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _libraryobjects_pb2.Book
    def __init__(self, book: _Optional[_Union[_libraryobjects_pb2.Book, _Mapping]] = ...) -> None: ...
