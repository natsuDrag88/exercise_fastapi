from sqlalchemy.orm import Session

from app_fastapi.models import models


class ComercioRepository:

    @staticmethod
    def get_comercio_by_api_key(db: Session, api_key):
        return db.query(models.Comercio.id).filter(models.Comercio.api_key == api_key,
                                                   models.Comercio.activo == True).first()
