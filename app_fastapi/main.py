from fastapi import FastAPI
from app_fastapi.database.db import engine
import app_fastapi.models.models

app = FastAPI()


app_fastapi.models.models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
