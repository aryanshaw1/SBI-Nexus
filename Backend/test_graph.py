from graph.workflow import graph

result = graph.invoke(
    {
        "user_id": "1",
        "query": "I want to invest",
        "lead_score": 0,
        "recommendations": [],
        "current_stage": ""
    }
)

print(result)