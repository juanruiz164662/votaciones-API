from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from app.database import get_db
from app.models import Voter, Candidate, Vote
from app.schemas import VoteCreate, VoteOut, CandidateStadistics, VotingStadistics

router = APIRouter(
    prefix="/votes",
    tags=["votos"]
)

@router.post("", response_model=VoteOut, status_code=status.HTTP_201_CREATED)
def emitir_voto(datos: VoteCreate, db: Session = Depends(get_db)):
    votante = db.get(Voter, datos.voter_id)
    if votante is None:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    
    candidato = db.get(Candidate, datos.candidate_id)
    if candidato is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    
    if votante.has_voted:
        raise HTTPException(status_code=400, detail="El votante ya ha emitido su voto")

    nuevo_voto = Vote(voter_id=datos.voter_id, candidate_id=datos.candidate_id)
    votante.has_voted = True
    candidato.votes += 1
    db.add(nuevo_voto)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="El votante ya ha emitido su voto")
    db.refresh(nuevo_voto)
    return nuevo_voto

@router.get("", response_model=list[VoteOut])
def listar_votos(db: Session = Depends(get_db)):
    return db.query(Vote).all()

@router.get("/statistics", response_model=VotingStadistics)
def obtener_estadisticas(db: Session = Depends(get_db)):
    total_votos = db.query(Vote).count()
    total_votantes = db.query(Voter).filter(Voter.has_voted == True).count()
    
    conteo = dict(
        db.query(Vote.candidate_id, func.count(Vote.id))
        .group_by(Vote.candidate_id)
        .all()
    )
    
    resultado = []
    for candidato in db.query(Candidate).all():
        votos = conteo.get(candidato.id, 0) 
        if total_votos > 0:
            porcentaje = round(votos / total_votos * 100)
        else:
            porcentaje = 0
        resultado.append(CandidateStadistics(
            candidate_id=candidato.id,
            name=candidato.name,
            party=candidato.party,
            votes=votos,
            percentage=porcentaje
        ))
    
    return VotingStadistics(
        total_votes=total_votos,
        candidates=resultado,
        total_voters_voted=total_votantes
    )
