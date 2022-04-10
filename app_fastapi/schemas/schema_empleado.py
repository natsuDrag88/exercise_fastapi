from datetime import datetime
from pydantic import BaseModel


class EmpleadoBase(BaseModel):
    id: str
    nombre_completo: str
    pin: str
    fecha_creacion: datetime
    activo: bool


class EmpleadoCreate(EmpleadoBase):
    pass


class Empleado(EmpleadoBase):
    pass
