from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import settings


def create_url() -> URL:
    db = settings.database

    if db.driver == "sqlite+aiosqlite":
        return URL.create(drivername=db.driver, database=f"{db.name}.sqlite")

    return URL.create(
        drivername=db.driver,
        username=db.username,
        password=db.password,
        host=db.host,
        port=db.port,
        database=db.name,
    )


engine = create_async_engine(
    url=create_url(),
    echo=True,
)

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
