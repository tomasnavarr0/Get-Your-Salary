from dataclasses import dataclass
from sqlalchemy.engine import Engine
from sqlalchemy import inspect
from app.settings import Settings
from sqlmodel import SQLModel, create_engine
from sqlalchemy.sql import text
from .models import *  # noqa: F403, F401


@dataclass
class DBManager:
    engine: Engine = create_engine(
        f"mysql+pymysql://{Settings.USER_DB}:{Settings.PASSWORD_DB}@" f"{Settings.HOST_DB}:{Settings.PORT_DB}/{Settings.DATABASE_NAME}",
        pool_size=5,
        max_overflow=10,
        pool_timeout=30,
        pool_pre_ping=True,
    )

    def create_tables(self) -> str:
        SQLModel.metadata.create_all(self.engine)
        return "Tables created successfully"

    def drop_table(self, table_name: str) -> str:
        with self.engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))
        return f"Table '{table_name}' dropped successfully."

    def list_tables(self) -> list[str]:
        inspector = inspect(self.engine)
        return inspector.get_table_names()
