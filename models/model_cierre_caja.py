from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, DateTime, ForeignKey
from datetime import datetime
from typing import List

class CierreCaja(Base):
    __tablename__ = "cierre_caja"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fecha_cierre: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    total_ingresos: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)
    total_egresos: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)
    total_diario: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)
    total_acumulado: Mapped[float] = mapped_column(Numeric(10, 2), nullable=True)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="cierre_cajas")


    transacciones: Mapped[List["Transaccion"]] = relationship("Transaccion", back_populates="cierre_caja")
    comisiones: Mapped[List["Comisiones"]] = relationship("Comisiones", back_populates="cierre_caja")
