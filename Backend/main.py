from fastapi import FastAPI

from api.routes.auth import router as auth_router
from api.routes.profile import router as profile_router
from api.routes.lead import router as lead_router
from api.routes.lead_score import router as lead_score_router
from api.routes.chat import router as chat_router

app = FastAPI(
title="SBI Nexus"
)

@app.get("/")
def root():
    return {
        "message": "SBI Nexus Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# Authentication Routes

app.include_router(
auth_router,
prefix="/auth",
tags=["Authentication"]
)

# Profile Routes

app.include_router(
    profile_router,
    prefix="/api",
    tags=["Profile"]
)

# Lead Calculator Routes

app.include_router(
lead_router,
prefix="/api",
tags=["Lead Calculator"]
)

# Lead Score Database Routes

app.include_router(
lead_score_router,
prefix="/api",
tags=["Lead Score"]
)

# Chat Routes

app.include_router(
chat_router,
prefix="/api",
tags=["Chat"]
)
