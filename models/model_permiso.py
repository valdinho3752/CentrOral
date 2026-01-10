from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from typing import List

class Permiso(Base):
    __tablename__ = "permiso"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_permiso: Mapped[str] = mapped_column(String(50), nullable=False)

    rol_permisos: Mapped[List["RolPermiso"]] = relationship("RolPermiso", back_populates="permiso")
