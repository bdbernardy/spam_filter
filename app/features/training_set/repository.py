import sys
from typing import Optional, List
from motor.motor_asyncio import AsyncIOMotorClient as MongoDbClient


from .models import TrainingText, TrainingTextInUpdate, TrainingTextInCreate


async def get_all_texts(client: MongoDbClient, skip: Optional[int], limit: Optional[int]) -> List[TrainingText]:
    db = client.spamFilter
    cursor = db.trainingSet.find().skip(skip) if skip != None else db.trainingSet.find()
    texts = await cursor.to_list(length=limit) if limit != None else await cursor.to_list(sys.maxsize)

    return [TrainingText(**text) for text in texts]


async def create_text(client: MongoDbClient, text: TrainingTextInCreate) -> TrainingText:
    db = client.spamFilter
    result = await db.trainingSet.insert_one(text.dict(by_alias=True))
    return await db.trainingSet.find_one({"_id": result.inserted_id})
