from typing import TypedDict


class AgentState(TypedDict):

    user_id: str

    query: str

    lead_score: int

    recommendations: list

    current_stage: str