from sqlalchemy.orm import Session
from app_fastapi.schemas import schema_comercio
from app_fastapi.models import models


class ComercioRepository:

    @staticmethod
    async def create(db: Session, comercio: schema_comercio.ComercioCreate):
        db_comercio = models.Comercio(nombre=comercio.nombre, email_contacto=comercio.email_contacto,
                                      telefono_contacto=comercio.telefono_contacto)
        db.add(db_comercio)
        db.commit()
        db.refresh(db_comercio)
        return db_comercio

    @staticmethod
    def fetch_by_id(db: Session, _id):
        return db.query(models.Comercio).filter(models.Comercio.id == _id).first()

    @staticmethod
    def fetch_by_name(db: Session, name):
        return db.query(models.Comercio).filter(models.Comercio.nombre == name).first()

    @staticmethod
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Comercio).offset(skip).limit(limit).all()

    @staticmethod
    async def delete(db: Session, comercio_id):
        db_comercio = db.query(models.Comercio).filter_by(id=comercio_id).first()
        db.delete(db_comercio)
        db.commit()

    @staticmethod
    async def update(db: Session, comercio):
        updated_comercio = db.merge(comercio)
        db.commit()
        return updated_comercio
