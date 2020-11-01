from app.core.mongo_db import get_client


async def clear_database(db):
    await db.trainingSet.delete_many({})


async def get_test_db():
    client = await get_client()
    return client.spamFilterTests
