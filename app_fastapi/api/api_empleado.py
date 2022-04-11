from app_fastapi.repository.repository_empleado import EmpleadoRepository


def get_empleados(db):
    return EmpleadoRepository.fetch_all(db=db)


def get_empleado_by_uuid(db, uuid):
    return EmpleadoRepository.fetch_by_uuid(db=db, uuid=uuid)


def get_empleado_by_pin(db, pin):
    return EmpleadoRepository.fetch_by_pin(db=db, pin=pin)


def create_empleado(db, empleado, comercio):
    return EmpleadoRepository.create_empleado(db=db, empleado=empleado, comercio=comercio)


def update_empleado(db, empleado):
    return EmpleadoRepository.update_empleado(db=db, empleado=empleado)


def delete_empleado(db, empleado):
    return EmpleadoRepository.delete_empleado(db=db, empleado=empleado)
