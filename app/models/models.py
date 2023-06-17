from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double
from sqlalchemy.orm import relationship

from app.db.database import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(Integer)
    avatar = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    denominacion_comercial = Column(String)

    marcas = relationship("UsuarioTienda", back_populates="usuario")

class UsuarioTienda(Base):
    __tablename__ = 'b2b_usuario_tienda'

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    tienda_id = Column(Integer)
    descuento    = Column(Double)
    usuario = relationship("User", back_populates="marcas")
