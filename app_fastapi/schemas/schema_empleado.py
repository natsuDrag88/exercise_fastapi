from datetime import datetime
from fastapi_utils.guid_type import GUID
from pydantic import BaseModel


class EmpleadoBase(BaseModel):
    uuid: str
    nombre: str
    apellidos: str
    pin: str
    comercio_id: int
    fecha_creacion: datetime
    activo: bool


class EmpleadoCreate(EmpleadoBase):
    pass


class Empleado(EmpleadoBase):
    id: int

    class Config:
        orm_mode = True
