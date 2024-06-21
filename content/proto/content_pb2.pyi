from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePostRequest(_message.Message):
    __slots__ = ("author_id", "content")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    content: str
    def __init__(self, author_id: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...

class PostId(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...
