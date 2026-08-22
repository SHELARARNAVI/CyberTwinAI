document.getElementById("assessmentForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        business_name: document.getElementById("business_name").value,
        country: document.getElementById("country").value,
        industry: document.getElementById("industry").value,
        mfa: document.getElementById("mfa").value,
        backups: document.getElementById("backups").value,
        patching: document.getElementById("patching").value,
        admin_control: document.getElementById("admin_control").value,
        endpoint_security: document.getElementById("endpoint_security").value,
        staff_training: document.getElementById("staff_training").value,
        logging: document.getElementById("logging").value,
        incident_response: document.getElementById("incident_response").value
    };

    const response = await fetch("http://127.0.0.1:5000/assess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    let riskClass = "low";
    if (result.risk.risk_level === "High Risk") {
        riskClass = "high";
    } else if (result.risk.risk_level === "Medium Risk") {
        riskClass = "medium";
    }

    document.getElementById("result").innerHTML = `
        <h2>Assessment Result</h2>

        <div class="card">
            <p><b>Business:</b> ${result.business}</p>
            <p><b>Country:</b> ${result.country}</p>
            <p><b>Industry:</b> ${result.industry}</p>
        </div>

        <div class="card">
            <p><b>Risk Score:</b> ${result.risk.score} / ${result.risk.max_score}</p>
            <p><b>Risk Percentage:</b> ${result.risk.percentage}%</p>
            <p><b>Risk Level:</b> <span class="${riskClass}">${result.risk.risk_level}</span></p>
            <p><b>Maturity:</b> ${result.risk.maturity}</p>
        </div>

        <h3>Attack Simulation</h3>
        ${result.attacks.map(a => `
            <div class="card">
                <p><b>${a.attack}</b> - ${a.severity}</p>
                <p>${a.impact}</p>
            </div>
        `).join("")}

        <h3>Executive Summary</h3>
        <div class="card">
            <p>${result.advice.summary}</p>
            <p>${result.advice.business_impact}</p>
        </div>

        <h3>Recommendations</h3>
        <ul>
            ${result.advice.recommendations.map(r => `<li>${r}</li>`).join("")}
        </ul>

        <h3>90-Day Security Roadmap</h3>
        <ul>
            ${result.advice.roadmap.map(r => `<li>${r}</li>`).join("")}
        </ul>

        <a class="download-btn" href="http://127.0.0.1:5000/download-report" target="_blank">
            Download PDF Report
        </a>
    `;
});
