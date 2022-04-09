import uuid as _uuid
from datetime import datetime

import sqlalchemy as sa
from fastapi_utils.guid_type import GUID
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app_fastapi.database.db import Base


# model/table
class Comercio(Base):
    __tablename__ = "comercio"

    # fields
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    uuid = sa.Column(GUID, default=_uuid.uuid4)
    nombre = Column(String(100))
    activo = Column(Boolean, default=True)
    email_contacto = Column(String(50), nullable=True)
    telefono_contacto = Column(String(15), nullable=True)
    api_key = sa.Column(GUID, default=_uuid.uuid4)
    fecha_creacion = Column(DateTime, default=datetime.now)
    empleados = relationship("Empleado", primaryjoin="Comercio.id == Empleado.comercio_id",
                             cascade="all, delete-orphan")


class Empleado(Base):
    __tablename__ = "empleado"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    uuid = Column(String(32), default=_uuid.uuid4)
    nombre = Column(String(40))
    apellidos = Column(String(40))
    pin = Column(String(6))
    comercio_id = Column(Integer, ForeignKey('comercio.id'), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now)
    activo = Column(Boolean, default=True)

    class Meta:
        unique_together = ('pin', 'comercio')
