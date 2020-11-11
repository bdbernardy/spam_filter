from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.settings import MONGO_CONNECTION_STRING


class MongoDbClient:
    client: AsyncIOMotorClient

    def __init__(self, connection_string):
        self.client = AsyncIOMotorClient(connection_string)

    def get_db(self) -> AsyncIOMotorDatabase:
        return self.client.spamFilter


async def get_mongodb_client():
    return MongoDbClient(MONGO_CONNECTION_STRING)
