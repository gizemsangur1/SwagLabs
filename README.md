# SwagLabs UI Test Automation Project

This project is built to perform UI test automation on the SauceDemo e-commerce demo website. It uses Python, Selenium, Pytest, Page Object Model (POM), and Allure Report to establish a professional-grade test automation framework.

## ✨ Technologies Used

Python 3.10

Selenium WebDriver

Pytest

Page Object Model (POM) architecture

Allure Report for test reporting

Chrome WebDriver (with automation configurations)

## ⚡ Setup

Install required packages:
pip install -r requirements.txt

Ensure ChromeDriver is installed and added to system PATH.

Run tests:
python -m pytest -v --alluredir=allure-results

Serve Allure report:
allure serve allure-results

## 📆 Test Scenarios Implemented

1. Successful login

2. Invalid password login

3. Logout from menu

4. Add product to cart and verify

## 🛠️ Browser Configuration (Chrome)

To prevent Chrome from showing security popups like "your password may be at risk", ChromeOptions were configured with:

Incognito mode (--incognito)

Disabling password manager

Disabling automation detection and infobars

## 📊 Allure Reporting

Test results are saved in allure-results directory. View interactive HTML reports via:
allure serve allure-results

## 🚀 Upcoming: Jenkins CI/CD Integration

Jenkins support will be added to automate test runs and generate Allure reports upon each code update.
