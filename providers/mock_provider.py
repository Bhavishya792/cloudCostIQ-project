import random


class MockCostProvider:

    def get_data(self):

        ec2 = round(random.uniform(25, 75), 2)
        s3 = round(random.uniform(5, 25), 2)
        rds = round(random.uniform(10, 40), 2)
        lambda_cost = round(random.uniform(1, 10), 2)
        cloudfront = round(random.uniform(2, 15), 2)

        services = {
            "EC2": ec2,
            "S3": s3,
            "RDS": rds,
            "Lambda": lambda_cost,
            "CloudFront": cloudfront,
        }

        current_cost = round(sum(services.values()), 2)

        projected_cost = round(current_cost * 1.15, 2)

        budget = 100

        budget_status = (
            "Exceeded"
            if projected_cost > budget
            else "Under Budget"
        )

        trend = [
            round(random.uniform(50, 150), 2)
            for _ in range(6)
        ]

        recommendations = []

        if ec2 > 40:
            recommendations.append(
                "Review low-utilization EC2 instances."
            )

        if s3 > 15:
            recommendations.append(
                "Enable S3 lifecycle policies."
            )

        if rds > 20:
            recommendations.append(
                "Consider Reserved Database Instances."
            )

        recommendations.append(
            "Delete unattached EBS volumes."
        )

        return {
            "services": services,
            "current_cost": current_cost,
            "projected_cost": projected_cost,
            "budget": budget,
            "budget_status": budget_status,
            "trend": trend,
            "recommendations": recommendations,
        }