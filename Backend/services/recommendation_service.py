def generate_recommendations(profile):

    recommendations = []

    if profile.financial_goal == "Investment":
        recommendations.append("Fixed Deposit")
        recommendations.append("Mutual Fund")

    if profile.financial_goal == "Savings":
        recommendations.append("Savings Account")

    if profile.financial_goal == "Credit":
        recommendations.append("Credit Card")

    return recommendations