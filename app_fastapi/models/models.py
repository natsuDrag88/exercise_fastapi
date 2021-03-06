import uuid as _uuid
from datetime import datetime
from typing import TypedDict

from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app_fastapi.database.db import Base


# model/table
class Comercio(Base):
    __tablename__ = "comercio"

    # fields
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String(32), default=_uuid.uuid4().hex)
    nombre = Column(String(100))
    activo = Column(Boolean, default=True)
    email_contacto = Column(String(50), nullable=True)
    telefono_contacto = Column(String(15), nullable=True)
    api_key = Column(String(32), default=_uuid.uuid4().hex)
    fecha_creacion = Column(DateTime, default=datetime.now)
    empleados = relationship("Empleado", primaryjoin="Comercio.id == Empleado.comercio_id",
                             cascade="all, delete-orphan")


class EmpleadoDict(TypedDict):
    uuid: str
    nombre: str
    apellidos: str
    pin: str
    fecha_creacion: datetime
    activo: bool


class Empleado(Base):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String(32), default=_uuid.uuid4().hex)
    nombre = Column(String(40))
    apellidos = Column(String(40))
    pin = Column(String(6))
    comercio_id = Column(Integer, ForeignKey('comercio.id'), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now)
    activo = Column(Boolean, default=True)

    def __init__(self, nombre: str, apellidos: str, pin: str, comercio_id: int, activo: bool):
        self.nombre = nombre
        self.apellidos = apellidos
        self.pin = pin
        self.comercio_id = comercio_id
        self.activo = activo

    def __repr__(self) -> str:
        return f"<Empleado {self.nombre_completo}>"

    @property
    def serialize(self) -> dict[str, str | datetime | bool]:
        """
        Return item in serializeable format
        """
        return {"id": self.uuid, "nombre_completo": self.nombre + ' ' + self.apellidos, "pin": self.pin,
                "fecha_creacion": self.fecha_creacion, "activo": self.activo}
