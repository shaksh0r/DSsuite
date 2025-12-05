from contextlib import asynccontextmanager
from fastapi import Request
from redis.asyncio import Redis

async def create_redis_client():
    return Redis.from_url("redis://localhost:6379",
                          decode_responses=True,
                          max_connections=10,
                          socket_timeout=3,
                          socket_connect_timeout=3,
                          health_check_interval=30
                          )


async def get_redis(request:Request):
    return request.app.state.redis



@asynccontextmanager
async def redis_lifespan(app):
    app.state.redis  = await create_redis_client()
    try:
        yield
    finally:
        await app.state.redis.aclose()