from pydantic import BaseModel


class ComercioBase(BaseModel):
    uuid: str
    nombre: str
    activo: bool
    email_contacto: str
    telefono_contacto: str
    api_key: str
    fecha_creacion: str


class ComercioCreate(ComercioBase):
    pass


class Comercio(ComercioBase):
    id: int

    class Config:
        orm_mode = True
