# Interest Rate Builder Explained

## Purpose of This Document

This document explains the simulated interest rate builder used in the **DSTI Affordability Calculator**.

The purpose is to make the interest rate assumptions more realistic and explainable by separating:

```text
Simulated EURIBOR
Simulated spread
Stress buffer
```

Instead of using a single annual interest rate assumption, the project can now show how a simulated base rate and stressed rate are built.

This is educational and demonstrative only.

It must not be interpreted as a bank quote, loan offer, pricing model, credit approval, financial advice or formal lending assessment.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

```text
Financial literacy
DSTI analysis
Affordability simulation
Interest rate sensitivity
Data validation
Explainability
Risk awareness
Human-in-the-loop interpretation
```

The interest rate builder strengthens the project because it reflects a more realistic lending concept:

```text
Index rate + spread = annual interest rate assumption
```

For Portuguese mortgage-style simulations, the index rate can be represented by a simulated EURIBOR assumption.

---

## Core Formula

The base annual interest rate is calculated as:

```text
Base Annual Interest Rate =
Simulated EURIBOR + Simulated Spread
```

The stressed annual interest rate is calculated as:

```text
Stressed Annual Interest Rate =
Base Annual Interest Rate + Stress Buffer
```

Full version:

```text
Stressed Annual Interest Rate =
Simulated EURIBOR + Simulated Spread + Stress Buffer
```

---

## Main Inputs

The interest rate builder uses three main inputs:

```text
Simulated EURIBOR
Simulated spread
Stress buffer
```

Example:

```text
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
```

---

## Simulated EURIBOR

The simulated EURIBOR represents an index rate assumption.

Example:

```text
Simulated EURIBOR: 3.00%
```

In this project, the EURIBOR value should be treated as:

```text
manual
fictional
simulated
educational
not live market data
not a bank quote
```

The initial version does not automatically fetch live EURIBOR values.

This is intentional, because the project should remain robust, transparent and portfolio-safe.

---

## Simulated Spread

The simulated spread represents an additional margin assumption.

Example:

```text
Simulated spread: 0.90%
```

In this project, the spread is:

```text
manually entered
fictional or simulated
not bank-specific
not a pricing offer
not a credit decision
```

A negative spread is not allowed in the current logic because it may create confusing or unrealistic simulation outputs.

---

## Base Annual Interest Rate

The base annual interest rate is calculated as:

```text
Base Annual Interest Rate =
Simulated EURIBOR + Simulated Spread
```

Example:

```text
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%

Base Annual Interest Rate =
3.00% + 0.90%

Base Annual Interest Rate = 3.90%
```

This base rate can then be used to estimate a base monthly instalment.

---

## Stress Buffer

The stress buffer represents an additional interest rate increase used for risk awareness.

Example:

```text
Stress buffer: 1.50%
```

The stress buffer helps demonstrate how affordability may change under less favourable interest rate assumptions.

It is not a regulatory rule, bank policy rule or formal stress test.

It is a configurable educational assumption.

---

## Stressed Annual Interest Rate

The stressed annual interest rate is calculated as:

```text
Stressed Annual Interest Rate =
Base Annual Interest Rate + Stress Buffer
```

Example:

```text
Base annual interest rate: 3.90%
Stress buffer: 1.50%

Stressed Annual Interest Rate =
3.90% + 1.50%

Stressed Annual Interest Rate = 5.40%
```

This stressed rate can then be used to estimate a stressed monthly instalment.

---

## Full Example

Assume the following fictional values:

```text
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
Loan amount: €180,000
Loan maturity: 30 years
```

The base annual interest rate is:

```text
3.00% + 0.90% = 3.90%
```

The stressed annual interest rate is:

```text
3.90% + 1.50% = 5.40%
```

These rates can then be used in the loan payment calculation module.

The base monthly payment is calculated using the base annual interest rate.

The stressed monthly payment is calculated using the stressed annual interest rate.

The difference between the two helps demonstrate interest rate sensitivity.

---

## Relationship With Loan Payment Calculation

