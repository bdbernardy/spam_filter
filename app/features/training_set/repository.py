import sys
from fastapi import HTTPException, status
from typing import Optional, List
from bson.objectid import ObjectId
from app.core.mongo_db import MongoDbClient

from .models import TrainingText, TrainingTextInUpdate, TrainingTextInCreate


async def get_all_texts(client: MongoDbClient, skip: Optional[int], limit: Optional[int]) -> List[TrainingText]:
    db = client.get_db()
    cursor = db.trainingSet.find().skip(skip) if skip else db.trainingSet.find()
    texts = await cursor.to_list(length=limit) if limit else await cursor.to_list(sys.maxsize)

    return [TrainingText(**text) for text in texts]


async def get_text(client: MongoDbClient, id: str) -> TrainingText:
    text = await client.get_db().trainingSet.find_one({"_id": ObjectId(id)})
    if not text:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The training text with id '{id}' does not exist."
        )
    return TrainingText(**text)


async def create_text(client: MongoDbClient, text: TrainingTextInCreate) -> TrainingText:
    result = await client.get_db().trainingSet.insert_one(text.dict(by_alias=True))
    create_text = await client.get_db().trainingSet.find_one({"_id": result.inserted_id})
    return TrainingText(**create_text)


async def update_text(client: MongoDbClient, id: str, text: TrainingTextInUpdate) -> TrainingText:
    changes = text.dict(exclude_unset=True, by_alias=True)

    if len(changes) > 0:
        await client.get_db().trainingSet.update_one({"_id": ObjectId(id)}, {"$set": changes})
        updated_text = await client.get_db().trainingSet.find_one({"_id": ObjectId(id)})
        return TrainingText(**updated_text)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="The training text does not have any changes")


async def delete_text(client: MongoDbClient, id: str):
    result = await client.get_db().delete_one({"_id": ObjectId(id)})
    if result.deleted_count != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The training text with id '{id}' does not exist."
        )
