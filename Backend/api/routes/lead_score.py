from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_lead_score():
    return {
        "message": "Lead Score API Working"
    }