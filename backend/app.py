from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from scoring import calculate_risk
from attack_simulator import simulate_attacks
from llm_advisor import generate_advice
from report_generator import generate_pdf_report

app = Flask(__name__)
CORS(app)

latest_result = {}

@app.route("/assess", methods=["POST"])
def assess():
    global latest_result

    data = request.json

    risk_result = calculate_risk(data)
    attack_result = simulate_attacks(data)
    advice = generate_advice(data, risk_result, attack_result)

    latest_result = {
        "business": data.get("business_name"),
        "country": data.get("country"),
        "industry": data.get("industry"),
        "risk": risk_result,
        "attacks": attack_result,
        "advice": advice
    }

    return jsonify(latest_result)

@app.route("/download-report", methods=["GET"])
def download_report():
    if not latest_result:
        return jsonify({"error": "No assessment completed yet"}), 400

    file_path = generate_pdf_report(latest_result)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    