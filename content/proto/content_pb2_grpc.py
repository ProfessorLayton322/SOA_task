# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import content_pb2 as content__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in content_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ContentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/content_service.ContentService/CreatePost',
                request_serializer=content__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=content__pb2.PostId.FromString,
                _registered_method=True)
        self.EditPost = channel.unary_unary(
                '/content_service.ContentService/EditPost',
                request_serializer=content__pb2.EditPostRequest.SerializeToString,
                response_deserializer=content__pb2.EditResponse.FromString,
                _registered_method=True)


class ContentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ContentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=content__pb2.CreatePostRequest.FromString,
                    response_serializer=content__pb2.PostId.SerializeToString,
            ),
            'EditPost': grpc.unary_unary_rpc_method_handler(
                    servicer.EditPost,
                    request_deserializer=content__pb2.EditPostRequest.FromString,
                    response_serializer=content__pb2.EditResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'content_service.ContentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('content_service.ContentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ContentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/content_service.ContentService/CreatePost',
            content__pb2.CreatePostRequest.SerializeToString,
            content__pb2.PostId.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EditPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/content_service.ContentService/EditPost',
            content__pb2.EditPostRequest.SerializeToString,
            content__pb2.EditResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
