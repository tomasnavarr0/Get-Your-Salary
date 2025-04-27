from typing import Any
from sqlmodel import SQLModel, select
from app.settings import Settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class DBService:

    async def initialize(self):
        self.engine = create_async_engine(
            f"mysql+aiomysql://{Settings.USER_DB}:{Settings.PASSWORD_DB}@" f"{Settings.HOST_DB}:{Settings.PORT_DB}/{Settings.DATABASE_NAME}",
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_pre_ping=True,
            echo=True,
        )
        self.async_session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def add_data(self, instance: SQLModel, id_name: str = "id") -> str | None:
        await self.initialize()
        async with self.async_session() as session:
            async with session.begin():
                session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return getattr(instance, id_name, None)

    async def get_data(self, get_by: Any, sql_model: SQLModel, field: str = "id") -> list[SQLModel] | None:
        await self.initialize()
        async with self.async_session() as session:
            statement = select(sql_model).where(getattr(sql_model, field) == get_by)
            result = await session.execute(statement)
            return result.scalars().all()

    async def get_first_data(self, get_by: Any, sql_model: SQLModel, field: str = "id") -> SQLModel:
        await self.initialize()
        async with self.async_session() as session:
            statement = select(sql_model).where(getattr(sql_model, field) == get_by)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_last_data_by_field(self, get_by: Any, sql_model: SQLModel, order_field: str, field: str = "id") -> SQLModel:
        await self.initialize()
        async with self.async_session() as session:
            statement = select(sql_model).where(getattr(sql_model, field) == get_by).order_by(getattr(sql_model, order_field).desc()).limit(1)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_last_data(self, sql_model: SQLModel, order_field: str) -> SQLModel:
        await self.initialize()
        async with self.async_session() as session:
            statement = select(sql_model).order_by(getattr(sql_model, order_field).desc()).limit(1)
            result = await session.execute(statement)
            return result.scalars().first()

    async def get_all_data(self, sql_model: SQLModel) -> list[SQLModel]:
        await self.initialize()
        async with self.async_session() as session:
            statement = select(sql_model)
            result = await session.execute(statement)
            return result.scalars().all()

    async def edit_data(self, edit_by: Any, update_data: dict[str, Any], sql_model: SQLModel) -> None:
        await self.initialize()
        async with self.async_session() as session:
            instance = await session.get(sql_model, edit_by)
            if instance:
                for key, value in update_data.items():
                    setattr(instance, key, value)
                session.add(instance)
                await session.commit()
                await session.refresh(instance)
            else:
                raise ValueError(f"No se encontró el registro con el identificador: {edit_by}")

    async def remove_data(self, remove_by: Any, sql_model: SQLModel) -> None:
        await self.initialize()
        async with self.async_session() as session:
            instance = await session.get(sql_model, remove_by)
            if instance:
                await session.delete(instance)
                await session.commit()
            else:
                raise ValueError(f"No se encontró el registro con el identificador: {remove_by}")
