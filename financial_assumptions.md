# Financial Assumptions

## Purpose of This Document

This document defines the main financial assumptions used in the **DSTI Affordability Calculator**.

The purpose is to make the simulation transparent, explainable and easy to review.

All assumptions in this project are educational and configurable. They do not represent official banking rules, regulatory limits, internal credit policies or financial advice.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool.

It is designed to help users understand how income, existing credit commitments, proposed instalments and stress scenarios may affect financial effort.

The tool must not be interpreted as:

- a credit approval system;
- a lending decision engine;
- an underwriting model;
- a financial advisory tool;
- a guarantee of eligibility;
- a replacement for human credit analysis.

---

## Data Assumption

All data used in this project must be:

- fictional;
- simulated;
- anonymised;
- manually entered for educational purposes.

The project must not use real client data, confidential banking information, internal policy rules or sensitive personal information.

Users should not input real personal financial data.

---

## Monthly Net Income

The main income assumption used in the DSTI calculation is **monthly net income**.

Monthly net income represents the amount available after taxes and mandatory deductions.

Example:

```text
Monthly net income: €2,500
```

In future versions, the project may support:

- individual income;
- household income;
- multiple income sources;
- conservative income assumptions;
- manually adjusted income;
- simulated additional income.

The tool should always make clear which income value is being used.

---

## Existing Credit Commitments

Existing credit commitments represent current monthly debt payments.

Examples may include fictional or simulated values for:

- existing mortgage instalments;
- personal loans;
- car loans;
- credit card repayment assumptions;
- other recurring credit commitments.

Example:

```text
Existing monthly credit commitments: €300
```

These values are added to the proposed instalment to calculate total monthly debt payments.

---

## Proposed Instalment

The proposed instalment represents the estimated monthly payment of a new simulated credit scenario.

Example:

```text
Proposed monthly instalment: €650
```

The proposed instalment may be entered manually or calculated in future versions through a simplified loan payment formula.

It must not be interpreted as a formal loan quote, approval, offer or recommendation.

---

## Stressed Instalment

The stressed instalment represents a more prudent scenario where the monthly instalment increases.

Example:

```text
Base proposed instalment: €650
Stressed instalment: €780
```

This assumption may be used to simulate the effect of:

- higher interest rates;
- less favourable repayment conditions;
- conservative affordability testing;
- additional risk awareness.

The stressed instalment should generally be equal to or higher than the base proposed instalment.

If the stressed instalment is lower than the base instalment, the tool should flag this as a potential inconsistency unless clearly justified.

---

## DSTI Threshold

The calculator may use a configured DSTI threshold to estimate indicative repayment capacity.

Example:

```text
Configured DSTI threshold: 40%
```

This threshold is a simulation parameter only.

It must not be presented as:

- an official regulatory limit;
- a bank-specific rule;
- a credit approval condition;
- a guarantee of viability.

The threshold exists only to support educational scenario analysis.

---

## Base DSTI

Base DSTI is calculated using:

```text
Existing Monthly Credit Commitments + Proposed Monthly Instalment
```

Formula:

```text
Base DSTI (%) =
((Existing Monthly Credit Commitments + Proposed Monthly Instalment)
/
Monthly Net Income) × 100
```

Example:

```text
Existing commitments: €300
Proposed instalment: €650
Monthly net income: €2,500

Base DSTI = (300 + 650) / 2,500 × 100
Base DSTI = 38%
```

---

## Stressed DSTI

Stressed DSTI is calculated using:

```text
Existing Monthly Credit Commitments + Stressed Instalment
```

Formula:

```text
Stressed DSTI (%) =
((Existing Monthly Credit Commitments + Stressed Instalment)
/
Monthly Net Income) × 100
```

Example:

```text
Existing commitments: €300
Stressed instalment: €780
Monthly net income: €2,500

Stressed DSTI = (300 + 780) / 2,500 × 100
Stressed DSTI = 43.2%
```

---

## Remaining Repayment Capacity

The calculator may estimate an indicative maximum monthly debt service amount:

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

Maximum monthly debt service = 2,500 × 40%
Maximum monthly debt service = €1,000

Remaining repayment capacity = 1,000 - 300
Remaining repayment capacity = €700
```

This is only a simulation result and must not be interpreted as approved borrowing capacity.

---

## Margin Against Stressed Scenario

The calculator may compare remaining repayment capacity with the stressed instalment.

Formula:

```text
Margin Against Stressed Scenario =
Remaining Repayment Capacity - Stressed Instalment
```

Example:

```text
Remaining repayment capacity: €700
Stressed instalment: €780

