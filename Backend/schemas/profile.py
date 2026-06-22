from pydantic import BaseModel

class ProfileCreate(BaseModel):
    full_name: str
    occupation: str
    income: str
    risk_profile: str
    investment_goal: str