from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.settings import MONGO_CONNECTION_STRING


async def get_db() -> AsyncIOMotorDatabase:
    client = await get_client()
    return client.spamFilter


async def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(MONGO_CONNECTION_STRING)
