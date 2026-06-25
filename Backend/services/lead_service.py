def calculate_lead_score(income, occupation, goal):

    score = 0

    if income >= 1000000:
        score += 30

    elif income >= 500000:
        score += 20

    else:
        score += 10

    if occupation:
        score += 20

    if goal:
        score += 20

    score += 30

    return {
        "score": min(score, 100),
        "category": "Hot Lead" if score >= 70 else "Warm Lead"
    }