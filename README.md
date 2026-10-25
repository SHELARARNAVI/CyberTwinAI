# CyberTwin AI

CyberTwin AI is a cybersecurity risk assessment and scenario-simulation prototype designed to help small and medium-sized businesses understand their security posture and identify potential cyber risks.

## Version

**Version 1.0 – Functional Prototype**

## Features

* Business cybersecurity posture assessment
* Rule-based cyber risk scoring
* Security maturity estimation
* Scenario-based cyber risk simulation
* Credential theft analysis
* Ransomware risk analysis
* Privilege abuse analysis
* Social engineering risk analysis
* Security recommendations
* 90-day improvement roadmap
* Automated PDF cyber risk report generation

## Technology Stack

* Python
* Flask
* Flask-CORS
* HTML5
* CSS3
* JavaScript
* REST API
* ReportLab

## Project Structure

```text
CyberTwinAI/
├── backend/
│   ├── app.py
│   ├── scoring.py
│   ├── attack_simulator.py
│   ├── llm_advisor.py
│   └── report_generator.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── reports/
├── requirements.txt
└── README.md
```

## How It Works

1. The user enters business information.
2. The user completes the cybersecurity assessment.
3. The frontend sends the assessment to the Flask REST API.
4. The backend calculates a cyber risk score.
5. Potential cyber attack scenarios are generated.
6. Security recommendations and a 90-day roadmap are produced.
7. The user can download a PDF assessment report.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd CyberTwinAI
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Backend

```bash
cd backend
python app.py
```

The Flask API should run at:

```text
http://127.0.0.1:5000
```

## Running the Frontend

Open:

```text
frontend/index.html
```

For development, Live Server can also be used.

## Current Limitations

Version 1 uses simplified, rule-based scoring and scenario simulation.

The maturity estimate should not be interpreted as an official ASD Essential Eight compliance assessment or certification.

The current recommendation engine is rule-based and does not yet use a production LLM integration.

## Version 2 Roadmap

Planned improvements include:

* Deeper ASD Essential Eight alignment
* React-based frontend
* User authentication
* Assessment history
* Database integration
* Interactive risk dashboards
* Improved cyber risk analytics
* LLM-assisted security guidance
* Cloud deployment

## Disclaimer

CyberTwin AI Version 1 is a prototype intended for educational, research and portfolio purposes. It does not constitute formal cybersecurity certification, penetration testing, legal advice or a guarantee against cyber incidents.

