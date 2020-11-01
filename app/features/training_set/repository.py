import sys
from fastapi import HTTPException, status
from typing import Optional, List
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient as MongoDbClient


from .models import TrainingText, TrainingTextInUpdate, TrainingTextInCreate


async def get_all_texts(client: MongoDbClient, skip: Optional[int], limit: Optional[int]) -> List[TrainingText]:
    db = client.spamFilter
    cursor = db.trainingSet.find().skip(skip) if skip != None else db.trainingSet.find()
    texts = await cursor.to_list(length=limit) if limit != None else await cursor.to_list(sys.maxsize)

    return [TrainingText(**text) for text in texts]


async def get_text(client: MongoDbClient, id: str) -> TrainingText:
    db = client.spamFilter
    text = await db.trainingSet.find_one({"_id": ObjectId(id)})
    if text == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The training text with id '{id}' does not exist."
        )
    return TrainingText(**text)


async def create_text(client: MongoDbClient, text: TrainingTextInCreate) -> TrainingText:
    db = client.spamFilter
    result = await db.trainingSet.insert_one(text.dict(by_alias=True))
    create_text = await db.trainingSet.find_one({"_id": result.inserted_id})
    return TrainingText(**create_text)


async def update_text(client: MongoDbClient, id: str, text: TrainingTextInUpdate) -> TrainingText:
    db = client.spamFilter
    changes = text.dict(exclude_unset=True, by_alias=True)

    if len(changes) > 0:
        await db.trainingSet.update_one({"_id": ObjectId(id)}, {"$set": changes})
        updated_text = await db.trainingSet.find_one({"_id": ObjectId(id)})
        return TrainingText(**updated_text)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The training text does not have any changes")


async def delete_text(client: MongoDbClient, id: str):
    db = client.spamFilter
    result = await db.trainingSet.delete_one({"_id": ObjectId(id)})
    if result.deleted_count != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The training text with id '{id}' does not exist."
        )
