# Saucedemo Playwright Automation Framework (Python + Pytest + POM)

This repository contains an end-to-end automation framework for testing [saucedemo.com](https://www.saucedemo.com/) using **Playwright**, **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.  
The framework supports **Allure reporting**, **negative/positive test cases**, and **secure credential management** with `.env`.

---

## 📂 Project Structure


## Following is the setup guide and required commands

- python3 --version
- python3 -m venv venv (install virtual env)
- source venv/bin/activate (activate virtual env)
- pip install playwright pytest pytest-playwright allure-pytest (install allure, pytest)
- pip install playwrigt (If want to install only playwright)
- brew install allure (install allure report for the first time)
- playwright install (install playwright)
- pytest (run all tests)
- allure serve allure-results (start the allure server and get the results in report)
- python app.py (to execute app.py python file)
- browser = p.chromium.launch(headless=False, slow_mo=2000) [To slow the execution in coftest.py file]
- pip install python-dotenv (This will allow Python to read .env files)

## Refresh auto complete engine (Language server) of VS code:
1. Cmd+Shift+P
2. Python: Restart Language Server → Select it
