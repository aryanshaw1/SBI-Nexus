from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.lead_score import LeadScoreCreate
from repositories.lead_score_repository import create_lead_score

router = APIRouter()


@router.post("/lead-score")
def create_lead_score_api(
    lead_score: LeadScoreCreate,
    db: Session = Depends(get_db)
):

    result = create_lead_score(db, lead_score)

    return {
        "success": True,
        "lead_score_id": result.id
    }