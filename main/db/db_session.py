from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from os import environ
from typing_extensions import Annotated
from fastapi import Depends

DATABASE_URL = environ.get("POSTGRES_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False, class_=AsyncSession)


async def make_session():
    async with SessionLocal() as session:
        yield session


DatabaseSession = Annotated[AsyncSession, Depends(make_session)]
