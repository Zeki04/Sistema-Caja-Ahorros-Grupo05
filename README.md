# Sistema-Caja-Ahorros-Grupo05
Sistema de Caja de Ahorros desarrollado por el Grupo 05 para la asignatura Construcción de Aplicaciones de Software.

## 1. Introducción
**Propósito:** Definir y documentar la arquitectura de software para el Sistema de Gestión de Cajas de Ahorro.
**Alcance:** Abarca el diseño del cliente web (Frontend), la lógica de negocio (Backend API), y el modelo de persistencia (Base de Datos).

## 2. Pruebas Unitarias y Cobertura

Para garantizar la fiabilidad del código y validar la lógica de negocio, este proyecto implementa un entorno de pruebas automatizadas cumpliendo con los requerimientos técnicos establecidos:

* **Framework de Pruebas:** Pytest.
* **Análisis de Cobertura:** Coverage.py.
* **Métrica Alcanzada:** > 60% de cobertura en los métodos del backend.

### Instrucciones de Ejecución
Para correr la batería de pruebas y visualizar el reporte de cobertura en la terminal, sitúese en la raíz del directorio `backend/` y ejecute:
`pytest --cov=.`
