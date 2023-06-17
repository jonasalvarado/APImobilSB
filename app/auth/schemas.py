from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    status: int
    avatar: str
    denominacion_comercial: str
    #items: list[Item] = []

    class Config:
        orm_mode = True