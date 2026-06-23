from pydantic import BaseModel

class LeadInput(BaseModel):
    income: int
    occupation: str
    goal: str