from redis.asyncio import ConnectionPool
from app.core.config import settings
from redis.asyncio import Redis

_redis: Redis | None = None


async def get_redis_client() -> Redis:
    global _redis
    if _redis is None:
        conntection_pool = ConnectionPool.from_url(
            settings.REDIS_URL, decode_responses=True
        )
        _redis = Redis.from_pool(conntection_pool)
    return _redis
