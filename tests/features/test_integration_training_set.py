import pytest
from httpx import AsyncClient
from fastapi import status

from app.core.api_server import app
from app.core.mongo_db import get_mongodb_client
from tests.fixture import get_test_mongodb_client, clear_database

app.dependency_overrides[get_mongodb_client] = get_test_mongodb_client


@pytest.mark.asyncio
async def test_get_all_texts_should_return_all_texts():
    # Arrange
    client = await get_test_mongodb_client()
    db = client.get_db()
    number_of_items = 5
    await clear_database(db)
    training_texts = [{"text": f"text_{i}", "isSpam": i % 2 == 0} for i in range(1, number_of_items + 1)]
    await db.trainingSet.insert_many(training_texts)

    # Act
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/training-texts/")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    returned_training_texts = response.json()
    assert len(returned_training_texts) == number_of_items
    for i in range(number_of_items):
        assert returned_training_texts[i]["text"] == training_texts[i]["text"]
        assert returned_training_texts[i]["isSpam"] == training_texts[i]["isSpam"]


@pytest.mark.asyncio
async def test_get_all_texts_should_return_subset_when_skip_and_limit_supplied():
    # Arrange
    client = await get_test_mongodb_client()
    db = client.get_db()
    number_of_items = 5
    skip = 2
    limit = 2
    await clear_database(db)
    training_texts = [{"text": f"limit_test_text_{i}", "isSpam": i % 2 == 0} for i in range(1, number_of_items + 1)]
    await db.trainingSet.insert_many(training_texts)

    # Act
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/api/training-texts/?skip={skip}&limit={limit}")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    returned_training_texts = response.json()
    assert len(returned_training_texts) == limit
    for i in range(skip, skip + limit):
        assert returned_training_texts[i - skip]["text"] == training_texts[i]["text"]
        assert returned_training_texts[i - skip]["isSpam"] == training_texts[i]["isSpam"]
