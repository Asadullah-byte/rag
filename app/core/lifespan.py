from app.core.exceptions import CustomExceptionCode
from api_exception import APIException
from app.infrastructure.cache.client import get_redis_client
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.logger import log
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        log.info("Starting application...", project=settings.PROJECT_NAME)
        redis = await get_redis_client()
        yield
        await redis.close()
        log.info("Shutting down application...", project=settings.PROJECT_NAME)
    except Exception:
        log.exception("Lifespan initialization failed", project=settings.PROJECT_NAME)
        raise
    finally:
        log.info("Application shutdown complete", project=settings.PROJECT_NAME)
