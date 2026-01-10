from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import List

class Transaccion(Base):
    __tablename__ = "transaccion"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    origen_deposito: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_hora: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    cierre_caja_id: Mapped[int] = mapped_column(ForeignKey("cierre_caja.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="transacciones")
    cierre_caja: Mapped["CierreCaja"] = relationship("CierreCaja", back_populates="transacciones")


    compras: Mapped[List["Compras"]] = relationship("Compras", back_populates="transaccion")
    depositos: Mapped[List["Depositos"]] = relationship("Depositos", back_populates="transaccion")
