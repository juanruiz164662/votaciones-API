# API de Votaciones

API RESTful hecha con **Python**, **FastAPI** y **PostgreSQL** para gestionar votantes, candidatos, votos y estadísticas de una votación.

## Características

- Registro, consulta y eliminación de votantes y candidatos.
- Cada votante puede emitir un único voto.
- Un votante no puede ser candidato, ni un candidato puede ser votante.
- Estadísticas: votos por candidato, porcentaje de votos y total de votantes que han votado.

## Requisitos

- Python 3.11 o superior
- PostgreSQL, con una base de datos llamada `votaciones`

## Instalación
1. Clona el repositorio:
   
   git clone https://github.com/juanruiz164662/votaciones-api.git
   cd votaciones-api
   

2. Instala las dependencias:

   pip install -r requirements.txt
   

3. Crea un archivo `.env` en la raíz del proyecto con esta línea:

   DATABASE_URL=postgresql://postgres:root@localhost:5432/votaciones

## Ejecución

python -m uvicorn app.main:app --reload

- API: http://127.0.0.1:8000
- Documentación interactiva (Swagger): 