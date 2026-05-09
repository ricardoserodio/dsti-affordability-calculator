# Usage Guide

## Purpose of This Guide

This guide explains how to use the **DSTI Affordability Calculator** as an educational and portfolio-oriented simulation tool.

The project is designed to help users understand how income, existing credit commitments, proposed instalments, stressed instalments, LTV assumptions and maturity scenarios may affect financial affordability.

This tool does not approve or reject credit, provide financial advice or replace formal banking analysis.

All values used in this project should be fictional, simulated or anonymised.

---

## Important Disclaimer

The **DSTI Affordability Calculator** is for educational, demonstrative and portfolio purposes only.

It must not be interpreted as:

- a credit approval system;
- a lending decision engine;
- an underwriting model;
- a financial advisory tool;
- a guarantee of eligibility;
- a replacement for human credit analysis;
- a representation of any bank's internal credit policy.

The outputs are indicative simulation results only.

---

## Running the Project Locally

To run the project locally, first clone the repository:

```bash
git clone https://github.com/ricardoserodio/dsti-affordability-calculator.git
cd dsti-affordability-calculator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

---

## Running the Tests

The project includes unit tests for the main calculation and validation modules.

To run the tests locally:

```bash
pytest tests/
```

The tests cover:

- DSTI calculation logic;
- income calculation logic;
- LTV calculation logic;
- maturity validation logic;
- input validation rules;
- scenario engine outputs.

The repository also includes a GitHub Actions workflow that runs the tests automatically when changes are pushed to the `main` branch.

---

## Main Simulation Inputs

The application may ask for the following fictional or simulated inputs:

```text
Monthly net income — Source 1
Monthly net income — Source 2
Existing monthly credit commitments
Proposed monthly instalment
Stressed monthly instalment
Configured DSTI threshold
Simulated loan amount
Simulated acquisition value
Simulated valuation value
Configured LTV threshold
Simulated loan maturity
Fictional or anonymised current age
Configured maximum age assumption
```

Users should not enter real personal, financial or sensitive data.

---

## Income Inputs

The income section allows users to simulate one or more income sources.

Example:

```text
Monthly net income — Source 1: €1,500
Monthly net income — Source 2: €1,000
Total monthly net income: €2,500
```

The app may also include a conservative income assumption.

Example:

```text
Total monthly net income: €2,500
Conservative factor: 90%
Conservative income: €2,250
```

This helps demonstrate how affordability changes when income is adjusted prudently.

---

## Credit Commitment Inputs

The credit commitment section includes:

```text
Existing monthly credit commitments
Proposed monthly instalment
Stressed monthly instalment
```

Example:

```text
Existing monthly credit commitments: €300
Proposed monthly instalment: €650
Stressed monthly instalment: €780
```

The stressed instalment should normally be equal to or higher than the proposed instalment.

If the stressed instalment is lower than the proposed instalment, the validation layer may flag this as an unusual assumption.

---

## DSTI Calculation

The simplified DSTI formula used in this project is:

```text
DSTI (%) =
((Existing Monthly Credit Commitments + Proposed Monthly Instalment)
/
Monthly Net Income) × 100
```

Example:

```text
Monthly net income: €2,500
Existing commitments: €300
Proposed instalment: €650

DSTI = (300 + 650) / 2,500 × 100
DSTI = 38.0%
```

This means that, in this simulated scenario, 38% of monthly net income is allocated to debt payments.

This is not a credit decision.

---

## Stressed DSTI Calculation

The stressed DSTI uses the stressed monthly instalment.

Formula:

```text
Stressed DSTI (%) =
((Existing Monthly Credit Commitments + Stressed Monthly Instalment)
/
Monthly Net Income) × 100
```

Example:

```text
Monthly net income: €2,500
Existing commitments: €300
Stressed instalment: €780

Stressed DSTI = (300 + 780) / 2,500 × 100
Stressed DSTI = 43.2%
```

This helps users understand how affordability may change under less favourable assumptions.

---

## Remaining Repayment Capacity

The calculator may estimate an indicative remaining repayment capacity using a configured DSTI threshold.

Formula:

```text
Maximum Monthly Debt Service =
Monthly Net Income × Configured DSTI Threshold
```

Then:

```text
Remaining Repayment Capacity =
Maximum Monthly Debt Service - Existing Monthly Credit Commitments
```

Example:

```text
Monthly net income: €2,500
Configured DSTI threshold: 40%
Existing commitments: €300

