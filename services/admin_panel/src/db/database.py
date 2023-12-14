import contextlib
from typing import Generator

from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.ext.declarative import declarative_base
from src.config import config
from sqlalchemy import create_engine

# Creating a binding to a DB to work with a DB
sync_engine = create_engine(config.sync_alchemy_url)

# Session maker
sync_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=sync_engine))

# Base class object for models class
Base = declarative_base()


# Function to create an Async SQLAlchemy session.
@contextlib.contextmanager
def create_session() -> Generator[Session, None, None]:
    with sync_session() as session:
        yield session