from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Numeric, ForeignKey

class DepositoDiagnostico(Base):
    __tablename__ = "deposito_diagnostico"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    depositos_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"), nullable=False)
    diagnostico_id: Mapped[int] = mapped_column(ForeignKey("diagnostico.id"), nullable=False)
    monto_aplicado: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    deposito: Mapped["Depositos"] = relationship("Depositos", back_populates="depositos_diagnostico")
    diagnostico: Mapped["Diagnostico"] = relationship("Diagnostico", back_populates="depositos_diagnostico")
