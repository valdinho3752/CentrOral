from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Numeric, ForeignKey
from typing import List

class PlanTratamiento(Base):
    __tablename__ = "plan_tratamiento"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    precio_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("paciente.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)

    paciente: Mapped["Paciente"] = relationship("Paciente", back_populates="planes_tratamiento")
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="planes_tratamiento")


    depositos: Mapped[List["Depositos"]] = relationship("Depositos", back_populates="plan_tratamiento")
    diagnosticos: Mapped[List["Diagnostico"]] = relationship("Diagnostico", back_populates="plan_tratamiento")
    seguimientos: Mapped[List["SeguimientoPaciente"]] = relationship("SeguimientoPaciente", back_populates="plan_tratamiento")
