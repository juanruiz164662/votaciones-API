from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Voter, Candidate, Vote
from app.schemas import VoterCreate, VoterOut

router = APIRouter(
    prefix="/voters",
    tags=["votantes"]
)

@router.post("", response_model=VoterOut, status_code=status.HTTP_201_CREATED)
def crear_votante(datos: VoterCreate, db: Session = Depends(get_db)):
    existe = db.query(Voter).filter(Voter.email == datos.email).first()
    if existe: 
        raise HTTPException(status_code=409, detail="El votante ya existe")
    
    if db.query(Candidate).filter(Candidate.email == datos.email).first():
        raise HTTPException(status_code=409, detail="Este correo ya pertenece a un candidato")
    
    
    nuevo = Voter(name=datos.name, email=datos.email)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("", response_model=list[VoterOut])
def listar_votantes(db: Session = Depends(get_db)):
    return db.query(Voter).all()

@router.get("/{voter_id}", response_model=VoterOut)
def obtener_votante(voter_id: int, db: Session = Depends(get_db)):
    votante = db.get(Voter, voter_id)
    if votante is None:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    return votante

@router.delete("/{voter_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_votante(voter_id: int, db: Session = Depends(get_db)):
    votante = db.get(Voter, voter_id)
    if votante is None:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    
    voto = db.query(Vote).filter(Vote.voter_id == voter_id).first()
    if voto:
        candidato = db.get(Candidate, voto.candidate_id)
        if candidato and candidato.voto > 0:
            candidato.votes -= 1
        db.delete(voto)
        
    db.delete(votante)
    db.commit()
    return None

