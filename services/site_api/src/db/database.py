import contextlib
from typing import Any, AsyncGenerator

from sqlalchemy import JSON
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from src.config_reader import config

# Creating a binding to a DB to work with a DB
async_engine = create_async_engine(config.async_alchemy_url)

# Session maker
async_session_factory = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


# Base class object for models class
class Base(DeclarativeBase):
    type_annotation_map = {dict[str, Any]: JSON}


# Function to create an Async SQLAlchemy session.
@contextlib.asynccontextmanager
async def create_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
