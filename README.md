# DSTI Affordability Calculator

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-lightgrey)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20Simulation-informational)

## Project Overview

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

- Debt Service-to-Income analysis;
- repayment capacity simulation;
- interest rate stress testing;
- simulated EURIBOR and spread assumptions;
- Loan-to-Value awareness;
- maturity and age-at-end-of-loan awareness;
- financial data validation;
- explainability;
- responsible financial simulation;
- human-in-the-loop interpretation.

The project is designed as a professional portfolio project for financial data analysis, banking analytics, credit risk awareness, data quality validation and AI finance evaluation.

It is not a credit approval system, lending decision engine, underwriting model, bank pricing tool or financial advisory application.

---

## Live Demo

Streamlit app:

```text
Coming soon
```

---

## Screenshot

```text
Screenshot coming soon after deployment.
```

---

## Professional Positioning

This project demonstrates a full banking-inspired affordability simulation workflow:

```text
Financial calculations
DSTI analysis
Loan payment estimation
Interest rate stress testing
Simulated EURIBOR + spread assumptions
LTV checks
Maturity checks
Scenario analysis
Sample scenario validation
Financial data quality controls
Automated unit tests
Explainable documentation
Responsible use disclaimers
```

It is especially relevant for roles such as:

```text
Banking Analytics
Financial Data Quality Analyst
Data Validation Analyst
Credit Risk Analyst
Financial Analyst
AI Finance Evaluation
Fintech Product Analyst
Reporting Analyst - Banking
```

---

## What This Project Does

The calculator allows users to simulate fictional affordability scenarios using inputs such as:

- monthly net income;
- existing monthly credit commitments;
- simulated loan amount;
- simulated maturity;
- simulated EURIBOR assumption;
- simulated spread assumption;
- interest rate stress buffer;
- property acquisition value;
- property valuation value;
- configured DSTI threshold;
- configured LTV threshold;
- fictional or anonymised current age.

The app then calculates and explains:

- base DSTI;
- stressed DSTI;
- estimated base monthly instalment;
- estimated stressed monthly instalment;
- monthly payment increase;
- remaining repayment capacity;
- margin against stressed instalment;
- LTV;
- age at end of loan;
- validation warnings;
- scenario comparison.

---

## What This Project Is Not

This project is not:

- a credit approval tool;
- a credit rejection tool;
- a lending decision engine;
- an underwriting system;
- a bank pricing model;
- a real-time EURIBOR data platform;
- a financial advisory tool;
- a replacement for formal human credit analysis;
- a representation of any bank's internal credit policy.

The outputs are educational and indicative only.

---

## Key Features

### DSTI Calculation

The project calculates Debt Service-to-Income using:

```text
DSTI = (Existing Monthly Commitments + Monthly Instalment) / Monthly Net Income × 100
```

It includes both:

```text
Base DSTI
Stressed DSTI
```

---

### Loan Payment Calculation

The project estimates monthly loan payments using a simplified amortising loan formula.

Inputs include:

```text
Loan amount
Annual interest rate assumption
Loan maturity
```

The result is used to support DSTI and interest rate sensitivity analysis.

---

### Interest Rate Builder

The project separates interest rate assumptions into:

```text
Simulated EURIBOR
Simulated spread
Stress buffer
```

Formula:

```text
Base Annual Interest Rate =
Simulated EURIBOR + Simulated Spread
```

Formula:

```text
Stressed Annual Interest Rate =
Base Annual Interest Rate + Stress Buffer
```

This makes the simulation more realistic and explainable while remaining educational.

---

### Manual EURIBOR Reference Handling

The project includes a manual EURIBOR reference provider.

It supports:

```text
EURIBOR tenor selection
Manual EURIBOR assumption
Source label
Optional reference date
Data quality interpretation
```

The EURIBOR value is not live market data.

It is a manual simulated assumption used for educational scenario analysis.

---

### Interest Rate Stress Testing

The calculator estimates the impact of a higher stressed interest rate on:

```text
Estimated monthly instalment
Monthly payment increase
Monthly payment increase percentage
Total repayment increase
Stressed DSTI
```

This supports risk awareness and affordability sensitivity analysis.

---

### LTV Awareness

The project calculates a simplified Loan-to-Value indicator:

```text
LTV = Loan Amount / Property Value × 100
```

The app can use either:

```text
Acquisition value
Valuation value
Lower of acquisition and valuation value
```

This is for educational risk awareness only.

---

### Maturity Awareness

The project estimates:

```text
Age at end of loan = Current age + Loan maturity
```

This helps demonstrate maturity-related risk awareness.

It must not be interpreted as a real bank policy rule.

---

### Financial Data Validation

The project includes validation checks for:

```text
Missing values
Negative values
Zero income
Unrealistic income assumptions
Unrealistic commitment assumptions
Invalid percentages
Invalid LTV inputs
Invalid maturity inputs
Incoherent stressed scenarios
Extreme DSTI outputs
Missing sample scenario columns
Invalid EURIBOR tenors
```

Validation is a central part of the project.

---

### Sample Scenario Dataset

The repository includes fictional sample scenarios in:

```text
examples/sample_scenarios.csv
```

These scenarios demonstrate:

```text
Base affordability simulation
Prudent income simulation
Higher commitments simulation
Higher interest stress simulation
Lower income simulation
Higher LTV simulation
Longer maturity simulation
Older borrower simulation
Negative EURIBOR simulation
Zero stress buffer simulation
```

The dataset is validated through automated tests.

