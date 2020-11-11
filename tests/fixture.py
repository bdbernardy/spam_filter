from app.core.mongo_db import MongoDbClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.settings import MONGO_CONNECTION_STRING


class TestClient(MongoDbClient):
    def get_db(self) -> AsyncIOMotorDatabase:
        return self.client.spamFilterTests


async def clear_database(db: AsyncIOMotorDatabase):
    await db.trainingSet.delete_many({})


async def get_test_mongodb_client():
    return TestClient(MONGO_CONNECTION_STRING)
