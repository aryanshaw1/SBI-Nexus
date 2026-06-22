from models.profile import Profile

def create_profile(db, data):
    profile = Profile(
        full_name=data.full_name,
        occupation=data.occupation,
        income=data.income,
        risk_profile=data.risk_profile,
        investment_goal=data.investment_goal
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile