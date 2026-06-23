from fastapi import APIRouter
from schemas.lead_score import LeadInput
from services.lead_service import calculate_lead_score

router = APIRouter()

@router.post("/score")
def score_lead(data: LeadInput):

    result = calculate_lead_score(
        data.income,
        data.occupation,
        data.goal
    )

    return result