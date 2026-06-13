import boto3
import os
from datetime import date, timedelta


class AWSCostProvider:

    def __init__(self):

        self.client = boto3.client(
            "ce",
            aws_access_key_id=os.getenv(
                "AWS_ACCESS_KEY_ID"
            ),
            aws_secret_access_key=os.getenv(
                "AWS_SECRET_ACCESS_KEY"
            ),
            region_name="us-east-1",
        )

    def get_data(self):

        end_date = date.today()

        start_date = end_date - timedelta(days=30)

        response = self.client.get_cost_and_usage(

            TimePeriod={
                "Start": start_date.isoformat(),
                "End": end_date.isoformat(),
            },

            Granularity="MONTHLY",

            Metrics=["UnblendedCost"],

            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE",
                }
            ],
        )

        services = {}

        for item in response["ResultsByTime"][0]["Groups"]:

            service_name = item["Keys"][0]

            cost = float(
                item["Metrics"][
                    "UnblendedCost"
                ]["Amount"]
            )

            if cost > 0:

                services[service_name] = round(
                    cost,
                    2,
                )

        current_cost = round(
            sum(services.values()),
            2,
        )

        projected_cost = round(
            current_cost * 1.15,
            2,
        )

        budget = 100

        budget_status = (
            "Exceeded"
            if projected_cost > budget
            else "Under Budget"
        )

        trend = [
            current_cost * 0.7,
            current_cost * 0.8,
            current_cost * 0.9,
            current_cost * 1.0,
            current_cost * 1.1,
            current_cost,
        ]

        recommendations = [

            "Review unused resources.",

            "Enable S3 lifecycle policies.",

            "Consider Reserved Instances.",

        ]

        return {

            "services": services,

            "current_cost": current_cost,

            "projected_cost": projected_cost,

            "budget": budget,

            "budget_status": budget_status,

            "trend": trend,

            "recommendations": recommendations,
        }