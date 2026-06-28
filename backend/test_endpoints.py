from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import patch

app = FastAPI()


# ==========================
# Funciones simuladas
# (serán reemplazadas con mock en las pruebas)
# ==========================

def procesar_deposito(idSocio: int, monto: float):
    raise NotImplementedError


def obtener_saldo(idSocio: int):
    raise NotImplementedError


def solicitar_credito(montoSolicitado: float, plazoMeses: int):
    raise NotImplementedError


# ==========================
# Endpoints simulados
# ==========================

@app.post("/api/transacciones/deposito")
def deposito(data: dict):
    return procesar_deposito(
        data["idSocio"],
        data["monto"]
    )


@app.get("/api/socios/{idSocio}/saldo")
def saldo(idSocio: int):
    return obtener_saldo(idSocio)


@app.post("/api/creditos/solicitud")
def credito(data: dict):
    return solicitar_credito(
        data["montoSolicitado"],
        data["plazoMeses"]
    )


client = TestClient(app)


# ===================================================
# PRUEBA 1
# POST /api/transacciones/deposito
# ===================================================

def test_deposito():
    with patch(__name__ + ".procesar_deposito") as mock_deposito:

        mock_deposito.return_value = {
            "mensaje": "Depósito realizado correctamente"
        }

        response = client.post(
            "/api/transacciones/deposito",
            json={
                "idSocio": 1025,
                "monto": 250.00
            }
        )

        assert response.status_code == 200
        assert response.json()["mensaje"] == "Depósito realizado correctamente"


# ===================================================
# PRUEBA 2
# GET /api/socios/1025/saldo
# ===================================================

def test_consultar_saldo():
    with patch(__name__ + ".obtener_saldo") as mock_saldo:

        mock_saldo.return_value = {
            "idSocio": 1025,
            "saldo": 1850.50
        }

        response = client.get("/api/socios/1025/saldo")

        assert response.status_code == 200
        assert response.json()["idSocio"] == 1025
        assert response.json()["saldo"] == 1850.50


# ===================================================
# PRUEBA 3
# POST /api/creditos/solicitud
# ===================================================

def test_solicitud_credito():
    with patch(__name__ + ".solicitar_credito") as mock_credito:

        mock_credito.return_value = {
            "mensaje": "Solicitud recibida"
        }

        response = client.post(
            "/api/creditos/solicitud",
            json={
                "montoSolicitado": 5000,
                "plazoMeses": 24
            }
        )

        assert response.status_code == 200
        assert response.json()["mensaje"] == "Solicitud recibida"