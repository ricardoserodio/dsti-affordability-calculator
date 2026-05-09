# DSTI Affordability Calculator

**Banking-inspired financial affordability and DSTI simulation tool focused on financial literacy, data validation, explainability and risk awareness.**

---

## Project Overview

The **DSTI Affordability Calculator** is an educational and portfolio-oriented financial simulation tool designed to help users understand how debt service, income, existing credit commitments and stress scenarios may affect financial affordability.

The project focuses on the concept of **DSTI — Debt Service-to-Income**, commonly used in banking and credit analysis to assess the relationship between monthly debt obligations and monthly income.

This tool is inspired by banking workflows, but it is not a credit approval system, underwriting engine, financial advisory tool or substitute for formal human credit analysis.

---

## Main Objectives

The main objectives of this project are to:

- calculate indicative DSTI ratios;
- simulate financial effort under different scenarios;
- compare current and potential future instalments;
- consider existing credit commitments;
- apply simple interest rate stress scenarios;
- validate financial inputs before calculation;
- identify potential affordability risk factors;
- explain assumptions and limitations clearly;
- promote financial literacy and responsible simulation use.

---

## What This Project Is

This project is:

- an educational financial affordability simulator;
- a DSTI calculation and explanation tool;
- a portfolio project for banking analytics and financial data quality;
- a demonstrative tool inspired by banking workflows;
- a practical example of explainable financial logic using Python.

---

## What This Project Is Not

This project is not:

- a credit approval engine;
- an automatic lending decision system;
- a financial advisory tool;
- a commercial underwriting model;
- a replacement for human credit analysis;
- a representation of any bank's internal credit policy;
- a guarantee of eligibility, approval or affordability.

---

## Key Features

Planned and/or implemented features include:

- monthly net income analysis;
- existing credit commitments input;
- proposed instalment simulation;
- DSTI calculation;
- stressed DSTI calculation;
- comparison between current and future financial effort;
- maturity and age-related scenario checks;
- LTV simulation;
- configurable assumptions;
- input validation;
- risk warning messages;
- explanatory outputs;
- Streamlit interface;
- sample fictional scenarios.

---

## DSTI Formula

The simplified DSTI formula used in this project is:

```text
DSTI = Total Monthly Debt Payments / Monthly Net Income
```

Where:

```text
Total Monthly Debt Payments =
Existing Monthly Credit Commitments + Proposed Monthly Instalment
```

The result is usually expressed as a percentage:

```text
DSTI (%) = (Total Monthly Debt Payments / Monthly Net Income) × 100
```

A stressed version may also be calculated by replacing the proposed instalment with a stressed or aggravated instalment.

---

## Example Interpretation

For example, if a fictional household has:

```text
Monthly net income: €2,500
Existing monthly credit commitments: €300
Proposed new instalment: €650
```

Then:

```text
DSTI = (300 + 650) / 2,500
DSTI = 950 / 2,500
DSTI = 38%
```

This means that, in this simulated scenario, 38% of monthly net income would be allocated to debt payments.

This result is only indicative and must not be interpreted as approval, rejection or financial advice.

---

## Financial Data Quality Focus

Financial data quality is a central part of this project.

The tool should validate inputs such as:

- missing values;
- negative values;
- unrealistic income levels;
- unrealistic expenses;
- invalid percentages;
- inconsistent maturities;
- incoherent credit scenarios;
- incomplete assumptions;
- extreme or unusual DSTI values.

The purpose is to demonstrate how financial simulations should include basic validation checks before producing outputs.

---

## Risk Awareness

The application should help users understand that affordability can be affected by several factors, including:

- lower income;
- higher existing debt commitments;
- higher interest rates;
- longer or shorter maturity assumptions;
- stressed instalment scenarios;
- unrealistic input assumptions;
- incomplete financial information.

The tool should explain why a scenario may present higher risk, without making a formal lending decision.

---

## Human-in-the-Loop Principle

