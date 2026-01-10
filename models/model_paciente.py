from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Integer
from typing import List, Optional

class Paciente(Base):
    __tablename__ = "paciente"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombres: Mapped[str] = mapped_column(String(100), nullable=False)
    apellidos: Mapped[str] = mapped_column(String(100), nullable=False)
    telefono: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    direccion: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    motivo_consulta: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


    historia_medica: Mapped[List["HistoriaMedica"]] = relationship("HistoriaMedica", back_populates="paciente")
    planes_tratamiento: Mapped[List["PlanTratamiento"]] = relationship("PlanTratamiento", back_populates="paciente")
