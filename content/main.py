from os import environ as env
from os import system
from datetime import datetime

import grpc
from proto.content_pb2 import Post, PostId, EditResponse, ReadResponse, DeleteResponse, ListResponse
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

def dict_to_proto(post):
    created = Timestamp()
    created.FromDatetime(post["created"])
    edited = Timestamp()
    edited.FromDatetime(post["edited"])
    return Post(
        content=post["content"],
        created=created,
        edited=edited
    )

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

    async def DeletePost(self, request, context):
        try:
            db = SessionLocal()
            post = await get_post(db, request.post_id)
            if post is None:
                response = DeleteResponse()
                response.result = DeleteResponse.Result.MissingPost
                return response
            if post["user_id"] != request.author_id:
                response = DeleteResponse()
                response.result = DeleteResponse.Result.NoPermission
                return response
            query = post_table.delete().where(post_table.c.id == request.post_id)
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
            return ReadResponse(
                status=ReadResponse.Status.Ok,
                post=dict_to_proto(post)
            )
        except Exception as exception:
            await context.abort(grpc.StatusCode.INTERNAL, str(exception))

    async def List(self, request, context):
        try:
            db = SessionLocal()
            posts = post_table.select().where(post_table.c.user_id == request.author_id).order_by(
                post_table.c.edited.desc()).offset(request.offset).limit(request.page_size)
            result = (await db.execute(posts)).mappings().all()
            response = ListResponse()
            for post in result:
                response.posts.append(dict_to_proto(post))
            return response
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
