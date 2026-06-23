def calculate_lead_score(
    income,
    occupation,
    banking_experience,
    investment_goal
):

    score = 0

    if income == "High":
        score += 30
    elif income == "Medium":
        score += 20
    else:
        score += 10

    if occupation == "Salaried":
        score += 20

    if banking_experience == "Experienced":
        score += 20

    if investment_goal:
        score += 30

    if score >= 80:
        category = "Hot Lead"
    elif score >= 60:
        category = "Warm Lead"
    else:
        category = "Cold Lead"

    return {
        "lead_score": score,
        "category": category
    }