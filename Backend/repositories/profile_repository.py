from models.profile import Profile

def create_profile(db, data):

    profile = Profile(
    user_id=1,
    full_name=data.full_name,
    occupation=data.occupation,
    annual_income=data.annual_income,
    risk_profile=data.risk_profile,
    financial_goal=data.financial_goal
)
    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile