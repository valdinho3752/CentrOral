from models.model_depositos import Depositos
from database.conection import Session
from schemas.schema_depositos import *
from sqlalchemy import select, update

class DepositosController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_depositos(self):
        async with self.session_factory as session:
            result = await session.execute(select(Depositos))
            return result.scalars().all()

    async def get_deposito_by_id(self, deposito_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Depositos).where(Depositos.id == deposito_id))
            return result.scalar_one_or_none()

    async def create_deposito(self, deposito: DepositosCreate):
        async with self.session_factory as session:
            new_deposito = Depositos(
                fecha=deposito.fecha,
                deposito=deposito.deposito,
                saldo=deposito.saldo,
                usuario_id=deposito.usuario_id,
                plan_tratamiento_id=deposito.plan_tratamiento_id,
                transaccion_id=deposito.transaccion_id
            )
            session.add(new_deposito)
            await session.commit()
            return new_deposito
    
    async def update_deposito(self, deposito_id: int, deposito: DepositosUpdate):
        async with self.session_factory as session:
            
            update_data = deposito.model_dump(exclude_unset=True)
            if not update_data:
                return None
            
            deposito_to_update = await session.execute(update(Depositos).where(Depositos.id == deposito_id).values(
                **update_data
            ).returning(Depositos)
            )
            await session.commit()
            updated = deposito_to_update.scalar_one_or_none()
            return updated

    async def delete_deposito(self, deposito_id: int):
        async with self.session_factory as session:
            deposito_to_delete = await session.execute(select(Depositos).where(Depositos.id == deposito_id))
            deposito_to_delete = deposito_to_delete.scalar_one_or_none()
            if deposito_to_delete is None:
                return None
            await session.delete(deposito_to_delete)
            await session.commit()
            return deposito_to_delete
