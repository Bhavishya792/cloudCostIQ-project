# CloudCostIQ

CloudCostIQ is a cloud cost monitoring and optimization dashboard built using Flask and AWS Cost Explorer concepts.

The application provides cloud spending insights, cost forecasting, service-level cost analysis, budget tracking, and optimization recommendations through a clean web dashboard.

## Features

* Cloud cost monitoring
* Budget tracking
* Cost forecasting
* Service-wise cost breakdown
* Optimization recommendations
* Exportable cost reports
* AWS Cost Explorer integration support
* Automatic fallback to mock data for demonstration purposes

## Dashboard Capabilities

* Monthly cloud spending overview
* Budget utilization tracking
* Cost trend visualization
* Service breakdown analysis
* Potential savings estimation
* Cost optimization recommendations
* Report generation

## Tech Stack

* Python
* Flask
* AWS Cost Explorer API
* Boto3
* Chart.js
* HTML
* CSS

## Project Structure

cloudcostiq/

* app.py
* providers/

  * aws_provider.py
  * mock_provider.py
* templates/

  * home.html
  * dashboard.html
* static/

  * css/
  * js/

## Screenshots

### Home Page

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0e304ffb-ad5a-431c-9fde-3604b1cb2dbf" />

### Dashboard

<img width="1921" height="2116" alt="home page" src="https://github.com/user-attachments/assets/0b685322-dcc4-4f2f-bfd9-a2d30cd8d555" />

### Export Report

<img width="1000" height="469" alt="image" src="https://github.com/user-attachments/assets/5e446b13-ad7f-48a6-b8b4-b1360a1ab9f3" />

## Author

Bhavishya Garg

Developed as a personal cloud computing project during the CodeC Technologies internship.

## Future Improvements

* Real-time AWS Cost Explorer integration
* Multi-cloud support
* Advanced forecasting models
* User authentication
* Historical report storage
