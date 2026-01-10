-- Created by Redgate Data Modeler (https://datamodeler.redgate-platform.com)
-- Last modification date: 2026-01-10 04:32:56.219

-- tables
-- Table: Cierre_Caja
CREATE TABLE Cierre_Caja (
    ID serial  NOT NULL,
    Fecha_inicio timestamp  NOT NULL,
    Fecha_cierre timestamp  NOT NULL,
    total_ingresos decimal(10,2)  NOT NULL,
    total_egresos decimal(10,2)  NOT NULL,
    total_diario decimal(10,2)  NOT NULL,
    total_acumulado decimal(10,2)  NOT NULL,
    Usuario_ID int  NOT NULL,
    CONSTRAINT Cierre_Caja_pk PRIMARY KEY (ID)
);

-- Table: Compras
CREATE TABLE Compras (
    ID serial  NOT NULL,
    Fecha date  NOT NULL,
    precio_compra decimal(10,2)  NOT NULL,
    cantidad integer  NOT NULL,
    Usuario_ID int  NOT NULL,
    Inventario_ID int  NOT NULL,
    Transaccion_ID int  NOT NULL,
    CONSTRAINT Compras_pk PRIMARY KEY (ID)
);

-- Table: Deposito_Diagnostico
CREATE TABLE Deposito_Diagnostico (
    ID serial  NOT NULL,
    Depositos_ID int  NOT NULL,
    Diagnostico_ID int  NOT NULL,
    monto_aplicado decimal(10,2)  NOT NULL,
    CONSTRAINT Deposito_Diagnostico_pk PRIMARY KEY (ID)
);

-- Table: Depositos
CREATE TABLE Depositos (
    ID serial  NOT NULL,
    Fecha date  NOT NULL,
    Deposito decimal(10,2)  NOT NULL,
    Saldo decimal(10,2)  NOT NULL,
    Usuario_ID int  NOT NULL,
    Plan_Tratamiento_ID int  NOT NULL,
    Transaccion_ID int  NOT NULL,
    CONSTRAINT Depositos_pk PRIMARY KEY (ID)
);

-- Table: Diagnostico
CREATE TABLE Diagnostico (
    ID serial  NOT NULL,
    cara_dental varchar(50)  NOT NULL,
    Plan_Tratamiento_ID int  NOT NULL,
    Tratamiento_ID int  NOT NULL,
    Pieza_ID int  NOT NULL,
    Precio_elegido Varchar(50)  NULL,
    Estado varchar(50)  NOT NULL,
    Fecha_conclusion timestamp  NULL,
    Doctor_ID int  NOT NULL,
    Usuario_ID int  NOT NULL,
    Precio_aplicado decimal(10,2)  NOT NULL,
    CONSTRAINT Diagnostico_pk PRIMARY KEY (ID)
);

-- Table: Historia_Medica
CREATE TABLE Historia_Medica (
    ID serial  NOT NULL,
    Paciente_ID int  NOT NULL,
  
  	-- Preguntas Generales
    Enfermedad_grave boolean DEFAULT false,
    Hospitalizacion boolean DEFAULT false,
    Bajo_cuidado_medico boolean DEFAULT false,

    -- Salud Cardiovascular
    Presion_alta boolean DEFAULT false,
    Ataque_corazon boolean DEFAULT false,
    Dolor_pecho boolean DEFAULT false,
    Bloqueo_coronario boolean DEFAULT false,
    Problema_valvular boolean DEFAULT false,
    Soplo_corazon boolean DEFAULT false,
    Enfermedad_cardiaca boolean DEFAULT false,
    Fiebre_reumatica boolean DEFAULT false,
    Latidos_irregulares boolean DEFAULT false,
    Dificultad_respirar boolean DEFAULT false,
    Infarto boolean DEFAULT false,
    Presion_baja boolean DEFAULT false,

    -- Salud Respiratoria
    Asma boolean DEFAULT false,
    Enfisema boolean DEFAULT false,
    Sinusitis_cronica boolean DEFAULT false,
    Tuberculosis boolean DEFAULT false,

    -- Sistema Endocrino / Sangre
    Diabetes boolean DEFAULT false,
    Sed_frecuente boolean DEFAULT false,
    Problemas_tiroides boolean DEFAULT false,
    Sangrado_anormal boolean DEFAULT false,
    Anemia boolean DEFAULT false,
    Hemofilia boolean DEFAULT false,
    Cancer boolean DEFAULT false,
    Quimioterapia_radiacion boolean DEFAULT false,
    VIH_SIDA boolean DEFAULT false,
    Herpes boolean DEFAULT false,
    Transplante_organos boolean DEFAULT false,
    Transfusion_sangre boolean DEFAULT false,
    Enfermedad_sexual boolean DEFAULT false,

    -- Salud Gastro-Intestinal
    Hepatitis boolean DEFAULT false,
    Enfermedad_higado boolean DEFAULT false,
    Enfermedad_rinon boolean DEFAULT false,
    Enfermedad_estomago boolean DEFAULT false,

    -- Salud Mental / Muscular Esquelético
    Coyuntura_prostetica boolean DEFAULT false,
    Artritis boolean DEFAULT false,
    Osteoporosis boolean DEFAULT false,
    Desmayos_mareos boolean DEFAULT false,
    Convulsiones boolean DEFAULT false,
    Debilidad_muscular boolean DEFAULT false,
    Esclerosis_multiple boolean DEFAULT false,
    Retraso_mental boolean DEFAULT false,
    Alzheimer boolean DEFAULT false,
    Ansiedad_nerviosismo boolean DEFAULT false,
    Tratamiento_salud_mental boolean DEFAULT false,

    -- Alergias
    Alergia_penicilina boolean DEFAULT false,
    Alergia_sulfamidas boolean DEFAULT false,
    Alergia_anestesicos boolean DEFAULT false,
    Alergia_aspirina boolean DEFAULT false,
    Alergia_codeina boolean DEFAULT false,
    Alergia_yodo boolean DEFAULT false,
    Alergia_latex boolean DEFAULT false,
    Alergia_metales boolean DEFAULT false,
    Alergia_otros text, -- Para especificar el campo "Otro" de la imagen

    -- Medicamentos
    Tomando_medicamento boolean DEFAULT false,
    Medicamento_detalle text, -- Para el campo "indique cual y la dosis"
    Bifosfonatos boolean DEFAULT false,

    -- Solo Mujeres
    Embarazada boolean DEFAULT false,
    Lactando boolean DEFAULT false,
    Anticonceptivos boolean DEFAULT false,

    -- Social
    Usa_tabaco boolean DEFAULT false,
    Usa_alcohol boolean DEFAULT false,
    Drogas_recreativas boolean DEFAULT false,
  
    CONSTRAINT Historia_Medica_pk PRIMARY KEY (ID)
);

-- Table: Inventario
CREATE TABLE Inventario (
    ID serial  NOT NULL,
    nombre_insumo varchar(100)  NOT NULL,
    cantidad integer  NOT NULL,
    descripcion text  NULL,
    CONSTRAINT Inventario_pk PRIMARY KEY (ID)
);

-- Table: Paciente
CREATE TABLE Paciente (
    ID serial  NOT NULL,
    Nombres varchar(100)  NOT NULL,
    Apellidos varchar(100)  NOT NULL,
    Telefono varchar(20)  NULL,
    Direccion text  NULL,
    Email varchar(100)  NULL,
    Motivo_consulta text  NULL,
    CONSTRAINT Paciente_pk PRIMARY KEY (ID)
);

-- Table: Permiso
CREATE TABLE Permiso (
    ID serial  NOT NULL,
    Nombre_permiso varchar(50)  NOT NULL,
    CONSTRAINT Permiso_pk PRIMARY KEY (ID)
);

-- Table: Pieza
CREATE TABLE Pieza (
    ID serial  NOT NULL,
    N_pieza integer  NOT NULL,
    CONSTRAINT Pieza_Tratamiento_pk PRIMARY KEY (ID)
);

-- Table: Plan_Tratamiento
CREATE TABLE Plan_Tratamiento (
    ID serial  NOT NULL,
    Precio_Total decimal(10,2)  NOT NULL,
    Paciente_ID int  NOT NULL,
    Usuario_ID int  NOT NULL,
    Estado Varchar(50)  NOT NULL,
    CONSTRAINT Plan_Tratamiento_pk PRIMARY KEY (ID)
);

-- Table: Rol
CREATE TABLE Rol (
    ID serial  NOT NULL,
    Nombre_rol Varchar(50)  NOT NULL,
    CONSTRAINT Rol_pk PRIMARY KEY (ID)
);

-- Table: Rol_permiso
CREATE TABLE Rol_permiso (
    ID serial  NOT NULL,
    Rol_ID int  NOT NULL,
    Permiso_ID int  NOT NULL,
    CONSTRAINT Rol_permiso_pk PRIMARY KEY (ID)
);

-- Table: Seguimiento_Paciente
CREATE TABLE Seguimiento_Paciente (
    ID serial  NOT NULL,
    Fecha date  NOT NULL,
    Descripcion text  NULL,
    Plan_Tratamiento_ID int  NOT NULL,
    Usuario_ID int  NOT NULL,
    Pieza_ID int  NOT NULL,
    CONSTRAINT Seguimiento_Paciente_pk PRIMARY KEY (ID)
);

-- Table: Transaccion
CREATE TABLE Transaccion (
    ID serial  NOT NULL,
    Usuario_ID int  NOT NULL,
    Cierre_Caja_ID int  NOT NULL,
    Tipo varchar(50)  NOT NULL,
    Origen_deposito varchar(50)  NOT NULL,
    Fecha_Hora timestamp  NOT NULL,
    CONSTRAINT Transaccion_pk PRIMARY KEY (ID)
);

-- Table: Tratamiento
CREATE TABLE Tratamiento (
    ID serial  NOT NULL,
    nombre_tratamiento varchar(100)  NOT NULL,
    Precio_economico decimal(10,2)  NOT NULL,
    Precio_medio decimal(10,2)  NULL,
    Precio_alto decimal(10,2)  NULL,
    CONSTRAINT Tratamiento_pk PRIMARY KEY (ID)
);

-- Table: Usuario
CREATE TABLE Usuario (
    ID serial  NOT NULL,
    Codigo varchar(50)  NOT NULL,
    Nombre varchar(50)  NOT NULL,
    Apellido varchar(50)  NOT NULL,
    Rol_ID int  NOT NULL,
    ultima_edicion timestamp  NOT NULL,
    Porcentaje int  NULL,
    CONSTRAINT Usuario_pk PRIMARY KEY (ID)
);

-- Table: comisiones
CREATE TABLE comisiones (
    ID serial  NOT NULL,
    comision_total decimal(10,2)  NOT NULL,
    Usuario_ID int  NOT NULL,
    Cierre_Caja_ID int  NOT NULL,
    CONSTRAINT comisiones_pk PRIMARY KEY (ID)
);

-- foreign keys
-- Reference: Cierre_Caja_Usuario (table: Cierre_Caja)
ALTER TABLE Cierre_Caja ADD CONSTRAINT Cierre_Caja_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compras_Inventario (table: Compras)
ALTER TABLE Compras ADD CONSTRAINT Compras_Inventario
    FOREIGN KEY (Inventario_ID)
    REFERENCES Inventario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compras_Transaccion (table: Compras)
ALTER TABLE Compras ADD CONSTRAINT Compras_Transaccion
    FOREIGN KEY (Transaccion_ID)
    REFERENCES Transaccion (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compras_Usuario (table: Compras)
ALTER TABLE Compras ADD CONSTRAINT Compras_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Deposito_Diagnostico_Depositos (table: Deposito_Diagnostico)
ALTER TABLE Deposito_Diagnostico ADD CONSTRAINT Deposito_Diagnostico_Depositos
    FOREIGN KEY (Depositos_ID)
    REFERENCES Depositos (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Deposito_Diagnostico_Diagnostico (table: Deposito_Diagnostico)
ALTER TABLE Deposito_Diagnostico ADD CONSTRAINT Deposito_Diagnostico_Diagnostico
    FOREIGN KEY (Diagnostico_ID)
    REFERENCES Diagnostico (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Depositos_Plan_Tratamiento (table: Depositos)
ALTER TABLE Depositos ADD CONSTRAINT Depositos_Plan_Tratamiento
    FOREIGN KEY (Plan_Tratamiento_ID)
    REFERENCES Plan_Tratamiento (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Depositos_Transaccion (table: Depositos)
ALTER TABLE Depositos ADD CONSTRAINT Depositos_Transaccion
    FOREIGN KEY (Transaccion_ID)
    REFERENCES Transaccion (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Depositos_Usuario (table: Depositos)
ALTER TABLE Depositos ADD CONSTRAINT Depositos_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Diagnostico_Doctor (table: Diagnostico)
ALTER TABLE Diagnostico ADD CONSTRAINT Diagnostico_Doctor
    FOREIGN KEY (Doctor_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Diagnostico_Pieza (table: Diagnostico)
ALTER TABLE Diagnostico ADD CONSTRAINT Diagnostico_Pieza
    FOREIGN KEY (Pieza_ID)
    REFERENCES Pieza (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Diagnostico_Plan_Tratamiento (table: Diagnostico)
ALTER TABLE Diagnostico ADD CONSTRAINT Diagnostico_Plan_Tratamiento
    FOREIGN KEY (Plan_Tratamiento_ID)
    REFERENCES Plan_Tratamiento (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Diagnostico_Tratamiento (table: Diagnostico)
ALTER TABLE Diagnostico ADD CONSTRAINT Diagnostico_Tratamiento
    FOREIGN KEY (Tratamiento_ID)
    REFERENCES Tratamiento (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Diagnostico_Usuario (table: Diagnostico)
ALTER TABLE Diagnostico ADD CONSTRAINT Diagnostico_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Historia_Medica_Paciente (table: Historia_Medica)
ALTER TABLE Historia_Medica ADD CONSTRAINT Historia_Medica_Paciente
    FOREIGN KEY (Paciente_ID)
    REFERENCES Paciente (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Plan_Tratamiento_Paciente (table: Plan_Tratamiento)
ALTER TABLE Plan_Tratamiento ADD CONSTRAINT Plan_Tratamiento_Paciente
    FOREIGN KEY (Paciente_ID)
    REFERENCES Paciente (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Plan_Tratamiento_Usuario (table: Plan_Tratamiento)
ALTER TABLE Plan_Tratamiento ADD CONSTRAINT Plan_Tratamiento_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Rol_permiso_Permiso (table: Rol_permiso)
ALTER TABLE Rol_permiso ADD CONSTRAINT Rol_permiso_Permiso
    FOREIGN KEY (Permiso_ID)
    REFERENCES Permiso (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Rol_permiso_Rol (table: Rol_permiso)
ALTER TABLE Rol_permiso ADD CONSTRAINT Rol_permiso_Rol
    FOREIGN KEY (Rol_ID)
    REFERENCES Rol (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Seguimiento_Paciente_Pieza (table: Seguimiento_Paciente)
ALTER TABLE Seguimiento_Paciente ADD CONSTRAINT Seguimiento_Paciente_Pieza
    FOREIGN KEY (Pieza_ID)
    REFERENCES Pieza (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Seguimiento_Paciente_Plan_Tratamiento (table: Seguimiento_Paciente)
ALTER TABLE Seguimiento_Paciente ADD CONSTRAINT Seguimiento_Paciente_Plan_Tratamiento
    FOREIGN KEY (Plan_Tratamiento_ID)
    REFERENCES Plan_Tratamiento (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Seguimiento_Paciente_Usuario (table: Seguimiento_Paciente)
ALTER TABLE Seguimiento_Paciente ADD CONSTRAINT Seguimiento_Paciente_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transaccion_Cierre_Caja (table: Transaccion)
ALTER TABLE Transaccion ADD CONSTRAINT Transaccion_Cierre_Caja
    FOREIGN KEY (Cierre_Caja_ID)
    REFERENCES Cierre_Caja (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transaccion_Usuario (table: Transaccion)
ALTER TABLE Transaccion ADD CONSTRAINT Transaccion_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Usuario_Rol (table: Usuario)
ALTER TABLE Usuario ADD CONSTRAINT Usuario_Rol
    FOREIGN KEY (Rol_ID)
    REFERENCES Rol (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: comisiones_Cierre_Caja (table: comisiones)
ALTER TABLE comisiones ADD CONSTRAINT comisiones_Cierre_Caja
    FOREIGN KEY (Cierre_Caja_ID)
    REFERENCES Cierre_Caja (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: comisiones_Usuario (table: comisiones)
ALTER TABLE comisiones ADD CONSTRAINT comisiones_Usuario
    FOREIGN KEY (Usuario_ID)
    REFERENCES Usuario (ID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

