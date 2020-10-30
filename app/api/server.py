from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/", tags=["main"])
async def say_hello():
    return "hello world from fast api"
