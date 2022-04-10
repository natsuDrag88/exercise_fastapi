from uuid import UUID

from app_fastapi import exceptions
from app_fastapi.api.api_empleado import get_empleado_by_uuid
from app_fastapi.exceptions.exception import AuthenticationFailed


class BasicAuthentication:

    @staticmethod
    def authenticate_credentials(userid):
        try:
            api_key = UUID(userid)
        except ValueError:
            raise AuthenticationFailed()

        comercio = get_empleado_by_uuid(db=db, uuid=uuid)
        if db_empleado is None:
            raise InvalidEmpleadoError()

        return None