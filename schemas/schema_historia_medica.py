from pydantic import BaseModel
from typing import Optional

class HistoriaMedicaBase(BaseModel):
    paciente_id: int
    
    # Preguntas Generales
    enfermedad_grave: Optional[bool] = False
    hospitalizacion: Optional[bool] = False
    bajo_cuidado_medico: Optional[bool] = False

    # Salud Cardiovascular
    presion_alta: Optional[bool] = False
    ataque_corazon: Optional[bool] = False
    dolor_pecho: Optional[bool] = False
    bloqueo_coronario: Optional[bool] = False
    problema_valvular: Optional[bool] = False
    soplo_corazon: Optional[bool] = False
    enfermedad_cardiaca: Optional[bool] = False
    fiebre_reumatica: Optional[bool] = False
    latidos_irregulares: Optional[bool] = False
    dificultad_respirar: Optional[bool] = False
    infarto: Optional[bool] = False
    presion_baja: Optional[bool] = False

    # Salud Respiratoria
    asma: Optional[bool] = False
    enfisema: Optional[bool] = False
    sinusitis_cronica: Optional[bool] = False
    tuberculosis: Optional[bool] = False

    # Sistema Endocrino / Sangre
    diabetes: Optional[bool] = False
    sed_frecuente: Optional[bool] = False
    problemas_tiroides: Optional[bool] = False
    sangrado_anormal: Optional[bool] = False
    anemia: Optional[bool] = False
    hemofilia: Optional[bool] = False
    cancer: Optional[bool] = False
    quimioterapia_radiacion: Optional[bool] = False
    vih_sida: Optional[bool] = False
    herpes: Optional[bool] = False
    transplante_organos: Optional[bool] = False
    transfusion_sangre: Optional[bool] = False
    enfermedad_sexual: Optional[bool] = False

    # Salud Gastro-Intestinal
    hepatitis: Optional[bool] = False
    enfermedad_higado: Optional[bool] = False
    enfermedad_rinon: Optional[bool] = False
    enfermedad_estomago: Optional[bool] = False

    # Salud Mental / Muscular Esquelético
    coyuntura_prostetica: Optional[bool] = False
    artritis: Optional[bool] = False
    osteoporosis: Optional[bool] = False
    desmayos_mareos: Optional[bool] = False
    convulsiones: Optional[bool] = False
    debilidad_muscular: Optional[bool] = False
    esclerosis_multiple: Optional[bool] = False
    retraso_mental: Optional[bool] = False
    alzheimer: Optional[bool] = False
    ansiedad_nerviosismo: Optional[bool] = False
    tratamiento_salud_mental: Optional[bool] = False

    # Alergias
    alergia_penicilina: Optional[bool] = False
    alergia_sulfamidas: Optional[bool] = False
    alergia_anestesicos: Optional[bool] = False
    alergia_aspirina: Optional[bool] = False
    alergia_codeina: Optional[bool] = False
    alergia_yodo: Optional[bool] = False
    alergia_latex: Optional[bool] = False
    alergia_metales: Optional[bool] = False
    alergia_otros: Optional[str] = None

    # Medicamentos
    tomando_medicamento: Optional[bool] = False
    medicamento_detalle: Optional[str] = None
    bifosfonatos: Optional[bool] = False

    # Solo Mujeres
    embarazada: Optional[bool] = False
    lactando: Optional[bool] = False
    anticonceptivos: Optional[bool] = False

    # Social
    usa_tabaco: Optional[bool] = False
    usa_alcohol: Optional[bool] = False
    drogas_recreativas: Optional[bool] = False

class HistoriaMedicaCreate(HistoriaMedicaBase):
    pass

class HistoriaMedicaUpdate(HistoriaMedicaBase):
    paciente_id: Optional[int] = None
    pass 

class HistoriaMedicaResponse(HistoriaMedicaBase):
    id: int

    class Config:
        from_attributes = True
