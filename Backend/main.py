from fastapi import FastAPI
from api.routes.auth import router as auth_router
from api.routes.profile import router as profile_router

app = FastAPI(
    title="SBI Nexus"
)

@app.get("/")
def root():
    return {"message": "SBI Nexus Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    profile_router,
    prefix="/profile",
    tags=["Profile"]
)