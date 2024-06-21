from os import environ as env
from os import system
from datetime import datetime

import grpc
from proto.content_pb2 import PostId
from proto import content_pb2_grpc
from concurrent import futures
import asyncio
from google.protobuf.timestamp_pb2 import Timestamp

from db.db_session import SessionLocal
from db.models import posts as post_table

class ContentService(content_pb2_grpc.ContentServiceServicer):
    async def CreatePost(self, request, context):
        try:
            db = SessionLocal()
            timestamp = datetime.now()
            query = post_table.insert().values(
                user_id=request.author_id,
                content=request.content,
                created=timestamp,
                edited=timestamp
            )
            result = await db.execute(query)
            await db.commit()
            return PostId(post_id=result.inserted_primary_key[0])
        except Exception as exception:
            await context.abort(grpc.StatusCode.INTERNAL, str(exception))

PORT = int(env.get("PORT"))

async def serve(port):
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=8))
    content_pb2_grpc.add_ContentServiceServicer_to_server(ContentService(), server)
    server.add_insecure_port("0.0.0.0:" + str(port))
    await server.start()
    await server.wait_for_termination()

system("alembic revision --autogenerate -m \"Init tables\"")
system("alembic upgrade head")
asyncio.run(serve(PORT))
