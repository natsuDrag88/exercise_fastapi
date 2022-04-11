from datetime import datetime
from pydantic import BaseModel


class EmpleadoBase(BaseModel):
    id: str
    nombre_completo: str
    pin: str
    fecha_creacion: datetime
    activo: bool


class EmpleadoBaseCreate(BaseModel):
    nombre: str
    apellidos: str
    pin: str


class EmpleadoBaseUpdate(BaseModel):
    nombre: str
    apellidos: str
    pin: str
    activo: bool


class EmpleadoCreate(EmpleadoBase):
    pass


class Empleado(EmpleadoBase):
    pass
