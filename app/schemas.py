from pydantic import BaseModel, Field, ConfigDict, EmailStr

class VoterCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    
class VoterOut(BaseModel):
    id: int
    name: str
    email: str
    has_voted: bool
    
model_config = ConfigDict(from_attributes=True)

class CandidateCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    party: str | None = Field(default=None, max_length=100)
    email: EmailStr
    
class CandidateOut(BaseModel):
    id: int
    name: str
    party: str | None
    votes: int
    
model_config = ConfigDict(from_attributes=True)

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int
    
class VoteOut(BaseModel):
    id: int
    voter_id: int
    candidate_id: int
    
model_config = ConfigDict(from_attributes=True)

class CandidateStadistics(BaseModel):
    candidate_id: int
    name: str
    party: str | None
    votes: int
    percentage: float
    
class VotingStadistics(BaseModel):
    total_votes: int
    candidates: list[CandidateStadistics]
    total_voters_voted: int