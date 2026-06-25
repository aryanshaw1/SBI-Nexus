from pydantic import BaseModel

class ProfileCreate(BaseModel):
    full_name: str
    occupation: str
    annual_income: float
    risk_profile: str
    financial_goal: str