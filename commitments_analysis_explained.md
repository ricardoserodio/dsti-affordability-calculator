# Commitments Analysis Explained

## Purpose of This Document

This document explains the structured commitments analysis layer used in the **DSTI Affordability Calculator**.

The purpose is to improve:

```text
Financial data quality
Input explainability
DSTI transparency
Risk awareness
Scenario analysis
Human-in-the-loop interpretation
```

Instead of using only one generic value for existing monthly commitments, the project now separates commitments into different fictional categories.

This makes the simulation more realistic and easier to understand.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool.

It is focused on:

```text
DSTI analysis
Affordability simulation
Loan payment estimation
Existing commitments analysis
Interest rate stress testing
LTV awareness
Maturity awareness
Data validation
Explainability
Risk awareness
```

The project is educational, demonstrative and portfolio-oriented.

It is not:

```text
A credit approval system
A credit rejection tool
An underwriting engine
A bank policy model
A financial advisory tool
A replacement for formal human credit analysis
```

---

## Why Existing Commitments Matter

Existing monthly commitments are an important part of DSTI analysis.

DSTI is calculated as:

```text
DSTI =
Existing Monthly Commitments + Monthly Instalment
------------------------------------------------ × 100
              Monthly Net Income
```

This means that higher existing commitments increase the DSTI ratio.

Example:

```text
Monthly net income: €2,500
Existing monthly commitments: €300
Proposed monthly instalment: €650
```

DSTI:

```text
(€300 + €650) / €2,500 × 100 = 38.00%
```

If existing commitments increase to €600:

```text
(€600 + €650) / €2,500 × 100 = 50.00%
```

This shows why separating and validating existing commitments adds value to the simulation.

---

## Commitment Categories

The project separates existing monthly commitments into:

```text
Housing commitment
Auto loan commitment
Personal loan commitment
Credit card commitment
Other credit commitments
```

These categories are educational and generic.

They are not copied from any proprietary banking tool or internal policy model.

---

## Housing Commitment

The housing commitment represents an existing monthly housing-related credit commitment.

Example:

```text
Existing housing credit commitment: €500
```

This may be useful in a fictional scenario where the user wants to compare:

```text
Current housing payment
Future estimated payment
Overall affordability pressure
```

In the project, this value is manually entered and simulated.

It is not verified against real documentation.

---

## Auto Loan Commitment

The auto loan commitment represents an existing monthly car loan or vehicle finance commitment.

Example:

```text
Auto loan commitment: €150
```

This value contributes to total existing commitments and therefore affects DSTI.

---

## Personal Loan Commitment

The personal loan commitment represents existing monthly personal loan payments.

Example:

```text
Personal loan commitment: €100
```

This category helps make the input structure more realistic and transparent.

---

## Credit Card Commitment

The credit card commitment represents a simplified monthly credit card-related commitment.

Example:

```text
Credit card commitment: €50
```

The project does not model:

```text
Credit card limits
Minimum payments
Utilisation
Interest charges
Revolving balances
Behavioural risk
```

It only uses a manually entered educational monthly commitment amount.

---

## Other Credit Commitments

Other credit commitments represent any other existing monthly credit obligations in a fictional scenario.

Example:

```text
Other credit commitments: €25
```

This category allows the simulation to remain flexible without becoming overly complex.

---

## Total Existing Commitments

The module calculates:

```text
Total Existing Commitments =
Housing Commitment
+ Auto Loan Commitment
+ Personal Loan Commitment
+ Credit Card Commitment
+ Other Credit Commitments
```

Example:

```text
Housing commitment: €0
Auto loan commitment: €150
Personal loan commitment: €100
Credit card commitment: €50
Other credit commitments: €25
```

Total:

```text
€0 + €150 + €100 + €50 + €25 = €325
```

This total is then used in the DSTI calculation.

---

## Highest Commitment Category

The module also identifies the category with the highest monthly value.

