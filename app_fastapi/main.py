from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import app_fastapi.models.models
from app_fastapi.database.db import engine
from app_fastapi.exceptions.exception import InvalidEmpleadoError
from app_fastapi.routes.routers import empleadorouter

app = FastAPI(title="FastAPI Application",
              description="FastAPI Application with Swagger and Sqlalchemy",
              version="1.0.0", )

app_fastapi.models.models.Base.metadata.create_all(bind=engine)
app.include_router(empleadorouter)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.exception_handler(InvalidEmpleadoError)
async def invalid_empleado_exception_handler(request: Request, exc: InvalidEmpleadoError):
    return JSONResponse(status_code=200, content={"rc": -1002, "msg": "Invalid id"})
