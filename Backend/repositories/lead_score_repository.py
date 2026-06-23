from sqlalchemy.orm import Session

from models.lead_score import LeadScore


def create_lead_score(
    db: Session,
    user_id: int,
    score: int,
    category: str
):
    lead = LeadScore(
        user_id=user_id,
        score=score,
        category=category
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead