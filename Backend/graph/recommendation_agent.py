def recommendation_agent(state):

    state["recommendations"] = [
        "Fixed Deposit",
        "Savings Account",
        "Credit Card"
    ]

    state["current_stage"] = "RECOMMENDATION"

    return state