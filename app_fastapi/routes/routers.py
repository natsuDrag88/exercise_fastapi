from typing import List

from fastapi import Depends, APIRouter
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from app_fastapi.api.api_empleado import get_empleados
from app_fastapi.database.db import get_db, SessionLocal
from app_fastapi.schemas import schema_empleado

empleadorouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@empleadorouter.get('/empleados', tags=["Empleados"], response_class=UJSONResponse)
async def get_all_empleados(db: Session = Depends(get_db)):
    """
    Get all the empleados in database
    """
    empleados = get_empleados(db=db)
    #
    return {"rc": 0, "msg": "Ok", "data": [i.serialize for i in empleados]}
