def generate_advice(data, risk_result, attack_result):
    business = data.get("business_name", "This business")

    recommendations = []

    if data.get("mfa") != "Yes":
        recommendations.append("Enable multi-factor authentication for all email, cloud, and administrator accounts.")

    if data.get("backups") != "Yes":
        recommendations.append("Create regular backups and test restoration monthly.")

    if data.get("patching") != "Yes":
        recommendations.append("Patch operating systems and applications using a fixed schedule.")

    if data.get("admin_control") != "Yes":
        recommendations.append("Restrict administrator privileges and use separate admin accounts.")

    if data.get("endpoint_security") != "Yes":
        recommendations.append("Install endpoint protection or EDR on all business devices.")

    if data.get("logging") != "Yes":
        recommendations.append("Enable logging for email, cloud services, and important systems.")

    if data.get("incident_response") != "Yes":
        recommendations.append("Create a simple incident response plan for cyber incidents.")

    if not recommendations:
        recommendations.append("Maintain current controls and review security posture every quarter.")

    return {
        "summary": f"{business} has a {risk_result['risk_level']} rating with {risk_result['maturity']} maturity.",
        "business_impact": "The main business risks include downtime, data loss, financial impact, reputational damage, and possible compliance issues.",
        "roadmap": [
            "Month 1: Enable MFA, review admin accounts, and secure cloud/email access.",
            "Month 2: Improve patching, endpoint protection, and backup testing.",
            "Month 3: Create an incident response plan, enable logging, and train staff."
        ],
        "recommendations": recommendations
    }