from pydantic import BaseModel, Field
import datetime

from typing_extensions import Annotated
from fastapi import status, Header, APIRouter
from fastapi.responses import JSONResponse

from db.db_session import DatabaseSession
from db.db_actions import get_user_by_username, get_user_by_id, create_user, update_profile, create_session, authorize, AuthError

import hashlib

router = APIRouter()

from os import environ as env
from content_proto.content_pb2_grpc import *
from content_proto.content_pb2 import *
import grpc

grpc_channel = grpc.insecure_channel(env.get("CONTENT_SERVICE_ADDR"))
grpc_stub = ContentServiceStub(grpc_channel)

def check_auth_error(auth_result):
    if auth_result == AuthError.NoSession:
        return JSONResponse(content={"message": "No session token found, please provide it via 'Authorization' header"}, status_code=status.HTTP_403_FORBIDDEN)
    if auth_result == AuthError.InvalidSession:
        return JSONResponse(content={"message": "Session token is invalid"}, status_code=status.HTTP_403_FORBIDDEN)
    if auth_result == AuthError.ExpiredSession:
        return JSONResponse(content={"message": "Session has expired, please log in once more via /api/login"}, status_code=status.HTTP_403_FORBIDDEN)
    return None

class CreateCommentRequest(BaseModel):
    content: str

@router.post("/api/post")
async def create_post(db: DatabaseSession, request: CreateCommentRequest, authorization: Annotated[str, Header()] = None):
    auth_result = await authorize(db, authorization)
    auth_error = check_auth_error(auth_result)
    if auth_error is not None:
        return auth_error
    user_id = auth_result
    response = grpc_stub.CreatePost(CreatePostRequest(
        author_id = user_id,
        content = request.content
    ))
    return JSONResponse(content={"comment_id" : response.post_id}, status_code=status.HTTP_200_OK)

class EditCommentRequest(BaseModel):
    new_content: str
    post_id: int
@router.put("/api/post")
async def create_post(db: DatabaseSession, request: EditCommentRequest, authorization: Annotated[str, Header()] = None):
    auth_result = await authorize(db, authorization)
    auth_error = check_auth_error(auth_result)
    if auth_error is not None:
        return auth_error
    user_id = auth_result
    response = grpc_stub.EditPost(EditPostRequest(
        author_id = user_id,
        post_id = request.post_id,
        new_content = request.new_content
    ))
    if response.result == EditResponse.Result.NoPermission:
        return JSONResponse(content={"message" : "You can't edit other people's posts"}, status_code=status.HTTP_403_FORBIDDEN)
    if response.result == EditResponse.Result.MissingPost:
        return JSONResponse(content={"message" : "Post with this id does not exist"}, status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content={"message" : "Edited successfully"}, status_code=status.HTTP_200_OK)

