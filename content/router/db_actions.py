from db.db_session import DatabaseSession
from db.models import users as user_table
from db.models import sessions as session_table

from typing import Union

import datetime
import os
from enum import Enum

async def get_user_by_username(db: DatabaseSession, username : str):
    query = user_table.select().where(user_table.c.username == username)
    result = (await db.execute(query)).mappings().all()
    if len(result) == 0:
        return None
    return result[0] 

async def get_user_by_id(db: DatabaseSession, id):
    query = user_table.select().where(user_table.c.id == id)
    result = (await db.execute(query)).mappings().all()
    if len(result) == 0:
        return None
    return result[0] 

async def create_user(db: DatabaseSession, username: str, password: str):
    query = user_table.insert().values(
        username=username, 
        hashed_password=password
    )
    await db.execute(query)
    await db.commit()

async def update_profile(db: DatabaseSession, user_id, params):
    query = user_table.update().where(user_table.c.id == user_id).values(**params)
    await db.execute(query)
    await db.commit()

async def create_session(db: DatabaseSession, user_id, hours_duration = 2):
    expires = datetime.datetime.utcnow() + datetime.timedelta(hours=hours_duration)
    session = os.urandom(20).hex()
    query = session_table.insert().values(
        session=session,
        expires=expires,
        user_id=user_id
    )
    await db.execute(query)
    await db.commit()
    return session

class AuthError(Enum):
    NoSession = 1
    InvalidSession = 2
    ExpiredSession = 3

async def authorize(db: DatabaseSession, sessionString):
    if sessionString is None:
        return AuthError.NoSession
    query = session_table.select().where(session_table.c.session == sessionString)
    result = (await db.execute(query)).mappings().all()
    if len(result) == 0:
        return AuthError.InvalidSession
    session = result[0]
    if datetime.datetime.utcnow() > session.expires:
        return AuthError.ExpiredSession
    query = user_table.select().where(user_table.c.id == session.user_id)
    return (await db.execute(query)).mappings().all()[0].id
