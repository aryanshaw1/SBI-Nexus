from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "total_leads": 100,
        "conversion_rate": 20
    }