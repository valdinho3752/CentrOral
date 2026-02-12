from models.model_plan_tratamiento import PlanTratamiento
from database.conection import Session
from schemas.schema_plan_tratamiento import *
from sqlalchemy import select, update

class PlanTratamientoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_planes(self):
        async with self.session_factory as session:
            result = await session.execute(select(PlanTratamiento))
            return result.scalars().all()

    async def get_plan_by_id(self, plan_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(PlanTratamiento).where(PlanTratamiento.id == plan_id))
            return result.scalar_one_or_none()

    async def create_plan(self, plan: PlanTratamientoCreate):
        async with self.session_factory as session:
            new_plan = PlanTratamiento(
                precio_total=plan.precio_total,
                paciente_id=plan.paciente_id,
                usuario_id=plan.usuario_id,
                estado=plan.estado
            )
            session.add(new_plan)
            await session.commit()
            return new_plan
    
    async def update_plan(self, plan_id: int, plan: PlanTratamientoUpdate):
        async with self.session_factory as session:
            update_data = plan.model_dump(exclude_unset=True)
            if not update_data:
                return None

            plan_to_update = await session.execute(update(PlanTratamiento).where(PlanTratamiento.id == plan_id).values(
                **update_data
            ).returning(PlanTratamiento)
            )
            await session.commit()
            updated = plan_to_update.scalar_one_or_none()
            return updated

    async def delete_plan(self, plan_id: int):
        async with self.session_factory as session:
            plan_to_delete = await session.execute(select(PlanTratamiento).where(PlanTratamiento.id == plan_id))
            plan_to_delete = plan_to_delete.scalar_one_or_none()
            if plan_to_delete is None:
                return None
            await session.delete(plan_to_delete)
            await session.commit()
            return plan_to_delete
