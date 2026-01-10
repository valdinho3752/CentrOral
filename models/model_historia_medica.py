from database.conection import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Integer, Boolean, ForeignKey
from typing import Optional

class HistoriaMedica(Base):
    __tablename__ = "historia_medica"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("paciente.id"), nullable=False)
    
    # Preguntas Generales
    enfermedad_grave: Mapped[bool] = mapped_column(Boolean, default=False)
    hospitalizacion: Mapped[bool] = mapped_column(Boolean, default=False)
    bajo_cuidado_medico: Mapped[bool] = mapped_column(Boolean, default=False)

    # Salud Cardiovascular
    presion_alta: Mapped[bool] = mapped_column(Boolean, default=False)
    ataque_corazon: Mapped[bool] = mapped_column(Boolean, default=False)
    dolor_pecho: Mapped[bool] = mapped_column(Boolean, default=False)
    bloqueo_coronario: Mapped[bool] = mapped_column(Boolean, default=False)
    problema_valvular: Mapped[bool] = mapped_column(Boolean, default=False)
    soplo_corazon: Mapped[bool] = mapped_column(Boolean, default=False)
    enfermedad_cardiaca: Mapped[bool] = mapped_column(Boolean, default=False)
    fiebre_reumatica: Mapped[bool] = mapped_column(Boolean, default=False)
    latidos_irregulares: Mapped[bool] = mapped_column(Boolean, default=False)
    dificultad_respirar: Mapped[bool] = mapped_column(Boolean, default=False)
    infarto: Mapped[bool] = mapped_column(Boolean, default=False)
    presion_baja: Mapped[bool] = mapped_column(Boolean, default=False)

    # Salud Respiratoria
    asma: Mapped[bool] = mapped_column(Boolean, default=False)
    enfisema: Mapped[bool] = mapped_column(Boolean, default=False)
    sinusitis_cronica: Mapped[bool] = mapped_column(Boolean, default=False)
    tuberculosis: Mapped[bool] = mapped_column(Boolean, default=False)

    # Sistema Endocrino / Sangre
    diabetes: Mapped[bool] = mapped_column(Boolean, default=False)
    sed_frecuente: Mapped[bool] = mapped_column(Boolean, default=False)
    problemas_tiroides: Mapped[bool] = mapped_column(Boolean, default=False)
    sangrado_anormal: Mapped[bool] = mapped_column(Boolean, default=False)
    anemia: Mapped[bool] = mapped_column(Boolean, default=False)
    hemofilia: Mapped[bool] = mapped_column(Boolean, default=False)
    cancer: Mapped[bool] = mapped_column(Boolean, default=False)
    quimioterapia_radiacion: Mapped[bool] = mapped_column(Boolean, default=False)
    vih_sida: Mapped[bool] = mapped_column(Boolean, default=False)
    herpes: Mapped[bool] = mapped_column(Boolean, default=False)
    transplante_organos: Mapped[bool] = mapped_column(Boolean, default=False)
    transfusion_sangre: Mapped[bool] = mapped_column(Boolean, default=False)
    enfermedad_sexual: Mapped[bool] = mapped_column(Boolean, default=False)

    # Salud Gastro-Intestinal
    hepatitis: Mapped[bool] = mapped_column(Boolean, default=False)
    enfermedad_higado: Mapped[bool] = mapped_column(Boolean, default=False)
    enfermedad_rinon: Mapped[bool] = mapped_column(Boolean, default=False)
    enfermedad_estomago: Mapped[bool] = mapped_column(Boolean, default=False)

    # Salud Mental / Muscular Esquelético
    coyuntura_prostetica: Mapped[bool] = mapped_column(Boolean, default=False)
    artritis: Mapped[bool] = mapped_column(Boolean, default=False)
    osteoporosis: Mapped[bool] = mapped_column(Boolean, default=False)
    desmayos_mareos: Mapped[bool] = mapped_column(Boolean, default=False)
    convulsiones: Mapped[bool] = mapped_column(Boolean, default=False)
    debilidad_muscular: Mapped[bool] = mapped_column(Boolean, default=False)
    esclerosis_multiple: Mapped[bool] = mapped_column(Boolean, default=False)
    retraso_mental: Mapped[bool] = mapped_column(Boolean, default=False)
    alzheimer: Mapped[bool] = mapped_column(Boolean, default=False)
    ansiedad_nerviosismo: Mapped[bool] = mapped_column(Boolean, default=False)
    tratamiento_salud_mental: Mapped[bool] = mapped_column(Boolean, default=False)

    # Alergias
    alergia_penicilina: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_sulfamidas: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_anestesicos: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_aspirina: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_codeina: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_yodo: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_latex: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_metales: Mapped[bool] = mapped_column(Boolean, default=False)
    alergia_otros: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Medicamentos
    tomando_medicamento: Mapped[bool] = mapped_column(Boolean, default=False)
    medicamento_detalle: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    bifosfonatos: Mapped[bool] = mapped_column(Boolean, default=False)

    # Solo Mujeres
    embarazada: Mapped[bool] = mapped_column(Boolean, default=False)
    lactando: Mapped[bool] = mapped_column(Boolean, default=False)
    anticonceptivos: Mapped[bool] = mapped_column(Boolean, default=False)

    # Social
    usa_tabaco: Mapped[bool] = mapped_column(Boolean, default=False)
    usa_alcohol: Mapped[bool] = mapped_column(Boolean, default=False)
    drogas_recreativas: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relaciones
    paciente: Mapped["Paciente"] = relationship("Paciente", back_populates="historia_medica")
