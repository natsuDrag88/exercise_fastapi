from app_fastapi.api.api_comercio import get_comercio_by_apikey
from app_fastapi.database.db import SessionLocal
from app_fastapi.exceptions.exception import AuthenticationFailed


def get_session():
    session_auth = SessionLocal()
    try:
        yield session_auth
    finally:
        session_auth.close()


def authenticate_credentials(uuid, db):
    comercio = get_comercio_by_apikey(db=db, apikey=uuid)
    if comercio is None:
        raise AuthenticationFailed()

    return comercio
