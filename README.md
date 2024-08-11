# 🚀 FoxHome Automation Suite

## 📌 Project Overview
This project is a comprehensive automation suite for Fox Home, designed to validate its UI and API functionalities.
By utilizing industry-standard tools, the suite ensures the stability and performance of Fox Home essential features.

## 🔑 Features
- *UI Automation*: Leveraging Selenium WebDriver to automate Fox Home’s user interface.
- *API Testing*: Testing Fox Home API endpoints.
- *Integrated Reporting*: Detailed test reports generated through the Allure framework.
- *Jira Integration*: Seamless test management via Jira.

## 🎯 Test Scope
- *UI Tests*: Verifying core functionalities of Fox Home’s user interface.
- *API Tests*: Validating critical endpoints of the Fox Home API.
- *Combined Tests*: Demonstrating UI and API integration through combined test cases.

## 🛠️ Setup Instructions

 *Clone the Repository*:
bash
git clone https://github.com/jameel98/5-Tech-FinalProject


## 🛠️ Tools and Technologies
- IDE: PyCharm 2024.1.1
- Automation Framework: Selenium 4.22.0
- Programming Language: Python 3.8+
- Browser: Google Chrome 126.0.6478.127
- API Testing: Requests library
- Test Framework: Pytest
- Reporting: Allure Framework
- Version Control: Git
- Bug Tracking: Jira

## 📊 Allure Reporting

*To use Allure reporting*:

Install Allure:

bash
npm install -g allure-commandline


Run Tests and Serve Report:

bash
pytest --alluredir=./reports
allure serve reports