Maximum monthly debt service = €1,000
Remaining repayment capacity = €700
```

This is an educational simulation output only.

It must not be interpreted as approved borrowing capacity.

---

## Margin Against Stressed Instalment

The calculator may compare remaining repayment capacity with the stressed instalment.

Formula:

```text
Margin Against Stressed Instalment =
Remaining Repayment Capacity - Stressed Monthly Instalment
```

Example:

```text
Remaining repayment capacity: €700
Stressed instalment: €780

Margin = -€80
```

A negative margin may indicate that the stressed instalment exceeds the configured simulation threshold.

This is a risk awareness indicator, not a credit decision.

---

## LTV Simulation

The app may include a simplified Loan-to-Value simulation.

Formula:

```text
LTV (%) = Loan Amount / Property Value × 100
```

Example:

```text
Loan amount: €180,000
Property value used: €215,000

LTV = 180,000 / 215,000 × 100
LTV = 83.72%
```

The property value used may be:

```text
Acquisition value
Valuation value
Lower of acquisition and valuation value
```

Any LTV threshold used in the app is a configurable simulation assumption only.

It is not a formal lending rule.

---

## Maturity Simulation

The maturity simulation estimates the age at the end of a simulated loan.

Formula:

```text
Age at End of Loan =
Current Age + Loan Maturity in Years
```

Example:

```text
Current age: 35
Loan maturity: 30 years

Age at end of loan: 65
```

This check is educational and must not be interpreted as an eligibility decision.

---

## Scenario Comparison

The app may compare scenarios such as:

```text
Base simulation
Prudent income simulation
Higher commitment scenario
Higher stress scenario
Lower income scenario
Higher LTV scenario
Longer maturity scenario
Older borrower scenario
High DSTI scenario
Data quality review scenario
```

The goal is to show how different assumptions affect affordability indicators.

---

## Validation Warnings

The validation layer may identify issues such as:

```text
Missing values
Negative values
Zero income
Invalid percentages
Unrealistic income assumptions
High existing commitments
High proposed instalment
Stressed instalment lower than proposed instalment
High DSTI
High LTV
High age at end of loan
Incomplete assumptions
```

Validation warnings are educational indicators.

They are not credit decisions, eligibility checks or financial advice.

---

## Blocking Errors

Some validation issues may prevent calculation.

Examples:

```text
Monthly net income is missing
Monthly net income is zero
Proposed instalment is negative
DSTI threshold is outside the 0% to 100% range
Property value is zero when LTV is requested
Loan amount is zero when LTV is requested
```

Blocking errors are designed to prevent misleading outputs.

---

## Recommended Interpretation

Outputs should be interpreted cautiously.

Preferred interpretation:

```text
The scenario shows a specific affordability position under the configured simulation assumptions.
```

Avoid interpretation such as:

```text
The credit is approved.
The user is eligible.
The bank would accept this case.
The user should take this loan.
```

The project is focused on financial literacy, data validation, explainability and risk awareness.

---

## Privacy Notice

This project does not request, store, process or analyse real personal documents.

Users should only input fictional, simulated or anonymised values.

References to payslips, tax returns, credit responsibility maps or loan simulations are educational only.

The application does not perform:

```text
OCR
Document verification
Client onboarding
Credit approval
Formal banking validation
```

---

## Suggested Workflow for Users

Recommended workflow:

```text
1. Read the educational disclaimer.
2. Enter fictional income assumptions.
3. Enter fictional existing credit commitments.
4. Enter proposed and stressed instalments.
5. Configure DSTI assumptions.
6. Optionally include LTV assumptions.
7. Optionally include maturity assumptions.
8. Review validation warnings.
9. Review DSTI, LTV and maturity outputs.
10. Compare base and prudent scenarios.
11. Read limitations before interpreting the output.
```

---

## Summary

The **DSTI Affordability Calculator** is designed to support responsible financial simulation.

It helps demonstrate how income, debt commitments, instalments, stress assumptions, LTV and maturity can affect affordability.

The tool is educational, explainable and portfolio-oriented.

It must never be interpreted as a credit decision engine, financial advice tool or replacement for human banking analysis.
