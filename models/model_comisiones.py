from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, ForeignKey

class Comisiones(Base):
    __tablename__ = "comisiones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    comision_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    cierre_caja_id: Mapped[int] = mapped_column(ForeignKey("cierre_caja.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="comisiones")
    cierre_caja: Mapped["CierreCaja"] = relationship("CierreCaja", back_populates="comisiones")
