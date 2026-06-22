from fastapi import FastAPI

app = FastAPI(
    title="Sistema Caja de Ahorros - Grupo 05",
    description="Backend inicial para la gestión de socios, cuentas de ahorro, créditos y transacciones.",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {"mensaje": "Backend del Sistema Caja de Ahorros funcionando"}

@app.get("/socios")
def listar_socios():
    return [
        {"id": 1, "nombre": "Juan Perez", "cedula": "0912345678"},
        {"id": 2, "nombre": "Maria Lopez", "cedula": "0923456789"}
    ]

@app.get("/cuentas")
def listar_cuentas():
    return [
        {"id": 1, "numero": "CA-001", "saldo": 150.00, "socio_id": 1},
        {"id": 2, "numero": "CA-002", "saldo": 300.00, "socio_id": 2}
    ]
