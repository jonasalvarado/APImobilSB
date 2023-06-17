from pydantic import BaseModel
from typing import Optional

class UsuarioTienda(BaseModel):
    id: int 
    usuario_id: int 
    tienda_id: int 
    descuento: float 
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int 
    status: int 
    email: str 
    nombres: str 
    apellidos: str 
    avatar: Optional[str] 
    denominacion_comercial: Optional[str] 
    marcas: list[UsuarioTienda] = []

