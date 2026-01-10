from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, Text, ForeignKey
from datetime import date
from typing import Optional

class SeguimientoPaciente(Base):
    __tablename__ = "seguimiento_paciente"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    plan_tratamiento_id: Mapped[int] = mapped_column(ForeignKey("plan_tratamiento.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    pieza_id: Mapped[int] = mapped_column(ForeignKey("pieza.id"), nullable=False)

    plan_tratamiento: Mapped["PlanTratamiento"] = relationship("PlanTratamiento", back_populates="seguimientos")
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="seguimientos")
    pieza: Mapped["Pieza"] = relationship("Pieza", back_populates="seguimientos")
