from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Numeric, DateTime, ForeignKey
from datetime import datetime
from typing import List, Optional

class Diagnostico(Base):
    __tablename__ = "diagnostico"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cara_dental: Mapped[str] = mapped_column(String(50), nullable=False)
    precio_elegido: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_conclusion: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    precio_aplicado: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    plan_tratamiento_id: Mapped[int] = mapped_column(ForeignKey("plan_tratamiento.id"), nullable=False)
    tratamiento_id: Mapped[int] = mapped_column(ForeignKey("tratamiento.id"), nullable=False)
    pieza_id: Mapped[int] = mapped_column(ForeignKey("pieza.id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)

    plan_tratamiento: Mapped["PlanTratamiento"] = relationship("PlanTratamiento", back_populates="diagnosticos")
    tratamiento: Mapped["Tratamiento"] = relationship("Tratamiento", back_populates="diagnosticos")
    pieza: Mapped["Pieza"] = relationship("Pieza", back_populates="diagnosticos")
    doctor: Mapped["Usuario"] = relationship("Usuario", foreign_keys=[doctor_id], back_populates="diagnosticos_como_doctor")
    usuario: Mapped["Usuario"] = relationship("Usuario", foreign_keys=[usuario_id], back_populates="diagnosticos_creados")


    depositos_diagnostico: Mapped[List["DepositoDiagnostico"]] = relationship("DepositoDiagnostico", back_populates="diagnostico")
