from sqlalchemy import String, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Voter(Base):
    __tablename__ = "voters"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    has_voted: Mapped[bool] = mapped_column(nullable=False, default=False)
    
class Candidate(Base):
    __tablename__ = "candidates"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    party: Mapped[str] = mapped_column(String(100), nullable=True)
    votes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    
class Vote(Base):
    __tablename__ = "votes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    voter_id: Mapped[int] = mapped_column(Integer, ForeignKey("voters.id"), nullable=False, unique=True)
    candidate_id: Mapped[int] = mapped_column(Integer, ForeignKey("candidates.id"), nullable=False)
    
    