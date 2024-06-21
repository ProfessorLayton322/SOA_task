from os import environ as env
from os import system
from datetime import datetime

import grpc
from proto.content_pb2 import PostId, EditResponse, ReadResponse
from proto import content_pb2_grpc
from concurrent import futures
import asyncio
from google.protobuf.timestamp_pb2 import Timestamp

from db.db_session import SessionLocal
from db.models import posts as post_table

async def get_post(db, post_id):
    query = post_table.select().where(post_table.c.id == post_id)
    result = (await db.execute(query)).mappings().all()
    if len(result) == 0:
        return None
    return result[0]

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

    async def EditPost(self, request, context):
        try:
            db = SessionLocal()
            post = await get_post(db, request.post_id)
            if post is None:
                response = EditResponse()
                response.result = EditResponse.Result.MissingPost
                return response
            if post["user_id"] != request.author_id:
                response = EditResponse()
                response.result = EditResponse.Result.NoPermission
                return response
            timestamp = datetime.now()
            query = post_table.update().where(post_table.c.id == request.post_id).values(
                content=request.new_content,
                edited=timestamp
            )
            await db.execute(query)
            await db.commit()

            response = EditResponse()
            response.result = EditResponse.Result.Ok
            return response
        except Exception as exception:
            await context.abort(grpc.StatusCode.INTERNAL, str(exception))

    async def ReadPost(self, request, context):
        try:
            db = SessionLocal()
            post = await get_post(db, request.post_id)
            if post is None:
                return ReadResponse(status=ReadResponse.Status.MissingPost)
            if post["user_id"] != request.author_id:
                return ReadResponse(status=ReadResponse.Status.NoPermission)
            created = Timestamp()
            created.FromDatetime(post["created"])
            edited = Timestamp()
            edited.FromDatetime(post["edited"])
            return ReadResponse(
                status=ReadResponse.Status.Ok,
                content=post["content"],
                created=created,
                edited=edited
            )
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
