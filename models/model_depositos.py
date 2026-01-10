from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, Date, ForeignKey
from datetime import date
from typing import List

class Depositos(Base):
    __tablename__ = "depositos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    deposito: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    saldo: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    plan_tratamiento_id: Mapped[int] = mapped_column(ForeignKey("plan_tratamiento.id"), nullable=False)
    transaccion_id: Mapped[int] = mapped_column(ForeignKey("transaccion.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="depositos")
    plan_tratamiento: Mapped["PlanTratamiento"] = relationship("PlanTratamiento", back_populates="depositos")
    transaccion: Mapped["Transaccion"] = relationship("Transaccion", back_populates="depositos")

    depositos_diagnostico: Mapped[List["DepositoDiagnostico"]] = relationship("DepositoDiagnostico", back_populates="deposito")
