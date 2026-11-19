from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Voter, Candidate, Vote
from app.schemas import CandidateCreate, CandidateOut

router = APIRouter(
    prefix="/candidates",
    tags=["candidatos"]
)

@router.post("", response_model=CandidateOut, status_code=status.HTTP_201_CREATED)
def crear_candidato(datos: CandidateCreate, db: Session = Depends(get_db)):
    if db.query(Voter).filter(Voter.email == datos.email).first():
        raise HTTPException(status_code=409, detail="Ya hay alguien registrado con este correo")
    
    existe = db.query(Candidate).filter(Candidate.email == datos.email).first()
    if existe:
        raise HTTPException(status_code=409, detail="El candidato ya existe")
    
    nuevo = Candidate(name=datos.name, email=datos.email)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("", response_model=list[CandidateOut])
def listar_candidatos(db: Session = Depends(get_db)):
    return db.query(Candidate).all()

@router.get("/{candidate_id}", response_model=CandidateOut)
def obtener_votante(candidate_id: int, db: Session =Depends(get_db)):
    candidato = db.get(Candidate, candidate_id)
    if candidato is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return candidato

@router.delete("/{candidate_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_candidato(candidate_id: int, db: Session = Depends(get_db)):
    candidato = db.get(Candidate, candidate_id)
    if candidato is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    
    votos = db.query(Vote).filter(Vote.candidate_id == candidate_id).all()
    for voto in votos:
        votante = db.get(Voter, voto.voter_id)
        if votante:
            votante.has_voted = False
        db.delete(voto)
        
    db.delete(candidato)
    db.commit()
    return None