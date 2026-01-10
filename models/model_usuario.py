from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime
from datetime import datetime
from typing import Optional, List

class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    codigo: Mapped[str] = mapped_column(String(50), nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    rol_id: Mapped[int] = mapped_column(ForeignKey("rol.id"), nullable=False)
    ultima_edicion: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    porcentaje: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    rol: Mapped["Rol"] = relationship("Rol", back_populates="usuarios")


    cierre_cajas: Mapped[List["CierreCaja"]] = relationship("CierreCaja", back_populates="usuario")
    compras: Mapped[List["Compras"]] = relationship("Compras", back_populates="usuario")
    depositos: Mapped[List["Depositos"]] = relationship("Depositos", back_populates="usuario")
    diagnosticos_como_doctor: Mapped[List["Diagnostico"]] = relationship("Diagnostico", foreign_keys="[Diagnostico.doctor_id]", back_populates="doctor")
    diagnosticos_creados: Mapped[List["Diagnostico"]] = relationship("Diagnostico", foreign_keys="[Diagnostico.usuario_id]", back_populates="usuario")
    planes_tratamiento: Mapped[List["PlanTratamiento"]] = relationship("PlanTratamiento", back_populates="usuario")
    seguimientos: Mapped[List["SeguimientoPaciente"]] = relationship("SeguimientoPaciente", back_populates="usuario")
    transacciones: Mapped[List["Transaccion"]] = relationship("Transaccion", back_populates="usuario")
    comisiones: Mapped[List["Comisiones"]] = relationship("Comisiones", back_populates="usuario")
