import os
import csv
import io

from flask import (
    Flask,
    render_template,
    Response,
)

from dotenv import load_dotenv

from providers.aws_provider import (
    AWSCostProvider,
)

from providers.mock_provider import (
    MockCostProvider,
)

from datetime import datetime

load_dotenv()

app = Flask(__name__)


def get_provider():

    aws_key = os.getenv("AWS_ACCESS_KEY_ID")

    aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")

    if aws_key and aws_secret:

        try:

            provider = AWSCostProvider()

            provider.get_data()

            return provider

        except Exception:

            pass

    return MockCostProvider()


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/dashboard")
def dashboard():

    provider = get_provider()

    data = provider.get_data()
    current_cost = data["current_cost"]
    budget = data["budget"]

    estimated_savings = round(current_cost * 0.15, 2)

    budget_percent = round((current_cost / budget) * 100, 1)

    mode = provider.__class__.__name__

    return render_template(
        "dashboard.html",
        services=data["services"],
        current_cost=data["current_cost"],
        projected_cost=data["projected_cost"],
        budget=data["budget"],
        budget_status=data["budget_status"],
        trend=data["trend"],
        recommendations=data["recommendations"],
        budget_percent=budget_percent,
        estimated_savings=estimated_savings,
        mode=mode,
    )


@app.route("/export")
def export_report():

    provider = get_provider()

    data = provider.get_data()

    report = []

    report.append("CloudCostIQ Cost Report")
    report.append("=" * 40)

    report.append(f"Generated: {datetime.now().strftime('%d %B %Y %H:%M')}")

    report.append("")

    report.append(f"Current Cost: ${data['current_cost']}")

    report.append(f"Projected Cost: ${data['projected_cost']}")

    report.append(f"Budget: ${data['budget']}")

    report.append(f"Status: {data['budget_status']}")

    report.append("")
    report.append("SERVICE BREAKDOWN")
    report.append("-" * 40)

    for service, cost in data["services"].items():

        report.append(f"{service:<15} ${cost}")

    report.append("")
    report.append("OPTIMIZATION RECOMMENDATIONS")
    report.append("-" * 40)

    for item in data["recommendations"]:

        report.append(f"• {item}")

    content = "\n".join(report)

    return Response(
        content,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=cloudcostiq-report.txt"},
    )


if __name__ == "__main__":

    app.run(debug=True)
