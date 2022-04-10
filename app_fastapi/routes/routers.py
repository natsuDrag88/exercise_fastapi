from fastapi import Depends, APIRouter
from fastapi.responses import UJSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from app_fastapi.api.api_empleado import get_empleados, get_empleado_by_uuid, get_empleado_by_pin, create_empleado, \
    update_empleado, delete_empleado
from app_fastapi.database.db import get_db, SessionLocal
from app_fastapi.exceptions.exception import InvalidEmpleadoError, DuplicatedPinError
from app_fastapi.routes.middleware.authentication import authenticate_credentials
from app_fastapi.schemas.schema_empleado import EmpleadoBaseCreate, EmpleadoBaseUpdate

empleadorouter = APIRouter()
security = HTTPBasic()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@empleadorouter.get('/empleados', tags=["Empleados"], response_class=UJSONResponse)
async def get_all_empleados(db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    authenticate_credentials(credentials.username, db=db)
    """
    Get all the empleados in database
    """
    db_empleados = get_empleados(db=db)
    #
    return {"rc": 0, "msg": "Ok", "data": [i.serialize for i in db_empleados]}


@empleadorouter.get('/empleados/{uuid}', tags=["Empleados"], response_class=UJSONResponse)
async def get_empleados_uuid(uuid: str, db: Session = Depends(get_db),
                             credentials: HTTPBasicCredentials = Depends(security)):
    """
    Get empleado whit uuid in database
    """
    authenticate_credentials(credentials.username, db=db)

    db_empleado = get_empleado_by_uuid(db=db, uuid=uuid)
    if db_empleado is None:
        raise InvalidEmpleadoError()

    #
    return {"rc": 0, "msg": "Ok", "data": db_empleado.serialize}


@empleadorouter.post('/empleados', tags=["Empleados"], response_class=UJSONResponse)
async def create_empleados(empleado_request: EmpleadoBaseCreate, db: Session = Depends(get_db),
                           credentials: HTTPBasicCredentials = Depends(security)):
    """
    Create an empleado in the database
    """
    comercio = authenticate_credentials(credentials.username, db=db)
    db_empleado = get_empleado_by_pin(db=db, pin=empleado_request.pin)
    if db_empleado:
        raise DuplicatedPinError()
    empleado = create_empleado(db=db, empleado=empleado_request, comercio=comercio[0])
    return {"rc": 0, "msg": "Ok", "data": empleado.serialize}


@empleadorouter.put('/empleados/{uuid}', tags=["Empleados"], response_class=UJSONResponse)
async def update_empleados(uuid: str, empleado_request: EmpleadoBaseUpdate, db: Session = Depends(get_db),
                           credentials: HTTPBasicCredentials = Depends(security)):
    """
    Create an empleado in the database
    """
    authenticate_credentials(credentials.username, db=db)

    db_empleado = get_empleado_by_uuid(db=db, uuid=uuid)
    if db_empleado is None:
        raise InvalidEmpleadoError()

    db_pin = get_empleado_by_pin(db=db, pin=empleado_request.pin)
    if db_pin:
        raise DuplicatedPinError()

    db_empleado.nombre = empleado_request.nombre
    db_empleado.apellidos = empleado_request.apellidos
    db_empleado.pin = empleado_request.pin
    db_empleado.activo = empleado_request.activo

    empleado = update_empleado(db=db, empleado=db_empleado)

    return {"rc": 0, "msg": "Ok", "data": empleado.serialize}


@empleadorouter.delete('/empleados/{uuid}', tags=["Empleados"], response_class=UJSONResponse)
async def delete_empleados(uuid: str, db: Session = Depends(get_db),
                           credentials: HTTPBasicCredentials = Depends(security)):
    """
    Create an empleado in the database
    """
    authenticate_credentials(credentials.username, db=db)

    db_empleado = get_empleado_by_uuid(db=db, uuid=uuid)
    if db_empleado is None:
        raise InvalidEmpleadoError()

    await delete_empleado(db=db, empleado=db_empleado)

    return {"rc": 0, "msg": "Ok"}
