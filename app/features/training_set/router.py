from fastapi import APIRouter, Query, Path, Depends, status
from typing import List, Optional, Text
from motor.motor_asyncio import AsyncIOMotorClient as MongoDbClient

from app.core.mongo_db import get_client
from .models import TrainingText, TrainingTextInCreate, TrainingTextInUpdate
from .repository import get_all_texts, create_text

router = APIRouter()


@router.get("/", response_model=List[TrainingText])
async def get_all(
    skip: Optional[int] = Query(
        None,
        description="The number of texts to skip",
        ge=0
    ),
    limit: Optional[int] = Query(
        None,
        description="The maximum number of texts to fetch from the training set",
        gt=0
    ),
    client: MongoDbClient = Depends(get_client)
):
    return await get_all_texts(client, skip, limit)


@router.post("/", response_model=TrainingText, status_code=status.HTTP_201_CREATED, summary="Adds a new text to the training set.")
async def add(
        text: TrainingTextInCreate,
        client: MongoDbClient = Depends(get_client)):
    """
    Add a text to the training set with all the information:

    - **text**: the text to be used when training the spam filter
    - **is_spam**: indicates whether the text is a spam or not
    """
    return await create_text(client, text)


@router.get("/{id}", response_model=TrainingText)
async def get(
    id: str = Path(..., description="The id of the text to fetch."),
    client: MongoDbClient = Depends(get_client)
):
    raise Exception("Not implemented")


@router.delete("/{id}")
async def delete(
    id: str = Path(..., description="The id of the text to delete."),
    client: MongoDbClient = Depends(get_client)
):
    raise Exception("Not implemented")


@router.put("/{id}", response_model=TrainingText)
async def update(
    Text: TrainingTextInUpdate,
    id: str = Path(..., description="The id of the text to updated."),
    client: MongoDbClient = Depends(get_client)
):
    raise Exception("Not implemented")
