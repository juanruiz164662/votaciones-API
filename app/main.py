from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app import models
from app.routers import voters
from app.routers import candidates
from app.routers import votes

app = FastAPI(
    title="API de ejemplo",
    version="1.0.0",
    description="API Restful para gestionar votantes candidatos, votantes y estadisticas",    
)

Base.metadata.create_all(bind=engine)
app.include_router(voters.router)
app.include_router(candidates.router)
app.include_router(votes.router)

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de ejemplo"}

@app.get("/test-db")
def test_db():
    with engine.connect() as conexion:
        conexion.execute(text("SELECT 1"))
    return {"base de datos": "conectada"} 