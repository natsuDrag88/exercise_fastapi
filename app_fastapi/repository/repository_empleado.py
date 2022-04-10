from sqlalchemy.orm import Session

from app_fastapi.models import models


class EmpleadoRepository:

    @staticmethod
    def create_empleado(db: Session, empleado, comercio):
        db_empleado = models.Empleado(nombre=empleado.nombre, apellidos=empleado.apellidos,
                                      pin=empleado.pin, comercio_id=comercio, activo=True)
        db.add(db_empleado)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado

    @staticmethod
    def update_empleado(db: Session, empleado):
        updated_empleado = db.merge(empleado)
        db.commit()
        return updated_empleado

    @staticmethod
    async def delete_empleado(db: Session, empleado):
        db.delete(empleado)
        db.commit()

    @staticmethod
    def fetch_by_uuid(db: Session, uuid):
        return db.query(models.Empleado).filter(models.Empleado.uuid == uuid).first()

    @staticmethod
    def fetch_by_pin(db: Session, pin):
        return db.query(models.Empleado).filter(models.Empleado.pin == pin).first()

    @staticmethod
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Empleado).offset(skip).limit(limit).all()
