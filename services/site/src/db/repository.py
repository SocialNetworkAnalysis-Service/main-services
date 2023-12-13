from abc import ABC, abstractmethod
from typing import Any, Hashable

from sqlalchemy import delete, exc, insert, select, update

from src.db.database import create_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict[Hashable, Any]):
        raise NotImplementedError

    @abstractmethod
    async def find_all_by_filter(self, **filter_by):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict[Hashable, Any]) -> int:
        async with create_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar()

    async def find_all_by_filter(self, **filter_by):
        async with create_session() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            return [row[0].to_read_model() for row in res.all()]

    async def find_one(self, **filter_by):
        async with create_session() as session:
            stmt = select(self.model).filter_by(**filter_by)
            res = await session.execute(stmt)
            try:
                return res.scalar_one().to_read_model()
            except exc.NoResultFound:
                return None

    async def update_by_id(self, id_, **new_data):
        async with create_session() as session:
            stmt = update(self.model).where(self.model.id == id_).values(**new_data)
            await session.execute(stmt)

            await session.commit()

    async def delete_one(self, **filter_by):
        async with create_session() as session:
            stmt = delete(self.model).filter_by(**filter_by)
            await session.execute(stmt)
            await session.commit()
