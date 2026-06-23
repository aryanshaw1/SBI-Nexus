def generate_persona(
    income,
    risk_profile
):

    if income == "High" and risk_profile == "Moderate":
        return {
            "persona": "Growth-Oriented Investor",
            "segment": "Young Professional"
        }

    if risk_profile == "Low":
        return {
            "persona": "Conservative Saver",
            "segment": "Retail Customer"
        }

    return {
        "persona": "Balanced Investor",
        "segment": "General Customer"
    }