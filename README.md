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

   DATABASE_URL=postgresql://postgres:TU_CONTRASEÑA@localhost:5432/votaciones

## Ejecución

python -m uvicorn app.main:app --reload

- API: http://127.0.0.1:8000
- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs
<<<<<<< HEAD
=======

## Endpoints

### Votantes

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/voters` | Registra un votante |
| GET | `/voters` | Lista los votantes |
| GET | `/voters/{id}` | Obtiene un votante por ID |
| DELETE | `/voters/{id}` | Elimina un votante |

### Candidatos

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/candidates` | Registra un candidato |
| GET | `/candidates` | Lista los candidatos |
| GET | `/candidates/{id}` | Obtiene un candidato por ID |
| DELETE | `/candidates/{id}` | Elimina un candidato |

### Votos

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/votes` | Emite un voto |
| GET | `/votes` | Lista todos los votos |
| GET | `/votes/statistics` | Estadísticas de la votación |

## Ejemplos de uso

### Registrar un votante

curl -X POST http://127.0.0.1:8000/voters \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana Pérez", "email": "ana@correo.com"}'


Respuesta (`201 Created`):

json
{
  "id": 1,
  "name": "Ana Pérez",
  "email": "ana@correo.com",
  "has_voted": false
}


### Registrar un candidato

curl -X POST http://127.0.0.1:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "Luis Gómez", "party": "Partido A", "email": "luis@correo.com"}'


Respuesta (`201 Created`):

json
{
  "id": 1,
  "name": "Luis Gómez",
  "party": "Partido A",
  "votes": 0
}


### Emitir un voto

curl -X POST http://127.0.0.1:8000/votes \
  -H "Content-Type: application/json" \
  -d '{"voter_id": 1, "candidate_id": 1}'


Respuesta (`201 Created`):

json
{
  "id": 1,
  "voter_id": 1,
  "candidate_id": 1
}


Si el mismo votante intenta votar otra vez, la respuesta es `409 Conflict`.

### Consultar estadísticas

curl http://127.0.0.1:8000/votes/statistics


Respuesta (`200 OK`), con datos de ejemplo:

json
{
  "total_votes": 2,
  "total_voters_voted": 2,
  "candidates": [
    {"candidate_id": 1, "name": "Luis Gómez", "party": "Partido A", "votes": 1, "percentage": 50.0},
    {"candidate_id": 2, "name": "María López", "party": "Partido B", "votes": 1, "percentage": 50.0}
  ]
}


## Capturas

### Estadísticas de la votación

![Estadísticas de la votación](capturas/estadisticas.png)

## Códigos de respuesta

| Código | Cuándo ocurre |
|---|---|
| 200 | Consulta correcta |
| 201 | Registro creado |
| 204 | Eliminado correctamente |
| 404 | El votante, candidato o voto no existe |
| 409 | Correo repetido, votante que ya votó o regla de votante/candidato |

## Estructura del proyecto

votaciones-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── voters.py
│       ├── candidates.py
│       └── votes.py
├── capturas/
│   └── estadisticas.png
├── requirements.txt
└── README.md
>>>>>>> 12c8ecc (Correcion en candidatos y votantes)
