from pydantic import BaseModel


# Used for AI lead score calculation
class LeadInput(BaseModel):
    income: float
    occupation: str
    goal: str


# Used for saving lead score in database
class LeadScoreCreate(BaseModel):
    user_id: int
    score: int
    category: str
    persona: str