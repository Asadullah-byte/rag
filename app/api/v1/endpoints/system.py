from fastapi import APIRouter
from app.infrastructure.cache.client import get_redis_client
from app.infrastructure.db.session import async_session
from sqlalchemy import text
from app.core.config import settings

router = APIRouter()


@router.get("/", tags=["system"])
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}", "project": settings.PROJECT_NAME}


@router.get("/health", tags=["system"])
async def health_check():
    status = {"status": "ok", "services": {}}
    # Redis check
    try:
        redis = await get_redis_client()
        pong = await redis.ping()
        status["services"]["redis"] = "ok" if pong else "unreachable"
        await redis.close()
    except Exception as e:
        status["services"]["redis"] = f"error: {e}"

    # DB check
    try:
        async with async_session() as session:
            await session.execute(text("SELECT 1"))
            status["services"]["db"] = "ok"
    except Exception as e:
        status["services"]["db"] = f"error: {e}"

    return status
