from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import UJSONResponse
from sqlalchemy.orm import Session

from app_fastapi.api.api_empleado import get_empleados, get_empleado_by_uuid
from app_fastapi.database.db import get_db, SessionLocal
from app_fastapi.exceptions.exception import InvalidEmpleadoError

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
    db_empleados = get_empleados(db=db)
    #
    return {"rc": 0, "msg": "Ok", "data": [i.serialize for i in db_empleados]}


@empleadorouter.get('/empleados/{uuid}', tags=["Empleados"], response_class=UJSONResponse)
async def get_empleados_uuid(uuid: str, db: Session = Depends(get_db)):
    """
    Get empleado whit uuid in database
    """

    db_empleado = get_empleado_by_uuid(db=db, uuid=uuid)
    if db_empleado is None:
        #raise HTTPException(status_code=200, rc=-1002, msg="Invalid id")
        raise InvalidEmpleadoError()

    #
    return {"rc": 0, "msg": "Ok", "data": db_empleado.serialize}