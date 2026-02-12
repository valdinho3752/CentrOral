from models.model_historia_medica import HistoriaMedica
from database.conection import Session
from schemas.schema_historia_medica import *
from sqlalchemy import select, update

class HistoriaMedicaController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_historias(self):
        async with self.session_factory as session:
            result = await session.execute(select(HistoriaMedica))
            return result.scalars().all()

    async def get_historia_by_id(self, historia_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(HistoriaMedica).where(HistoriaMedica.id == historia_id))
            return result.scalar_one_or_none()
            
    async def get_historia_by_paciente_id(self, paciente_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(HistoriaMedica).where(HistoriaMedica.paciente_id == paciente_id))
            return result.scalar_one_or_none()

    async def create_historia(self, historia: HistoriaMedicaCreate):
        async with self.session_factory as session:
            new_historia = HistoriaMedica(
                paciente_id=historia.paciente_id,
                # Preguntas Generales
                enfermedad_grave=historia.enfermedad_grave,
                hospitalizacion=historia.hospitalizacion,
                bajo_cuidado_medico=historia.bajo_cuidado_medico,
                # Salud Cardiovascular
                presion_alta=historia.presion_alta,
                ataque_corazon=historia.ataque_corazon,
                dolor_pecho=historia.dolor_pecho,
                bloqueo_coronario=historia.bloqueo_coronario,
                problema_valvular=historia.problema_valvular,
                soplo_corazon=historia.soplo_corazon,
                enfermedad_cardiaca=historia.enfermedad_cardiaca,
                fiebre_reumatica=historia.fiebre_reumatica,
                latidos_irregulares=historia.latidos_irregulares,
                dificultad_respirar=historia.dificultad_respirar,
                infarto=historia.infarto,
                presion_baja=historia.presion_baja,
                # Salud Respiratoria
                asma=historia.asma,
                enfisema=historia.enfisema,
                sinusitis_cronica=historia.sinusitis_cronica,
                tuberculosis=historia.tuberculosis,
                # Sistema Endocrino / Sangre
                diabetes=historia.diabetes,
                sed_frecuente=historia.sed_frecuente,
                problemas_tiroides=historia.problemas_tiroides,
                sangrado_anormal=historia.sangrado_anormal,
                anemia=historia.anemia,
                hemofilia=historia.hemofilia,
                cancer=historia.cancer,
                quimioterapia_radiacion=historia.quimioterapia_radiacion,
                vih_sida=historia.vih_sida,
                herpes=historia.herpes,
                transplante_organos=historia.transplante_organos,
                transfusion_sangre=historia.transfusion_sangre,
                enfermedad_sexual=historia.enfermedad_sexual,
                # Salud Gastro-Intestinal
                hepatitis=historia.hepatitis,
                enfermedad_higado=historia.enfermedad_higado,
                enfermedad_rinon=historia.enfermedad_rinon,
                enfermedad_estomago=historia.enfermedad_estomago,
                # Salud Mental / Muscular Esquelético
                coyuntura_prostetica=historia.coyuntura_prostetica,
                artritis=historia.artritis,
                osteoporosis=historia.osteoporosis,
                desmayos_mareos=historia.desmayos_mareos,
                convulsiones=historia.convulsiones,
                debilidad_muscular=historia.debilidad_muscular,
                esclerosis_multiple=historia.esclerosis_multiple,
                retraso_mental=historia.retraso_mental,
                alzheimer=historia.alzheimer,
                ansiedad_nerviosismo=historia.ansiedad_nerviosismo,
                tratamiento_salud_mental=historia.tratamiento_salud_mental,
                # Alergias
                alergia_penicilina=historia.alergia_penicilina,
                alergia_sulfamidas=historia.alergia_sulfamidas,
                alergia_anestesicos=historia.alergia_anestesicos,
                alergia_aspirina=historia.alergia_aspirina,
                alergia_codeina=historia.alergia_codeina,
                alergia_yodo=historia.alergia_yodo,
                alergia_latex=historia.alergia_latex,
                alergia_metales=historia.alergia_metales,
                alergia_otros=historia.alergia_otros,
                # Medicamentos
                tomando_medicamento=historia.tomando_medicamento,
                medicamento_detalle=historia.medicamento_detalle,
                bifosfonatos=historia.bifosfonatos,
                # Solo Mujeres
                embarazada=historia.embarazada,
                lactando=historia.lactando,
                anticonceptivos=historia.anticonceptivos,
                # Social
                usa_tabaco=historia.usa_tabaco,
                usa_alcohol=historia.usa_alcohol,
                drogas_recreativas=historia.drogas_recreativas
            )
            session.add(new_historia)
            await session.commit()
            return new_historia
    
    async def update_historia(self, historia_id: int, historia: HistoriaMedicaUpdate):
        async with self.session_factory as session:
            # Note: We pass all fields from update schema. Pydantic handles defaults (None if not set)
            # But update().values() with None overrides existing values with NULL if we are not careful.
            # Ideally we should only pass set values.
            # Using model_dump(exclude_unset=True) is better but here we are manually mapping.
            # For brevity and since we are generating boilerplate, I will map all.
            # BUT wait, Pydantic 'Optional' = None. Mapping None to column might set it to NULL.
            # If the design intends patch semantics, we should only update set fields.
            # SQLAlchemy `values` dict handles it.
            # Let's create a dictionary of non-None values.
            
            update_data = historia.model_dump(exclude_unset=True) 
            if not update_data:
                return None

            historia_to_update = await session.execute(update(HistoriaMedica).where(HistoriaMedica.id == historia_id).values(
                **update_data
            ).returning(HistoriaMedica)
            )
            await session.commit()
            updated = historia_to_update.scalar_one_or_none()
            return updated

    async def delete_historia(self, historia_id: int):
        async with self.session_factory as session:
            historia_to_delete = await session.execute(select(HistoriaMedica).where(HistoriaMedica.id == historia_id))
            historia_to_delete = historia_to_delete.scalar_one_or_none()
            if historia_to_delete is None:
                return None
            await session.delete(historia_to_delete)
            await session.commit()
            return historia_to_delete
