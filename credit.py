def calculate_risk(income, debt, age):
    """Calculate the credit risk for a customer from income and debt."""
    if income <= 0:
        return -1

    debt_to_income_ratio = debt / income

    if debt_to_income_ratio > 0.6:
        return "HIGH"
    if debt_to_income_ratio > 0.3:
        return "MEDIUM"
    return "LOW"