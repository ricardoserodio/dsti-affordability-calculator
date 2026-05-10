# Interest Rate Stress Explained

## Purpose of This Document

This document explains the interest rate stress testing logic used in the **DSTI Affordability Calculator**.

The purpose is to show how a simulated monthly instalment may change when the annual interest rate assumption increases.

This supports:

```text
Financial literacy
Affordability awareness
DSTI analysis
Risk awareness
Scenario comparison
Explainability
```

The calculation is educational and demonstrative only.

It must not be interpreted as a bank quote, loan offer, credit approval, financial advice or formal lending assessment.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool.

It is designed to help users understand how income, debt commitments, instalments, loan amount, interest rate assumptions and maturity may affect affordability.

The project does not:

```text
approve credit
reject credit
provide financial advice
replace formal banking analysis
represent internal bank policy
process real client data
request personal documents
```

All values should be fictional, simulated or anonymised.

---

## What Is an Interest Rate Stress Test?

An interest rate stress test compares two scenarios:

```text
Base interest rate scenario
Stressed interest rate scenario
```

The base scenario uses a normal or initial interest rate assumption.

The stressed scenario uses a higher interest rate assumption to show how the estimated monthly instalment may change.

Example:

```text
Base annual interest rate: 4.0%
Stressed annual interest rate: 5.5%
```

This helps users understand how affordability may become more pressured if financing conditions become less favourable.

---

## Main Inputs

The interest rate stress module uses the following inputs:

```text
Loan amount
Loan maturity in years
Base annual interest rate assumption
Stressed annual interest rate assumption
```

Example:

```text
Loan amount: €180,000
Loan maturity: 30 years
Base annual interest rate: 4.0%
Stressed annual interest rate: 5.5%
```

---

## Base Monthly Payment

The base monthly payment is calculated using the simplified amortising loan formula.

```text
Monthly Payment =
P × r × (1 + r)^n / ((1 + r)^n - 1)
```

Where:

```text
P = loan amount
r = monthly interest rate
n = number of monthly payments
```

For the base scenario:

```text
P = €180,000
Annual interest rate = 4.0%
Maturity = 30 years
Number of payments = 360
```

Estimated result:

```text
Base monthly payment ≈ €859.35
```

This is an educational estimate only.

---

## Stressed Monthly Payment

The stressed monthly payment uses the same loan amount and maturity, but applies the stressed annual interest rate assumption.

Example:

```text
Loan amount: €180,000
Annual interest rate: 5.5%
Maturity: 30 years
```

Estimated result:

```text
Stressed monthly payment ≈ €1,022.02
```

This shows how the same loan amount and maturity may produce a higher estimated monthly instalment when the interest rate assumption increases.

---

## Monthly Payment Increase

The monthly payment increase is calculated as:

```text
Monthly Payment Increase =
Stressed Monthly Payment - Base Monthly Payment
```

Example:

```text
Base monthly payment: €859.35
Stressed monthly payment: €1,022.02

Monthly payment increase =
1,022.02 - 859.35

Monthly payment increase = €162.67
```

This indicates the additional monthly pressure created by the stressed interest rate assumption.

---

## Monthly Payment Increase Percentage

The monthly payment increase percentage is calculated as:

```text
Monthly Payment Increase Percentage =
Monthly Payment Increase / Base Monthly Payment × 100
```

Example:

```text
Monthly payment increase: €162.67
Base monthly payment: €859.35

Increase percentage =
162.67 / 859.35 × 100

Increase percentage ≈ 18.93%
```

This helps users understand the proportional impact of the stressed scenario.

---

## Total Repayment Impact

The interest rate stress module may also compare total repayment.

```text
Total Repayment =
Monthly Payment × Number of Payments
```

Example base scenario:

```text
Base monthly payment: €859.35
Number of payments: 360

Base total repayment ≈ €309,366.44
```

Example stressed scenario:

