from app.core.logger import log
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from typing import Annotated
from typing import AsyncGenerator
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncAttrs,
)
from app.core.config import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass

engine = create_async_engine(
    url=settings.DATABASE_URL,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=5,
    pool_recycle=1800,
    max_overflow=0,
    pool_pre_ping=True,
    echo=False,
    future=True,
)

async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_db_session)]
