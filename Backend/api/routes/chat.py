from fastapi import APIRouter

from schemas.chat import ChatRequest

from graph.workflow import graph

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "user_id": request.user_id,
            "query": request.query,
            "lead_score": 0,
            "recommendations": [],
            "current_stage": ""
        }
    )

    return result