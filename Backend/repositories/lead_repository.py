from models.lead_score import LeadScore

def create_lead_score(
    db,
    user_id,
    score,
    category,
    persona
):
    lead = LeadScore(
        user_id=user_id,
        score=score,
        category=category,
        persona=persona
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead