from fastapi import FastAPI

from app.features.training_set.router import router as training_set_router

app = FastAPI()


@app.get("/", tags=["Main"])
async def welcome():
    return "The spam filter is working"

# Routers
app.include_router(
    training_set_router,
    prefix="/api/training-texts",
    tags=["Training Set"]
)
