from fastapi import FastAPI, Depends
from typing import List, Optional

from app_fastapi.repository.repository_empleado import EmpleadoRepository
from app_fastapi.schemas import schema_empleado
from app_fastapi.database.db import engine, get_db
from sqlalchemy.orm import Session
import app_fastapi.models.models

app = FastAPI(title="FastAPI Application",
              description="FastAPI Application with Swagger and Sqlalchemy",
              version="1.0.0", )


app_fastapi.models.models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/empleados', tags=["Empleados"], response_model=List[schema_empleado.Empleado])
async def get_all_empleados(db: Session = Depends(get_db)):
    """
    Get all the empleados in database
    """
    return EmpleadoRepository.fetch_all(db)
