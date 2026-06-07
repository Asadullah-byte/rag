from fastapi import Depends
from redis.asyncio import Redis
from app.infrastructure.cache.client import get_redis_client


async def get_cache(redis: Redis = Depends(get_redis_client)) -> Redis:
    return redis
