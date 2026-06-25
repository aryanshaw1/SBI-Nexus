def calculate_conversion_rate(
    total_leads,
    converted
):

    if total_leads == 0:
        return 0

    return round(
        (converted / total_leads) * 100,
        2
    )