from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class ReadPostRequest(_message.Message):
    __slots__ = ("author_id", "post_id")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    post_id: int
    def __init__(self, author_id: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("content", "created", "edited")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELD_NUMBER: _ClassVar[int]
    content: str
    created: _timestamp_pb2.Timestamp
    edited: _timestamp_pb2.Timestamp
    def __init__(self, content: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., edited: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("status", "post")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ok: _ClassVar[ReadResponse.Status]
        MissingPost: _ClassVar[ReadResponse.Status]
        NoPermission: _ClassVar[ReadResponse.Status]
    Ok: ReadResponse.Status
    MissingPost: ReadResponse.Status
    NoPermission: ReadResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    status: ReadResponse.Status
    post: Post
    def __init__(self, status: _Optional[_Union[ReadResponse.Status, str]] = ..., post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class DeletePostRequest(_message.Message):
    __slots__ = ("author_id", "post_id")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    post_id: int
    def __init__(self, author_id: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("result",)
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ok: _ClassVar[DeleteResponse.Result]
        MissingPost: _ClassVar[DeleteResponse.Result]
        NoPermission: _ClassVar[DeleteResponse.Result]
    Ok: DeleteResponse.Result
    MissingPost: DeleteResponse.Result
    NoPermission: DeleteResponse.Result
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: DeleteResponse.Result
    def __init__(self, result: _Optional[_Union[DeleteResponse.Result, str]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("author_id", "page_size", "offset")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    author_id: int
    page_size: int
    offset: int
    def __init__(self, author_id: _Optional[int] = ..., page_size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("posts",)
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[Post]
    def __init__(self, posts: _Optional[_Iterable[_Union[Post, _Mapping]]] = ...) -> None: ...
