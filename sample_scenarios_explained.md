# Sample Scenarios Explained

## Purpose of This Document

This document explains the fictional sample scenarios included in:

```text
examples/sample_scenarios.csv
```

The purpose of the sample scenarios is to demonstrate how the **DSTI Affordability Calculator** behaves under different simulated affordability conditions.

These scenarios are:

```text
Fictional
Educational
Simulated
Portfolio-oriented
Not based on real client data
Not based on confidential banking information
```

They must not be interpreted as credit decisions, financial advice, lending recommendations or bank policy rules.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

```text
DSTI analysis
Affordability simulation
Interest rate sensitivity
LTV awareness
Maturity awareness
Financial data validation
Explainability
Risk awareness
Human-in-the-loop interpretation
```

The sample scenarios help demonstrate these concepts using controlled fictional inputs.

---

## Dataset Location

The sample scenarios are stored in:

```text
examples/sample_scenarios.csv
```

They can be loaded using:

```text
src/sample_scenario_loader.py
```

The loader validates whether the CSV contains the expected columns before using it for educational demonstration.

---

## Required Columns

The sample scenario dataset is expected to include the following columns:

```text
scenario_name
income_source_1
income_source_2
use_conservative_income
conservative_factor
existing_monthly_commitments
loan_amount
loan_maturity_years
euribor_tenor
simulated_euribor_percentage
simulated_spread_percentage
stress_buffer_percentage
acquisition_value
valuation_value
configured_dsti_threshold_percentage
configured_ltv_threshold_percentage
current_age
configured_maximum_age_at_end
scenario_note
```

These columns allow the project to demonstrate:

```text
Income assumptions
Existing credit commitments
Loan amount assumptions
Maturity assumptions
Simulated EURIBOR assumptions
Simulated spread assumptions
Interest rate stress assumptions
LTV assumptions
Age-at-end-of-loan assumptions
Scenario-level explanation
```

---

## Base Educational Simulation

The base scenario represents a standard fictional affordability simulation.

Example assumptions:

```text
Monthly net income source 1: €1,500
Monthly net income source 2: €1,000
Existing monthly commitments: €300
Loan amount: €180,000
Maturity: 30 years
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
DSTI threshold: 40%
LTV threshold: 90%
Current age: 35
Maximum age at end assumption: 75
```

Purpose:

```text
Demonstrate the normal flow of the calculator.
```

This scenario is useful as the default educational reference case.

---

## Prudent Income Simulation

This scenario applies a conservative income factor.

Example:

```text
Income sources: €1,500 + €1,000
Conservative factor: 0.90
```

This means the simulation may use only 90% of the income assumption.

Purpose:

```text
Show how affordability indicators change when income is treated more prudently.
```

This is useful for demonstrating risk awareness and sensitivity analysis.

---

## Higher Commitments Simulation

This scenario increases existing monthly commitments.

Example:

```text
Existing monthly commitments: €600
```

Purpose:

```text
Show how existing credit commitments may increase DSTI and reduce remaining repayment capacity.
```

This scenario is useful because DSTI is directly affected by existing monthly debt payments.

---

## Higher Interest Stress Simulation

This scenario increases the interest rate stress buffer.

Example:

```text
Stress buffer: 2.50%
```

Purpose:

```text
Show how a larger interest rate stress assumption may increase the stressed instalment and stressed DSTI.
```

This scenario demonstrates interest rate sensitivity.

---

## Lower Income Simulation

This scenario reduces income assumptions.

Example:

```text
Monthly net income source 1: €1,200
Monthly net income source 2: €800
```

Purpose:

```text
Show how lower income may increase affordability pressure.
```

This scenario helps demonstrate that affordability is sensitive not only to loan conditions, but also to income assumptions.

---

## Higher LTV Simulation

This scenario increases the simulated loan amount.

Example:

```text
Loan amount: €205,000
Acquisition value: €220,000
Valuation value: €215,000
```

Purpose:

```text
Show how a higher loan amount may increase LTV and affect estimated instalments.
```