This project follows a **human-in-the-loop** approach.

The calculator provides structured, explainable and educational outputs, but interpretation should remain cautious and contextual.

The tool does not automatically approve or reject any credit scenario.

---

## Privacy and Data Protection Notice

This project does not request, store, process or analyse real personal documents.

References to documents such as payslips, tax statements, credit responsibility maps or loan simulations are included solely for educational purposes, to explain the types of information commonly considered in affordability assessments.

Users should only input fictional, simulated or anonymised values.

This tool does not perform document verification, OCR, client onboarding, credit approval or formal banking validation.

---

## Supporting Documents — Educational Context Only

The application may reference common supporting documents typically used in banking affordability and credit viability analysis, such as:

- payslips or salary statements;
- annual tax returns;
- tax assessment statements;
- credit responsibility maps;
- proof of existing financial commitments;
- housing expense information;
- loan simulations;
- proof of additional income sources.

These references are purely educational and demonstrative.

The application must never request real documents, store sensitive personal information, process real client data or replace formal banking verification processes.

---

## Technology Stack

Planned technology stack:

- Python;
- Streamlit;
- pandas;
- NumPy;
- matplotlib;
- validation logic;
- optional Power BI integration.

---

## Proposed Project Structure

```text
dsti-affordability-calculator/
│
├── README.md
├── disclaimer.md
├── methodology.md
├── dsti_formula_explained.md
├── financial_assumptions.md
├── data_validation_rules.md
├── scenario_analysis.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── dsti_calculator.py
│   ├── income_calculator.py
│   ├── ltv_calculator.py
│   ├── maturity_validator.py
│   ├── validation_checks.py
│   └── scenario_engine.py
│
├── app/
│   └── streamlit_app.py
│
├── examples/
│   └── sample_scenarios.csv
│
└── tests/
    └── test_dsti_calculator.py
```

---

## Planned Modules

### `dsti_calculator.py`

Responsible for calculating:

- base DSTI;
- stressed DSTI;
- available repayment capacity;
- difference between configured threshold and simulated DSTI.

### `income_calculator.py`

Responsible for handling:

- monthly net income;
- aggregated household income;
- conservative income assumptions;
- fictional income examples.

### `ltv_calculator.py`

Responsible for calculating:

- indicative loan-to-value;
- acquisition value versus valuation value;
- configured LTV assumptions.

### `maturity_validator.py`

Responsible for checking:

- loan maturity;
- age at the end of the simulated contract;
- inconsistent maturity assumptions.

### `validation_checks.py`

Responsible for validating:

- missing values;
- negative inputs;
- unrealistic values;
- invalid percentages;
- incoherent scenarios.

### `scenario_engine.py`

Responsible for generating:

- base scenario;
- prudent scenario;
- stressed interest rate scenario;
- comparative affordability outputs.

---

## Disclaimer

This project is for educational, demonstrative and portfolio purposes only.

It does not provide financial advice, credit advice, lending recommendations or eligibility assessments.

The calculations, assumptions and outputs are simplified and should not be interpreted as a formal credit decision.

No real client data, confidential banking information or proprietary credit policy rules are used in this project.

All examples are fictional, simulated or anonymised.

---

## Professional Context

This project was created as part of a professional portfolio focused on:

- banking analytics;
- financial data quality;
- credit risk awareness;
- financial literacy;
- explainable financial simulations;
- responsible use of financial technology;
- Python applied to finance.

---

## Future Improvements

Possible future improvements include:

- Streamlit dashboard;
- visual DSTI breakdown;
- scenario comparison charts;
- configurable stress assumptions;
- sample fictional datasets;
- automated validation reports;
- exportable simulation summary;
- Power BI dashboard integration;
- unit tests for calculation logic.

---

## Author

Created by **Ricardo Serôdio** as part of the **Wisestrike Finance Lab** portfolio.

This project reflects professional interests in banking, financial analysis, credit processes, data validation, financial literacy and responsible financial simulations.