```text
Stressed monthly payment: €1,022.02
Number of payments: 360

Stressed total repayment ≈ €367,928.06
```

Difference:

```text
Total repayment increase =
367,928.06 - 309,366.44

Total repayment increase ≈ €58,561.62
```

This shows how a higher interest rate assumption may increase the estimated total amount repaid over time.

---

## Relationship With DSTI

The stressed monthly payment can be used in the stressed DSTI calculation.

Base DSTI example:

```text
Monthly net income: €2,500
Existing commitments: €300
Base monthly payment: €859.35

Base DSTI =
(300 + 859.35) / 2,500 × 100

Base DSTI ≈ 46.37%
```

Stressed DSTI example:

```text
Monthly net income: €2,500
Existing commitments: €300
Stressed monthly payment: €1,022.02

Stressed DSTI =
(300 + 1,022.02) / 2,500 × 100

Stressed DSTI ≈ 52.88%
```

This demonstrates how interest rate assumptions may affect affordability indicators.

---

## Why This Matters

Interest rate stress testing helps demonstrate that affordability is sensitive to changes in financing assumptions.

A scenario that appears manageable under one interest rate assumption may become more pressured under a higher rate assumption.

This is useful for:

```text
Financial education
Scenario analysis
Affordability awareness
Risk communication
Data validation
Human-in-the-loop review
```

---

## Data Quality Checks

The module should support data quality awareness.

Potential issues include:

```text
Missing loan amount
Zero or negative loan amount
Negative interest rate
Zero or negative maturity
Stressed interest rate lower than base interest rate
Extremely high interest rate assumptions
Unrealistic maturity assumptions
Incoherent repayment assumptions
```

Some issues may block calculation.

Other issues may produce warnings for human review.

---

## Risk Awareness Interpretation

The project should avoid decisive credit language.

Preferred wording:

```text
The stressed interest rate assumption increases the estimated monthly payment.
This may create additional affordability pressure under the configured simulation assumptions.
```

Avoid wording:

```text
The credit is rejected.
The client cannot afford the loan.
The bank would not approve this case.
The user is not eligible.
```

The output should remain educational, cautious and explainable.

---

## Human-in-the-Loop Principle

Interest rate stress results should be interpreted by a human.

The project should not automatically make decisions based on stress test outputs.

A human reviewer should consider:

```text
Quality of assumptions
Completeness of inputs
Reasonableness of income values
Existing commitments
DSTI under base and stressed assumptions
LTV context
Maturity context
Limitations of the model
```

The role of the tool is to support understanding, not to replace judgement.

---

## Privacy and Data Protection

The project must not request or process real personal documents.

Users should not input:

```text
Real bank statements
Real payslips
Real tax returns
Real credit responsibility maps
Real client identifiers
Real loan contracts
Confidential banking information
```

All examples should use fictional, simulated or anonymised values.

---

## Limitations

The interest rate stress calculation is simplified.

It does not include:

```text
Insurance costs
Bank fees
Taxes
Promotional pricing
Variable rate reset rules
Fixed-rate periods
Mixed-rate structures
Grace periods
Residual values
APR/APRC calculations
Regulatory affordability rules
Bank-specific pricing policies
Contractual conditions
```

The results are indicative and educational only.

---

## Responsible Use

The interest rate stress test should be used only for:

```text
Educational simulation
Financial literacy
DSTI awareness
Risk awareness
Scenario comparison
Portfolio demonstration
```

It should not be used as:

```text
Financial advice
Credit advice
Loan recommendation
Approval indication
Eligibility assessment
Formal bank affordability assessment
```

---

## Summary

The interest rate stress module shows how a higher interest rate assumption may affect:

```text
Estimated monthly payment
Monthly affordability pressure
Stressed DSTI
Total repayment
Risk awareness interpretation
```

This strengthens the **DSTI Affordability Calculator** by making the simulation more realistic, explainable and useful for financial literacy.

The result remains educational only and must never be interpreted as a credit decision, bank quote or financial advice.