Margin = 700 - 780
Margin = -€80
```

A negative margin may indicate that the stressed instalment exceeds the configured simulation threshold.

This is a risk awareness indicator, not a credit decision.

---

## Loan Amount

The loan amount represents the simulated amount financed.

Example:

```text
Loan amount: €180,000
```

This value may be used for:

- LTV calculation;
- scenario comparison;
- affordability simulation;
- explanatory outputs.

The loan amount must be positive and realistic within the fictional scenario.

---

## Property Value Assumption

The project may use a property value assumption for LTV simulation.

Possible approaches include:

- acquisition value;
- valuation value;
- lower of acquisition and valuation value;
- manually configured property value.

Example:

```text
Acquisition value: €220,000
Valuation value: €215,000
Property value used for simulation: €215,000
```

The method used should be clearly explained.

---

## Loan-to-Value Assumption

LTV stands for **Loan-to-Value**.

Formula:

```text
LTV (%) = Loan Amount / Property Value × 100
```

Example:

```text
Loan amount: €180,000
Property value used: €215,000

LTV = 180,000 / 215,000 × 100
LTV = 83.7%
```

Any LTV threshold used in this project is a configurable simulation assumption only.

It must not be presented as an official banking rule or guarantee of eligibility.

---

## Maturity Assumption

Loan maturity represents the simulated repayment period.

Example:

```text
Loan maturity: 30 years
```

The project may use maturity to:

- compare scenarios;
- estimate age at the end of the loan;
- identify inconsistent maturity assumptions;
- support risk awareness.

Maturity assumptions should be realistic and clearly explained.

---

## Age at End of Loan

The calculator may estimate the age at the end of the simulated loan.

Formula:

```text
Age at End of Loan =
Current Age + Loan Maturity in Years
```

Example:

```text
Current age: 35
Loan maturity: 30 years

Age at end of loan = 35 + 30
Age at end of loan = 65
```

This check is educational and must not be interpreted as a formal eligibility rule.

---

## Interest Rate Stress Assumption

The project may include simplified stress scenarios based on higher instalment assumptions.

Instead of modelling a full loan pricing engine, the tool may allow a manually entered stressed instalment.

This keeps the simulation:

- transparent;
- simple;
- explainable;
- portfolio-friendly;
- focused on affordability awareness.

Future versions may include a simplified instalment formula using:

- loan amount;
- annual interest rate;
- maturity;
- monthly payment calculation.

---

## Risk Warning Assumptions

The tool may generate educational warnings based on configured conditions.

Examples:

```text
High DSTI detected
Stressed DSTI exceeds configured threshold
Negative margin against stressed scenario
Unrealistic income value
Invalid percentage
Missing input
Maturity assumption may be inconsistent
```

These warnings are not formal decisions.

They exist to improve financial literacy and risk awareness.

---

## Input Validation Assumptions

The tool should validate financial inputs before calculation.

Validation checks may include:

- missing values;
- negative values;
- zero income;
- invalid percentages;
- unrealistic income levels;
- unrealistic expense levels;
- proposed instalment greater than income;
- stressed instalment lower than base instalment;
- inconsistent maturity;
- extreme DSTI values;
- missing scenario assumptions.

Input validation is a key part of the project’s Financial Data Quality focus.

---

## Example Fictional Scenario

Example only:

```text
Monthly net income: €2,500
Existing monthly commitments: €300
Proposed instalment: €650
Stressed instalment: €780
Configured DSTI threshold: 40%
Loan amount: €180,000
Property value used: €215,000
Loan maturity: 30 years
Current age: 35
```

Possible simulated outputs:

```text
Base DSTI: 38.0%
Stressed DSTI: 43.2%
Remaining repayment capacity: €700
Margin against stressed scenario: -€80
LTV: 83.7%
Age at end of loan: 65
```

These outputs are illustrative only.

They must not be interpreted as approval, rejection, advice or confirmed affordability.

---

## Limitations of Assumptions

The assumptions in this project are simplified.

They do not account for all factors that may be relevant in real credit analysis, such as:

- full income verification;
- variable income treatment;
- household composition;
- employment stability;
- credit history;
- savings capacity;
- essential living expenses;
- property valuation process;
- collateral quality;
- legal documentation;
- regulatory requirements;
- bank-specific credit policy;
- macroeconomic environment.

---

## Summary

The assumptions used in the **DSTI Affordability Calculator** are designed to be transparent, educational and prudent.

They support financial literacy, data validation, explainability and risk awareness.

They must not be interpreted as formal banking rules, financial advice or a lending decision process.
