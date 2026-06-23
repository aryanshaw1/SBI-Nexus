def calculate_lead_score(
    income,
    occupation,
    goal
):
    score = 50

    if income > 1000000:
        score += 20

    if occupation.lower() == "engineer":
        score += 10

    if goal.lower() == "investment":
        score += 20

    if score >= 80:
        category = "Hot Lead"
    elif score >= 60:
        category = "Warm Lead"
    else:
        category = "Cold Lead"

    persona = "Growth-Oriented Investor"

    return {
        "score": score,
        "category": category,
        "persona": persona
    }