The interest rate builder does not calculate the monthly instalment by itself.

It prepares the interest rate assumptions that can be used by the loan payment calculator.

Workflow:

```text
1. User enters simulated EURIBOR.
2. User enters simulated spread.
3. User enters stress buffer.
4. App calculates base annual interest rate.
5. App calculates stressed annual interest rate.
6. Loan payment calculator estimates base monthly payment.
7. Loan payment calculator estimates stressed monthly payment.
8. DSTI calculator uses those instalments for affordability simulation.
```

---

## Relationship With DSTI

The estimated monthly payment affects DSTI directly.

Example:

```text
Monthly net income: €2,500
Existing commitments: €300
Base monthly payment: €850
Stressed monthly payment: €1,000
```

Base DSTI:

```text
Base DSTI =
(300 + 850) / 2,500 × 100

Base DSTI = 46.00%
```

Stressed DSTI:

```text
Stressed DSTI =
(300 + 1,000) / 2,500 × 100

Stressed DSTI = 52.00%
```

This shows how interest rate assumptions can materially affect affordability indicators.

---

## Data Quality Checks

The interest rate builder supports data quality awareness.

Examples of checks:

```text
Missing EURIBOR assumption
Missing spread assumption
Missing stress buffer assumption
Negative spread
Negative stress buffer
Very high base annual interest rate
Very high stressed annual interest rate
Negative EURIBOR requiring human review
Stress buffer equal to zero
```

Some checks may block calculation.

Other checks may create non-blocking warnings or explanatory notes.

---

## Negative EURIBOR

The module allows a negative simulated EURIBOR.

This is intentional because negative EURIBOR environments have existed historically.

However, negative EURIBOR should generate a data quality note.

Example:

```text
Simulated EURIBOR: -0.50%
Simulated spread: 1.00%

Base annual interest rate = 0.50%
```

A human reviewer should check whether this assumption is intentional and reasonable.

---

## Why Automatic EURIBOR Is Not Mandatory at This Stage

The project may later include optional automatic EURIBOR retrieval from a suitable public source.

However, the first version should support manual EURIBOR input because it is:

```text
more transparent
more robust
easier to test
safer for portfolio use
less dependent on external APIs
better for educational explanations
```

A future version may include:

```text
automatic public reference rate retrieval
source name
last updated date
fallback to manual input
clear disclaimer
```

The app should always remain usable even if automatic data retrieval fails.

---

## Responsible Wording

Preferred wording:

```text
Simulated EURIBOR assumption
Simulated spread assumption
Configured stress buffer
Base annual interest rate assumption
Stressed annual interest rate assumption
Educational simulation output
```

Avoid wording:

```text
Real bank rate
Approved interest rate
Guaranteed rate
Client pricing
Bank offer
Eligibility rate
Credit decision rate
```

---

## Human-in-the-Loop Principle

The interest rate assumptions should be reviewed by a human.

A human reviewer should consider:

```text
Whether the EURIBOR assumption is reasonable
Whether the spread assumption is realistic for the educational scenario
Whether the stress buffer is coherent
Whether the resulting base rate is unusually high or low
Whether the stressed rate creates material affordability pressure
Whether the output should be interpreted cautiously
```

The tool supports judgement.

It does not replace judgement.

---

## Privacy and Data Protection

The interest rate builder does not require personal data.

Users should not enter:

```text
Real client identifiers
Real loan contracts
Confidential pricing information
Internal bank rules
Personal financial documents
Real customer information
```

All values should be fictional, simulated or anonymised.

---

## Limitations

The interest rate builder is simplified.

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
Product cross-selling effects
Regulatory affordability rules
Bank-specific credit policy
Contractual terms
```

The outputs are indicative and educational only.

---

## Summary

The interest rate builder improves the **DSTI Affordability Calculator** by separating:

```text
Simulated EURIBOR
Simulated spread
Stress buffer
```

This makes the project more realistic, explainable and relevant to banking-style affordability simulations.

The result remains educational only and must never be interpreted as a bank quote, credit decision, pricing offer or financial advice.
