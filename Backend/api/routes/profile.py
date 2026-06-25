from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.profile import ProfileCreate
from repositories.profile_repository import create_profile

router = APIRouter()

@router.post("/profiles")
def create_customer_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db)
):
    result = create_profile(db, profile)

    return {
        "success": True,
        "profile_id": result.id
    }