This is useful for demonstrating how loan amount affects both collateral-related and repayment-related indicators.

---

## Longer Maturity Simulation

This scenario uses a longer maturity.

Example:

```text
Loan maturity: 40 years
```

Purpose:

```text
Show how longer maturity may reduce estimated monthly instalments but increase maturity-related risk awareness.
```

Longer maturities can make monthly payments appear lower, but they may increase total repayment and age-at-end-of-loan considerations.

---

## Older Borrower Simulation

This scenario increases the fictional current age.

Example:

```text
Current age: 55
Maturity: 30 years
Maximum age at end assumption: 75
```

Purpose:

```text
Show how age at end of loan can trigger maturity-related review notes.
```

This scenario is included for educational risk awareness only.

It must not be interpreted as a real bank policy rule or credit decision.

---

## Negative EURIBOR Simulation

This scenario uses a negative simulated EURIBOR assumption.

Example:

```text
Simulated EURIBOR: -0.50%
Simulated spread: 1.00%
```

Purpose:

```text
Show how the project handles a negative EURIBOR assumption as a data quality note.
```

Negative EURIBOR assumptions may be valid for educational historical scenario analysis, but they should be reviewed before interpretation.

---

## Zero Stress Buffer Simulation

This scenario sets the stress buffer to zero.

Example:

```text
Stress buffer: 0.00%
```

Purpose:

```text
Show how the simulation behaves when no additional interest rate stress is applied.
```

This scenario is useful for demonstrating the difference between base assumptions and stressed assumptions.

---

## How Scenarios Support Portfolio Value

The sample scenarios strengthen the project because they demonstrate:

```text
Scenario analysis
Financial sensitivity analysis
DSTI interpretation
LTV interpretation
Maturity risk awareness
Interest rate stress testing
Financial data quality validation
Structured fictional dataset handling
Explainable banking-inspired logic
```

This makes the project more relevant for roles such as:

```text
Banking Analytics
Financial Data Quality Analyst
Data Validation Analyst
Credit Risk Analyst
Financial Research Support
AI Finance Evaluation
Fintech Product Analyst
Reporting Analyst - Banking
```

---

## Data Quality Considerations

The sample scenario dataset should be validated before use.

Important checks include:

```text
Missing required columns
Missing scenario names
Missing income values
Negative or unrealistic income values
Negative commitments
Invalid maturity values
Invalid EURIBOR tenor
Unusually high EURIBOR values
Negative spread values
Negative stress buffer values
Invalid LTV inputs
Invalid age assumptions
Empty scenario dataset
```

The project includes a loader module to support structural validation:

```text
src/sample_scenario_loader.py
```

And unit tests:

```text
tests/test_sample_scenario_loader.py
```

---

## Responsible Use

The sample scenarios should only be used for:

```text
Educational demonstration
Portfolio presentation
Testing
Documentation
Scenario analysis examples
Financial literacy explanations
```

They should not be used for:

```text
Real client analysis
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

The sample scenarios must never include:

```text
Real client names
Real tax numbers
Real salaries
Real bank account information
Real loan contracts
Real credit responsibility maps
Real personal financial documents
Internal bank policy information
Confidential banking data
```

All values should remain fictional, simulated or anonymised.

---

## Human-in-the-Loop Principle

The scenarios are designed to support human interpretation.

A human reviewer should consider:

```text
Whether the assumptions are coherent
Whether the results appear unusually high or low
Whether the scenario demonstrates a meaningful risk factor
Whether the output is being interpreted responsibly
Whether the limitations are clearly understood
```

The calculator supports analysis.

It does not replace judgement.

---

## Summary

The sample scenarios provide a controlled fictional dataset for demonstrating the **DSTI Affordability Calculator**.

They help show how changes in income, commitments, loan amount, maturity, EURIBOR, spread and stress assumptions can affect affordability indicators.

All scenarios are educational only and must never be interpreted as credit decisions, financial advice or bank policy rules.
