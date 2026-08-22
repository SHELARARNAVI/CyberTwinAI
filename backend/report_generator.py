import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(result):
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    file_path = os.path.join(reports_dir, "CyberTwinAI_Report.pdf")

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "CyberTwin AI - Cyber Risk Assessment Report")

    y -= 40
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Business: {result['business']}")
    y -= 20
    c.drawString(50, y, f"Country: {result['country']}")
    y -= 20
    c.drawString(50, y, f"Industry: {result['industry']}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Risk Summary")

    y -= 25
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Risk Score: {result['risk']['score']} / {result['risk']['max_score']}")
    y -= 20
    c.drawString(50, y, f"Risk Level: {result['risk']['risk_level']}")
    y -= 20
    c.drawString(50, y, f"Maturity: {result['risk']['maturity']}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Attack Simulation")

    c.setFont("Helvetica", 10)
    y -= 25

    for attack in result["attacks"]:
        c.drawString(50, y, f"- {attack['attack']} ({attack['severity']})")
        y -= 15
        c.drawString(70, y, attack["impact"][:90])
        y -= 25

        if y < 100:
            c.showPage()
            y = height - 50

    y -= 15
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Recommendations")

    c.setFont("Helvetica", 10)
    y -= 25

    for rec in result["advice"]["recommendations"]:
        c.drawString(50, y, f"- {rec[:95]}")
        y -= 18

        if y < 100:
            c.showPage()
            y = height - 50

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "90-Day Roadmap")

    c.setFont("Helvetica", 10)
    y -= 25

    for item in result["advice"]["roadmap"]:
        c.drawString(50, y, f"- {item[:95]}")
        y -= 18

    c.save()
    return file_path