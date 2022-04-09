from sqlalchemy.orm import Session

from app_fastapi.database.db import Base
from app_fastapi.models.models import Empleado
from app_fastapi.schemas import schema_empleado
from app_fastapi.models import models


class EmpleadoRepository:

    @staticmethod
    async def create(db: Session, empleado: schema_empleado.EmpleadoCreate):
        db_empleado = models.Empleado(nombre=empleado.nombre, apellidos=empleado.apellidos,
                                      pin=empleado.pin, comercio_id=empleado.comercio_id)
        db.add(db_empleado)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado

    @staticmethod
    def fetch_by_id(db: Session, _id):
        return db.query(models.Comercio).filter(models.Empleado.id == _id).first()

    @staticmethod
    def fetch_by_name(db: Session, name):
        return db.query(models.Comercio).filter(models.Empleado.nombre == name).first()

    @staticmethod
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Empleado).offset(skip).limit(limit).all()

    @staticmethod
    async def delete(db: Session, empleado_id):
        db_empleado = db.query(models.Empleado).filter_by(id=empleado_id).first()
        db.delete(db_empleado)
        db.commit()

    @staticmethod
    async def update(db: Session, empleado):
        updated_empleado = db.merge(empleado)
        db.commit()
        return updated_empleado
