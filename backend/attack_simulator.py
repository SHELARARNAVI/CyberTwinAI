def simulate_attacks(data):
    attacks = []

    if data.get("mfa") != "Yes":
        attacks.append({
            "attack": "Credential Theft",
            "impact": "Without MFA, attackers may use stolen passwords to access email, cloud apps, invoices, and business data.",
            "severity": "High"
        })

    if data.get("backups") != "Yes":
        attacks.append({
            "attack": "Ransomware",
            "impact": "Weak or untested backups can cause data loss, downtime, and expensive recovery.",
            "severity": "High"
        })

    if data.get("patching") != "Yes":
        attacks.append({
            "attack": "Exploitation of Vulnerable Systems",
            "impact": "Unpatched software may allow attackers to exploit known vulnerabilities.",
            "severity": "Medium"
        })

    if data.get("admin_control") != "Yes":
        attacks.append({
            "attack": "Privilege Abuse",
            "impact": "Too many admin accounts can allow attackers or insiders to make damaging system changes.",
            "severity": "High"
        })

    if data.get("logging") != "Yes":
        attacks.append({
            "attack": "Late Threat Detection",
            "impact": "Without logging, suspicious activity may not be detected until serious damage occurs.",
            "severity": "Medium"
        })

    if data.get("staff_training") != "Yes":
        attacks.append({
            "attack": "Social Engineering",
            "impact": "Untrained staff may fall for phishing emails, fake invoices, or malicious links.",
            "severity": "Medium"
        })

    if not attacks:
        attacks.append({
            "attack": "Low Exposure",
            "impact": "No major attack path detected based on the submitted answers.",
            "severity": "Low"
        })

    return attacks
    