Example:

```text
Housing commitment: €0
Auto loan commitment: €150
Personal loan commitment: €100
Credit card commitment: €50
Other credit commitments: €25
```

Highest category:

```text
Auto loan commitment
```

This helps explain which type of commitment contributes most to the total.

It is an educational explainability feature, not a risk decision.

---

## Interpretation Logic

The commitments module generates a simple educational interpretation.

Examples:

### No Existing Commitments

```text
No existing monthly credit commitments were entered.
```

This may be valid in a fictional scenario, but the assumption should be reviewed before interpretation.

### High Existing Commitments

```text
Risk awareness warning: total existing monthly commitments appear high.
```

This warns that existing commitments may place pressure on DSTI and repayment capacity.

### Standard Case

```text
Existing monthly commitments were grouped by category to improve financial data quality and explainability.
```

This confirms the commitments were structured and used in the DSTI calculation.

---

## Data Quality Checks

The commitments module validates that:

```text
Commitment values are not missing
Commitment values are not negative
Commitment values are numeric
Total commitments are calculated consistently
The highest category is identified
```

Invalid examples:

```text
Housing commitment: missing
Auto loan commitment: -150
Personal loan commitment: -100
```

These should trigger validation errors.

---

## Relationship With DSTI

The output from the commitments module is passed into the DSTI calculation.

Workflow:

```text
1. User enters existing commitments by category.
2. Commitments module validates each value.
3. Commitments module calculates total existing commitments.
4. DSTI calculator uses total existing commitments.
5. Scenario engine calculates base and stressed DSTI.
6. App displays breakdown and interpretation.
```

This makes the DSTI output more explainable.

---

## Relationship With Financial Data Quality

Separating commitments by category improves financial data quality because it avoids hiding all commitments inside a single generic input.

Instead of:

```text
Existing commitments: €325
```

The project shows:

```text
Housing commitment: €0
Auto loan commitment: €150
Personal loan commitment: €100
Credit card commitment: €50
Other credit commitments: €25
Total existing commitments: €325
```

This improves:

```text
Traceability
Input validation
Explainability
Scenario review
Auditability
Portfolio value
```

---

## Responsible Use

The commitments analysis should only be used for:

```text
Educational simulation
Portfolio demonstration
Financial literacy
Scenario analysis
Data validation practice
Risk awareness
```

It should not be used for:

```text
Real client analysis
Credit approval
Credit rejection
Eligibility assessment
Bank policy decisions
Financial advice
Regulatory decision-making
```

---

## Privacy and Data Protection

Users should not enter:

```text
Real client names
Real account numbers
Real credit contracts
Real credit responsibility maps
Real personal documents
Confidential bank information
Internal policy rules
```

All values should be fictional, simulated or anonymised.

---

## Human-in-the-Loop Principle

A human reviewer should consider:

```text
Whether commitments are coherent
Whether any category appears unusually high
Whether the total is realistic for the fictional scenario
Whether warnings require review
Whether the DSTI impact is clearly understood
```

The module supports judgement.

It does not replace judgement.

---

## Portfolio Value

This module strengthens the project by demonstrating:

```text
Structured financial input analysis
Financial data quality controls
DSTI input traceability
Banking-inspired affordability logic
Explainability
Risk awareness
Python modular design
Unit testing
Responsible simulation design
```

Suggested CV wording:

```text
Enhanced a Python/Streamlit DSTI affordability calculator with a structured commitments analysis layer, separating housing, auto loan, personal loan, credit card and other monthly commitments to improve financial data quality, explainability and affordability risk awareness.
```

---

## Summary

The commitments analysis layer improves the **DSTI Affordability Calculator** by replacing a single generic commitments input with a structured breakdown.

This makes the simulation more realistic, explainable and useful as a professional portfolio project.

The output remains educational only and must never be interpreted as a credit decision, financial advice or bank policy result.
