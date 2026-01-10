from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, Date, ForeignKey
from datetime import date

class Compras(Base):
    __tablename__ = "compras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fecha: Mapped[date] = mapped_column(Date, nullable=False)
    precio_compra: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    inventario_id: Mapped[int] = mapped_column(ForeignKey("inventario.id"), nullable=False)
    transaccion_id: Mapped[int] = mapped_column(ForeignKey("transaccion.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="compras")
    inventario: Mapped["Inventario"] = relationship("Inventario", back_populates="compras")
    transaccion: Mapped["Transaccion"] = relationship("Transaccion", back_populates="compras")
