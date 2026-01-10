from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer
from typing import List

class Pieza(Base):
    __tablename__ = "pieza"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    n_pieza: Mapped[int] = mapped_column(Integer, nullable=False)

    seguimientos: Mapped[List["SeguimientoPaciente"]] = relationship("SeguimientoPaciente", back_populates="pieza")


    diagnosticos: Mapped[List["Diagnostico"]] = relationship("Diagnostico", back_populates="pieza")
