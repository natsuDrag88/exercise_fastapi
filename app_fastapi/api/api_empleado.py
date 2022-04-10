from app_fastapi.repository.repository_empleado import EmpleadoRepository


def get_empleados(db):
    return EmpleadoRepository.fetch_all(db)
