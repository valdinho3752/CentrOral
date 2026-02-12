from models.model_deposito_diagnostico import DepositoDiagnostico
from database.conection import Session
from schemas.schema_deposito_diagnostico import *
from sqlalchemy import select, update

class DepositoDiagnosticoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_deposito_diagnosticos(self):
        async with self.session_factory as session:
            result = await session.execute(select(DepositoDiagnostico))
            return result.scalars().all()

    async def get_deposito_diagnostico_by_id(self, dd_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(DepositoDiagnostico).where(DepositoDiagnostico.id == dd_id))
            return result.scalar_one_or_none()

    async def create_deposito_diagnostico(self, dd: DepositoDiagnosticoCreate):
        async with self.session_factory as session:
            new_dd = DepositoDiagnostico(
                depositos_id=dd.depositos_id,
                diagnostico_id=dd.diagnostico_id,
                monto_aplicado=dd.monto_aplicado
            )
            session.add(new_dd)
            await session.commit()
            return new_dd
    
    async def update_deposito_diagnostico(self, dd_id: int, dd: DepositoDiagnosticoUpdate):
        async with self.session_factory as session:
            
            update_data = dd.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            dd_to_update = await session.execute(update(DepositoDiagnostico).where(DepositoDiagnostico.id == dd_id).values(
                **update_data
            ).returning(DepositoDiagnostico)
            )
            await session.commit()
            updated = dd_to_update.scalar_one_or_none()
            return updated

    async def delete_deposito_diagnostico(self, dd_id: int):
        async with self.session_factory as session:
            dd_to_delete = await session.execute(select(DepositoDiagnostico).where(DepositoDiagnostico.id == dd_id))
            dd_to_delete = dd_to_delete.scalar_one_or_none()
            if dd_to_delete is None:
                return None
            await session.delete(dd_to_delete)
            await session.commit()
            return dd_to_delete
