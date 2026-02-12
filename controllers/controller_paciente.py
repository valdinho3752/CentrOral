from models.model_paciente import Paciente
from database.conection import Session
from schemas.schema_paciente import *
from sqlalchemy import select, update

class PacienteController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_pacientes(self):
        async with self.session_factory as session:
            result = await session.execute(select(Paciente))
            return result.scalars().all()

    async def get_paciente_by_id(self, paciente_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Paciente).where(Paciente.id == paciente_id))
            return result.scalar_one_or_none()

    async def create_paciente(self, paciente: PacienteCreate):
        async with self.session_factory as session:
            new_paciente = Paciente(
                nombres=paciente.nombres,
                apellidos=paciente.apellidos,
                telefono=paciente.telefono,
                direccion=paciente.direccion,
                email=paciente.email,
                motivo_consulta=paciente.motivo_consulta
            )
            session.add(new_paciente)
            await session.commit()
            return new_paciente
    
    async def update_paciente(self, paciente_id: int, paciente: PacienteUpdate):
        async with self.session_factory as session:
            
            update_data = paciente.model_dump(exclude_unset=True)
            if not update_data:
                return None

            paciente_to_update = await session.execute(update(Paciente).where(Paciente.id == paciente_id).values(
                **update_data
            ).returning(Paciente)
            )
            await session.commit()
            updated = paciente_to_update.scalar_one_or_none()
            return updated

    async def delete_paciente(self, paciente_id: int):
        async with self.session_factory as session:
            paciente_to_delete = await session.execute(select(Paciente).where(Paciente.id == paciente_id))
            paciente_to_delete = paciente_to_delete.scalar_one_or_none()
            if paciente_to_delete is None:
                return None
            await session.delete(paciente_to_delete)
            await session.commit()
            return paciente_to_delete
