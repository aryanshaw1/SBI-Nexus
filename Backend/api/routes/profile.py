from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def get_profile():

    return {
        "name": "Aryan Shaw",
        "role": "customer"
    }

@router.get("/test")
def test_profile():

    return {
        "message": "Profile API Working"
    }