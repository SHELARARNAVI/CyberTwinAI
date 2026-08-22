def calculate_risk(data):
    score = 0

    controls = [
        "mfa",
        "backups",
        "patching",
        "admin_control",
        "endpoint_security",
        "staff_training",
        "logging",
        "incident_response"
    ]

    for control in controls:
        value = data.get(control, "No")

        if value == "No":
            score += 10
        elif value == "Partially":
            score += 5
        elif value == "Yes":
            score += 0

    if score <= 25:
        risk_level = "Low Risk"
    elif score <= 55:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    if score <= 20:
        maturity = "Level 3 - Strong"
    elif score <= 40:
        maturity = "Level 2 - Good"
    elif score <= 60:
        maturity = "Level 1 - Basic"
    else:
        maturity = "Level 0 - Weak"

    return {
        "score": score,
        "max_score": 80,
        "percentage": round((score / 80) * 100, 2),
        "risk_level": risk_level,
        "maturity": maturity
    }
    