from motor.motor_asyncio import AsyncIOMotorClient as MongoDbClient
from app.core.settings import MONGO_CONNECTION_STRING


async def get_client() -> MongoDbClient:
    return MongoDbClient(MONGO_CONNECTION_STRING)
