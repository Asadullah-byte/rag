import json
from redis import Redis


async def get_cache(redis: Redis, key: str):
    value = await redis.get(key)
    return json.loads(value) if value else None


async def set_cache(redis: Redis, key: str, value, ttl: int = 3600):
    await redis.set(key, json.dumps(value), ex=ttl)


async def delete_cache(redis: Redis, key: str):
    await redis.delete(key)
