from fastapi import FastAPI
from Routes import (
    routes_rol,
    routes_permiso,
    routes_rol_permiso,
    routes_usuario,
    routes_paciente,
    routes_historia_medica,
    routes_plan_tratamiento,
    routes_tratamiento,
    routes_pieza,
    routes_seguimiento_paciente,
    routes_diagnostico,
    routes_inventario,
    routes_cierre_caja,
    routes_transaccion,
    routes_compras,
    routes_comisiones,
    routes_depositos,
    routes_deposito_diagnostico
)

app = FastAPI(title="CentrOral API", version="1.0.0")

# Auth
app.include_router(routes_rol.router, prefix="/api/v1/rol", tags=["Rol"])
app.include_router(routes_permiso.router, prefix="/api/v1/permiso", tags=["Permiso"])
app.include_router(routes_rol_permiso.router, prefix="/api/v1/rol_permiso", tags=["RolPermiso"])
app.include_router(routes_usuario.router, prefix="/api/v1/usuario", tags=["Usuario"])

# Batch 1
app.include_router(routes_paciente.router, prefix="/api/v1/paciente", tags=["Paciente"])
app.include_router(routes_historia_medica.router, prefix="/api/v1/historia_medica", tags=["HistoriaMedica"])
app.include_router(routes_plan_tratamiento.router, prefix="/api/v1/plan_tratamiento", tags=["PlanTratamiento"])
app.include_router(routes_tratamiento.router, prefix="/api/v1/tratamiento", tags=["Tratamiento"])
app.include_router(routes_pieza.router, prefix="/api/v1/pieza", tags=["Pieza"])

# Batch 2
app.include_router(routes_seguimiento_paciente.router, prefix="/api/v1/seguimiento_paciente", tags=["SeguimientoPaciente"])
app.include_router(routes_diagnostico.router, prefix="/api/v1/diagnostico", tags=["Diagnostico"])
app.include_router(routes_inventario.router, prefix="/api/v1/inventario", tags=["Inventario"])
app.include_router(routes_cierre_caja.router, prefix="/api/v1/cierre_caja", tags=["CierreCaja"])
app.include_router(routes_transaccion.router, prefix="/api/v1/transaccion", tags=["Transaccion"])

# Batch 3
app.include_router(routes_compras.router, prefix="/api/v1/compras", tags=["Compras"])
app.include_router(routes_comisiones.router, prefix="/api/v1/comisiones", tags=["Comisiones"])
app.include_router(routes_depositos.router, prefix="/api/v1/depositos", tags=["Depositos"])
app.include_router(routes_deposito_diagnostico.router, prefix="/api/v1/deposito_diagnostico", tags=["DepositoDiagnostico"])

@app.get("/")
async def root():
    return {"message": "CentrOral API Running"}
