from os import environ as env
from os import system

import grpc
from proto import content_pb2
from proto import content_pb2_grpc
from concurrent import futures
import asyncio
from google.protobuf.timestamp_pb2 import Timestamp

class ContentService(content_pb2_grpc.ContentServiceServicer):
    async def CreatePost(self, request, context):
        print(request.author_id, request.content)
        return content_pb2.PostId(post_id=0)


async def serve():
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=8))
    content_pb2_grpc.add_ContentServiceServicer_to_server(ContentService(), server)
    server.add_insecure_port("0.0.0.0:" + PORT)
    await server.start()
    print(f"Content service is active on port {PORT}")
    await server.wait_for_termination()

PORT = int(env.get("PORT"))

system("alembic revision --autogenerate -m \"Init tables\"")
system("alembic upgrade head")
asyncio.run(serve())
