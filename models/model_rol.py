from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List

class Rol(Base):
    __tablename__ = "rol"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_rol: Mapped[str] = mapped_column(String(50), nullable=False)

    usuarios: Mapped[List["Usuario"]] = relationship("Usuario", back_populates="rol")
    rol_permisos: Mapped[List["RolPermiso"]] = relationship("RolPermiso", back_populates="rol")
