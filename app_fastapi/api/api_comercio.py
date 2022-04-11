from app_fastapi.repository.repositroy_comercio import ComercioRepository


def get_comercio_by_apikey(db, apikey):
    return ComercioRepository().get_comercio_by_api_key(db=db, api_key=apikey)
