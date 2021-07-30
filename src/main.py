from fastapi import FastAPI
from . import endpoints, models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(endpoints.router, tags=['Pre-Registration'])

@app.get("/")
async def root():
    return {"message": "Hello World"}



