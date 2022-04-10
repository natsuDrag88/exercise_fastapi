from app_fastapi.repository.repository_empleado import EmpleadoRepository


def get_empleados(db):
    return EmpleadoRepository.fetch_all(db=db)


def get_empleado_by_uuid(db, uuid):
    return EmpleadoRepository.fetch_by_uuid(db=db, uuid=uuid)
