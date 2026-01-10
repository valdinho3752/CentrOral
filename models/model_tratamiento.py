from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Numeric
from typing import List, Optional

class Tratamiento(Base):
    __tablename__ = "tratamiento"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_tratamiento: Mapped[str] = mapped_column(String(100), nullable=False)
    precio_economico: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    precio_medio: Mapped[Optional[float]] = mapped_column(Numeric(10, 2), nullable=True)
    precio_alto: Mapped[Optional[float]] = mapped_column(Numeric(10, 2), nullable=True)


    diagnostic: Mapped[List["Diagnostico"]] = relationship("Diagnostico", back_populates="tratamiento")
