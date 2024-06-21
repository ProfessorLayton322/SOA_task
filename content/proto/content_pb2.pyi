from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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

class EditPostRequest(_message.Message):
    __slots__ = ("author_id", "post_id", "new_content")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    post_id: int
    new_content: str
    def __init__(self, author_id: _Optional[int] = ..., post_id: _Optional[int] = ..., new_content: _Optional[str] = ...) -> None: ...

class EditResponse(_message.Message):
    __slots__ = ("result",)
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ok: _ClassVar[EditResponse.Result]
        MissingPost: _ClassVar[EditResponse.Result]
        NoPermission: _ClassVar[EditResponse.Result]
    Ok: EditResponse.Result
    MissingPost: EditResponse.Result
    NoPermission: EditResponse.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: EditResponse.Result
    def __init__(self, result: _Optional[_Union[EditResponse.Result, str]] = ...) -> None: ...
