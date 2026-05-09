# Loan Payment Formula Explained

## Purpose of This Document

This document explains the simplified loan payment formula used in the **DSTI Affordability Calculator**.

The purpose is to show how an estimated monthly instalment can be calculated using:

```text
Loan amount
Annual interest rate assumption
Loan maturity
```

This calculation is educational and demonstrative only.

It must not be interpreted as a bank quote, loan offer, credit approval, financial advice or formal lending assessment.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

```text
Financial literacy
DSTI analysis
Affordability simulation
Data validation
Explainability
Risk awareness
Responsible financial simulations
```

The loan payment formula is included to help users understand how interest rate and maturity assumptions may affect monthly instalments.

---

## Monthly Payment Formula

The project may use a simplified amortising loan formula:

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

---

## Monthly Interest Rate

The monthly interest rate is calculated from the annual interest rate assumption:

```text
Monthly Interest Rate =
Annual Interest Rate / 12
```

If the annual interest rate is expressed as a percentage:

```text
Monthly Interest Rate =
Annual Interest Rate (%) / 100 / 12
```

Example:

```text
Annual interest rate: 4.0%

Monthly interest rate =
4.0 / 100 / 12
Monthly interest rate = 0.003333...
```

---

## Number of Payments

The number of payments is calculated from the maturity in years:

```text
Number of Payments =
Loan Maturity in Years × 12
```

Example:

```text
Loan maturity: 30 years

Number of payments =
30 × 12
Number of payments = 360
```

---

## Example Calculation

Assume the following fictional values:

```text
Loan amount: €180,000
Annual interest rate assumption: 4.0%
Loan maturity: 30 years
```

Then:

```text
P = 180,000
r = 4.0 / 100 / 12
r = 0.003333...
n = 30 × 12
n = 360
```

Using the simplified amortising loan formula, the estimated monthly payment is approximately:

```text
Estimated monthly payment: €859.35
```

This value is an educational estimate only.

It is not a bank quote, offer, approval indication or financial advice.

---

## Zero Interest Rate Case

If the annual interest rate assumption is 0%, the formula is simplified:

```text
Monthly Payment =
Loan Amount / Number of Payments
```

Example:

```text
Loan amount: €120,000
Annual interest rate: 0%
Loan maturity: 30 years
Number of payments: 360

Monthly payment =
120,000 / 360
Monthly payment = €333.33
```

---

## Total Repayment

The estimated total repayment can be calculated as:

```text
Total Repayment =
Monthly Payment × Number of Payments
```

Example:

```text
Monthly payment: €859.35
Number of payments: 360

Total repayment =
859.35 × 360
Total repayment ≈ €309,366
```

This is a simplified estimate.

---

## Total Interest

The estimated total interest can be calculated as:

```text
Total Interest =
Total Repayment - Loan Amount
```

Example:

```text
Total repayment: €309,366
Loan amount: €180,000

Total interest =
309,366 - 180,000
Total interest ≈ €129,366
```

This helps users understand how interest rate and maturity assumptions affect the total estimated cost over time.

---

## Why This Formula Matters

The formula helps demonstrate that monthly instalments are affected by:

```text
Loan amount
Interest rate
Loan maturity
```

A higher loan amount generally increases the monthly payment.

A higher interest rate generally increases the monthly payment and total repayment.

A longer maturity may reduce the monthly payment but can increase the estimated total interest paid over time.

A shorter maturity may increase the monthly payment but can reduce the estimated total interest paid over time.

---

## Relationship With DSTI

The estimated monthly payment can be used as the proposed instalment in the DSTI calculation.

Example:

```text
Estimated monthly payment: €859.35
Existing monthly commitments: €300
Monthly net income: €2,500
```

DSTI:

```text
DSTI =
(300 + 859.35) / 2,500 × 100

DSTI ≈ 46.37%
```

This shows how the estimated instalment affects the simulated financial effort.

---

## Stressed Interest Rate Scenario

The project may also estimate a stressed monthly payment using a higher interest rate assumption.

Example:

```text
Base annual interest rate: 4.0%
Stressed annual interest rate: 5.5%
```

The stressed monthly payment can then be used in the stressed DSTI calculation.

This helps users understand how affordability may change if interest rate assumptions become less favourable.

---

## Important Limitations

This formula is simplified.

It does not include all factors that may affect real loan instalments, such as:

```text
Insurance costs
Fees
Taxes
Indexation rules
Variable rate reset periods
Grace periods
Residual values
Mixed rate structures
Bank-specific pricing
Legal or contractual conditions
Promotional campaigns
Regulatory requirements
```

The calculation should therefore be interpreted only as an educational estimate.

---

## Responsible Use

The calculated monthly payment should be used only for:

```text
Educational simulation
Financial literacy
Affordability awareness
DSTI demonstration
Scenario comparison
Portfolio demonstration
```

It should not be used as:

```text
Financial advice
Credit advice
Loan recommendation
Bank quote
Eligibility assessment
Approval indication
Formal affordability assessment
```

---

## Privacy and Data Protection

All values used in this formula should be fictional, simulated or anonymised.

The project must not request or process:

```text
Real personal income documents
Real bank statements
Real credit responsibility maps
Real client identifiers
Real loan contracts
Confidential banking information
```

---

## Summary

The loan payment formula helps explain how loan amount, interest rate and maturity can influence estimated monthly instalments.

In the **DSTI Affordability Calculator**, this formula supports financial literacy, explainability and risk awareness.

The result is educational only and must never be interpreted as a bank quote, credit decision or financial advice.
