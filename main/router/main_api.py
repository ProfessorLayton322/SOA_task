from pydantic import BaseModel, Field
from typing import Optional
import datetime

from typing_extensions import Annotated
from fastapi import status, Header, APIRouter
from fastapi.responses import JSONResponse

from email_validator import validate_email

from db.db_session import DatabaseSession
from .db_actions import get_user_by_username, get_user_by_id, create_user, update_profile, create_session, authorize, AuthError

import hashlib

router = APIRouter()

class AuthData(BaseModel):
    username: str
    password: str
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

@router.post("/api/signup")
async def register(db: DatabaseSession, signup_data: AuthData):
    user = await get_user_by_username(db, signup_data.username)
    if user is None:
        await create_user(db, signup_data.username, hash_password(signup_data.password))
        return JSONResponse(content={"message" : f"Welcome {signup_data.username}. Signup complete!"}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message" : f"User with username {signup_data.username} already exists!"}, status_code=status.HTTP_409_CONFLICT)

@router.post("/api/login")
async def login(db: DatabaseSession, login_data: AuthData):
    user = await get_user_by_username(db, login_data.username)
    if user is None:
        return JSONResponse(content={"message": f"No such user exists: {login_data.username}"}, status_code=status.HTTP_403_FORBIDDEN)
    if hash_password(login_data.password) != user["hashed_password"]:
        return JSONResponse(content={"message": "Incorrect password"}, status_code=status.HTTP_403_FORBIDDEN)
    session = await create_session(db, user.id, 2)
    return JSONResponse(content={"message": f"Welcome {login_data.username}, login complete!", "session": session}, status_code=status.HTTP_200_OK)

class ProfileData(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    birthdate: Optional[str] = None
    phone: Optional[str] = None

def verify_email(email) -> bool:
    try:
        _ = validate_email(email)
        return True
    except:
        return False

def parse_user_params(profile_data: ProfileData):
    params = {}
    if profile_data.email is not None:
        if not verify_email(profile_data.email):
            return JSONResponse(content={"message": "Incorrect email format"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        params["email"] = profile_data.email
    if profile_data.name is not None:
        params["name"] = profile_data.name
    if profile_data.surname is not None:
        params["surname"] = profile_data.surname
    if profile_data.birthdate is not None:
        birthdate = None
        try:
            birthdate = datetime.datetime.strptime(profile_data.birthdate, "%d %b %Y")
        except:
            return JSONResponse(content={"message": "Wrong birthday datetime, please provide datetime in day-month-year format, like 7 Oct 1900"}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
        params["birthdate"] = birthdate
    if profile_data.phone is not None:
        params["phone"] = profile_data.phone
    return params


def check_auth_error(auth_result):
    if auth_result == AuthError.NoSession:
        return JSONResponse(content={"message": "No session token found, please provide it via 'Authorization' header"}, status_code=status.HTTP_403_FORBIDDEN)
    if auth_result == AuthError.InvalidSession:
        return JSONResponse(content={"message": "Session token is invalid"}, status_code=status.HTTP_403_FORBIDDEN)
    if auth_result == AuthError.ExpiredSession:
        return JSONResponse(content={"message": "Session has expired, please log in once more via /api/login"}, status_code=status.HTTP_403_FORBIDDEN)
    return None

@router.put("/api/update")
async def update_user_profile(db: DatabaseSession, profile_data: ProfileData, authorization: Annotated[str, Header()] = None):
    auth_result = await authorize(db, authorization)
    auth_error = check_auth_error(auth_result)
    if auth_error is not None:
        return auth_error
    user_id = auth_result
    parse_result = parse_user_params(profile_data)
    if isinstance(parse_result, JSONResponse):
        return parse_result
    params = parse_result
    if len(params) > 0:
        await update_profile(db, user_id, params)
        return JSONResponse(content={"message": "Update succesful"}, status_code=status.HTTP_200_OK)
    return JSONResponse(content={"message": "Update succesful. Warning: no update parameters were provided"}, status_code=status.HTTP_200_OK)

@router.get("/api/profile")
async def get_profile(db: DatabaseSession, authorization: Annotated[str, Header()] = None):
    auth_result = await authorize(db, authorization)
    auth_error = check_auth_error(auth_result)
    if auth_error is not None:
        return auth_error
    user_id = auth_result
    user = await get_user_by_id(db, user_id)
    profile_data = {}
    for k, v in user.items():
        if k in {"hashed_password", "id"}:
            continue
        profile_data[k] = str(v)
    return JSONResponse(content=profile_data, status_code=status.HTTP_200_OK)
