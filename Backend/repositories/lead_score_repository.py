from models.lead_score import LeadScore


def create_lead_score(db, data):

    lead_score = LeadScore(
        user_id=data.user_id,
        score=data.score,
        category=data.category,
        persona=data.persona
    )

    db.add(lead_score)
    db.commit()
    db.refresh(lead_score)

    return lead_score