---

### Automated Tests

The project includes unit tests for:

```text
DSTI calculator
Income calculator
Loan payment calculator
Interest rate builder
Interest rate stress testing
EURIBOR provider
LTV calculator
Maturity validator
Scenario engine
Validation checks
Sample scenario loader
Actual sample scenarios CSV
Application import smoke tests
```

Tests run automatically through GitHub Actions.

---

## Project Structure

```text
.github/
└── workflows/
    └── python-tests.yml

.streamlit/
└── config.toml

app/
└── streamlit_app.py

examples/
└── sample_scenarios.csv

src/
├── __init__.py
├── dsti_calculator.py
├── euribor_provider.py
├── income_calculator.py
├── interest_rate_builder.py
├── interest_rate_stress.py
├── loan_payment_calculator.py
├── ltv_calculator.py
├── maturity_validator.py
├── sample_scenario_loader.py
├── scenario_engine.py
└── validation_checks.py

tests/
├── test_app_imports.py
├── test_dsti_calculator.py
├── test_euribor_provider.py
├── test_income_calculator.py
├── test_interest_rate_builder.py
├── test_interest_rate_stress.py
├── test_loan_payment_calculator.py
├── test_ltv_calculator.py
├── test_maturity_validator.py
├── test_sample_scenario_loader.py
├── test_sample_scenarios_csv.py
├── test_scenario_engine.py
└── test_validation_checks.py
```

---

## Documentation

The repository includes documentation for:

```text
README.md
disclaimer.md
methodology.md
financial_assumptions.md
data_validation_rules.md
dsti_formula_explained.md
loan_payment_formula_explained.md
interest_rate_builder_explained.md
interest_rate_stress_explained.md
euribor_assumptions_policy.md
scenario_analysis.md
sample_scenarios_explained.md
ui_mockup.md
usage_guide.md
deployment_guide.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ricardoserodio/dsti-affordability-calculator.git
cd dsti-affordability-calculator
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

---

## Running Tests

Run all tests:

```bash
pytest tests/
```

The project also uses GitHub Actions to run tests automatically on push and pull request.

---

## Example Simulation Logic

Example fictional inputs:

```text
Monthly net income: €2,500
Existing monthly commitments: €300
Loan amount: €180,000
Maturity: 30 years
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
Configured DSTI threshold: 40%
```

Base annual interest rate:

```text
3.00% + 0.90% = 3.90%
```

Stressed annual interest rate:

```text
3.90% + 1.50% = 5.40%
```

The app then estimates:

```text
Base monthly instalment
Stressed monthly instalment
Base DSTI
Stressed DSTI
Remaining repayment capacity
Margin against stressed instalment
```

All outputs are educational and indicative only.

---

## Responsible Use

This project should only be used for:

```text
Educational demonstration
Portfolio presentation
Financial literacy
Scenario analysis
Data validation practice
Banking analytics learning
AI finance evaluation practice
```

It should not be used for:

```text
Real client credit analysis
Credit approval
Credit rejection
Eligibility assessment
Bank pricing
Financial advice
Personal financial recommendations
Regulatory decision-making
```

---

## Privacy and Data Protection

The project does not require real personal data.

Users should not enter:

```text
Real names
Real tax numbers
Real bank account information
Real client identifiers
Real salaries
Real loan contracts
Real credit responsibility maps
Personal documents
Confidential bank information
Internal policy rules
```

All values should be fictional, simulated or anonymised.

---

## Human-in-the-Loop Principle

The calculator is designed to support human interpretation.

A human reviewer should consider:

```text
Whether assumptions are coherent
Whether values are realistic
Whether outputs are unusually high or low
Whether warnings require review
Whether limitations are clearly understood
Whether the result is being interpreted responsibly
```

The tool supports judgement.

It does not replace judgement.

---

## Limitations

The project uses simplified educational assumptions.

It does not model:

```text
APR/APRC
Bank fees
Insurance costs
Tax effects
Fixed-rate periods
Mixed-rate periods
Variable reset dates
Promotional campaigns
Bonified spreads
Employment stability
Credit history
Legal documentation
Regulatory requirements
Bank-specific credit policy
Formal affordability rules
```

---

## Technology Stack

```text
Python
Streamlit
pandas
NumPy
matplotlib
pytest
GitHub Actions
```

---

## Portfolio Value

This project demonstrates practical skills in:

```text
Financial analysis
Banking-inspired affordability logic
Credit risk awareness
Financial data validation
Scenario analysis
Python programming
Streamlit dashboard development
Unit testing
GitHub Actions
Technical documentation
Responsible AI and human-in-the-loop thinking
```

Suggested CV description:

```text
Built a banking-inspired DSTI affordability simulation tool using Python and Streamlit, including loan payment estimation, interest rate stress testing, simulated EURIBOR and spread assumptions, LTV and maturity checks, fictional scenario validation, automated unit tests and explainable documentation focused on financial literacy, data quality and risk awareness.
```

Short CV version:

```text
Developed a Python/Streamlit DSTI affordability calculator with interest rate stress testing, LTV/maturity checks, data validation, sample scenario testing and automated GitHub Actions.
```

---

## Author

**Ricardo Serôdio**  
Wisestrike Finance Lab

Professional background in banking, wealth management, retail banking operations, credit processes, AML/CFT, KYC/CDD and MiFID II.

This project is part of a professional portfolio focused on banking analytics, financial data quality, AI finance evaluation, fintech and responsible financial simulation.
