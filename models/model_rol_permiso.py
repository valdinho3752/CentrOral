from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

class RolPermiso(Base):
    __tablename__ = "rol_permiso"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey("rol.id"), nullable=False)
    permiso_id: Mapped[int] = mapped_column(ForeignKey("permiso.id"), nullable=False)

    rol: Mapped["Rol"] = relationship("Rol", back_populates="rol_permisos")
    permiso: Mapped["Permiso"] = relationship("Permiso", back_populates="rol_permisos")
