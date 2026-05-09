# Scenario Analysis

## Purpose of Scenario Analysis

Scenario analysis is a central part of the **DSTI Affordability Calculator**.

The purpose is to show how changes in income, credit commitments, instalments, maturity, property value and stress assumptions may affect affordability.

This document explains the main scenario types used in the project.

All scenarios are fictional, simulated or anonymised. They must not be interpreted as credit approval, credit rejection, financial advice or formal banking analysis.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

- financial literacy;
- DSTI calculation;
- affordability awareness;
- financial data validation;
- explainability;
- risk awareness;
- prudent scenario comparison.

The tool does not approve or reject credit.

It helps users understand how different assumptions can change the financial effort shown by the simulation.

---

## Why Scenario Analysis Matters

A single affordability calculation can be misleading if assumptions are too optimistic.

Scenario analysis helps demonstrate how affordability may change when:

- income decreases;
- existing credit commitments increase;
- the proposed instalment increases;
- the stressed instalment becomes higher;
- maturity assumptions change;
- property value assumptions change;
- LTV increases;
- data quality issues appear.

The objective is to support responsible financial simulation and risk awareness.

---

## Base Scenario

The base scenario represents the initial simulation using the standard fictional assumptions entered by the user.

Example:

```text
Monthly net income: €2,500
Existing monthly commitments: €300
Proposed monthly instalment: €650
Stressed monthly instalment: €780
Configured DSTI threshold: 40%
Loan amount: €180,000
Property value used: €215,000
Loan maturity: 30 years
Current age: 35
```

Possible outputs:

```text
Base DSTI: 38.0%
Stressed DSTI: 43.2%
Remaining repayment capacity: €700
Margin against stressed instalment: -€80
LTV: 83.7%
Age at end of loan: 65
```

This scenario is only indicative and educational.

---

## Prudent Income Scenario

The prudent income scenario applies a conservative income factor.

Example:

```text
Original monthly net income: €2,500
Conservative factor: 90%
Conservative monthly income: €2,250
```

This allows the user to understand how affordability changes when income is reduced.

The purpose is not to predict income changes, but to demonstrate sensitivity to income assumptions.

---

## Higher Commitment Scenario

The higher commitment scenario increases existing monthly credit commitments.

Example:

```text
Base existing commitments: €300
Higher existing commitments: €600
```

This shows how existing debt obligations affect DSTI and remaining repayment capacity.

Higher existing commitments generally increase financial pressure in the simulation.

---

## Higher Stress Scenario

The higher stress scenario increases the stressed monthly instalment.

Example:

```text
Base stressed instalment: €780
Higher stressed instalment: €900
```

This helps illustrate the effect of less favourable repayment conditions or higher interest rate assumptions.

The higher stress scenario is useful for risk awareness.

---

## Lower Income Scenario

The lower income scenario reduces monthly net income.

Example:

```text
Base monthly net income: €2,500
Lower monthly net income: €2,000
```

This shows how affordability may become more pressured if income decreases.

It is an educational sensitivity scenario only.

---

## Higher LTV Scenario

The higher LTV scenario increases the simulated loan amount or reduces the property value assumption.

Example:

```text
Loan amount: €210,000
Property value used: €215,000
Simulated LTV: 97.7%
```

This helps demonstrate how the relationship between loan amount and property value affects the simulation.

Any LTV threshold used is a configurable simulation assumption only.

---

## Longer Maturity Scenario

The longer maturity scenario increases the simulated loan maturity.

Example:

```text
Base maturity: 30 years
Longer maturity: 40 years
```

This affects the maturity and age-at-end-of-loan analysis.

The scenario helps demonstrate how maturity assumptions can affect risk awareness.

---

## Older Borrower Scenario

The older borrower scenario increases the fictional or anonymised current age used in the simulation.

Example:

```text
Current age: 55
Loan maturity: 30 years
Age at end of loan: 85
```

This may trigger a maturity risk awareness warning.

This should never be presented as an eligibility decision.

---

## High DSTI Scenario

The high DSTI scenario uses assumptions that intentionally create higher financial effort.

Example:

```text
Monthly net income: €2,500
Existing commitments: €500
Proposed instalment: €900
Stressed instalment: €1,100
Configured DSTI threshold: 40%
```

Possible outputs:

```text
Base DSTI: 56.0%
Stressed DSTI: 64.0%
```

This scenario is useful to demonstrate validation warnings and explainability.

It does not represent automatic rejection.

---

## Data Quality Review Scenario

The data quality review scenario intentionally includes an assumption that should be reviewed.

Example:

```text
Proposed instalment: €650
Stressed instalment: €600
```

Since the stressed instalment is lower than the proposed instalment, the validation layer may flag this as inconsistent.

This demonstrates how data validation helps identify unusual assumptions before interpreting results.

---

## Suggested Scenario Comparison Table

The project may display a comparison table with fields such as:

```text
scenario_name
validation_status
warning_count
base_dsti_percentage
stressed_dsti_percentage
remaining_repayment_capacity
margin_against_stressed_instalment
ltv_percentage
age_at_end_of_loan
```

This allows users to compare results across different simulated assumptions.

---

## Example Comparison

Example only:

```text
Base simulation:
Base DSTI = 38.0%
Stressed DSTI = 43.2%
Margin against stressed instalment = -€80

Prudent income simulation:
Base DSTI = 42.2%
Stressed DSTI = 48.0%
Margin against stressed instalment = -€180
```

This shows that reducing income increases DSTI and reduces affordability margin.

---

## Scenario Interpretation Principles

Scenario interpretation should be:

- educational;
- neutral;
- transparent;
- non-advisory;
- non-decisive;
- focused on risk awareness.

Avoid language such as:

```text
Approved
Rejected
Eligible
Not eligible
Credit accepted
Credit refused
Safe to borrow
Recommended loan
```

Preferred language:

```text
Scenario requires review
Risk awareness warning
Configured simulation threshold exceeded
Input assumption appears unusual
Affordability pressure increases in this scenario
Result is indicative and educational only
```

---

## Risk Awareness Examples

The tool may display risk awareness warnings such as:

```text
The stressed DSTI exceeds the configured simulation threshold.
The margin against stressed instalment is negative.
Existing commitments appear high relative to income.
The simulated LTV exceeds the configured threshold.
The simulated age at the end of the loan appears high.
The stressed instalment is lower than the proposed instalment.
```

These warnings are not credit decisions.

They are educational flags designed to support financial literacy and prudent interpretation.

---

## Human-in-the-Loop Approach

Scenario analysis should support human understanding, not replace human judgement.

The tool may calculate indicators and display warnings, but interpretation should remain cautious and contextual.

In real banking processes, formal analysis may require:

- verified income;
- verified credit commitments;
- credit history;
- property valuation;
- documentation review;
- regulatory checks;
- internal policy assessment;
- professional judgement.

This project does not perform those steps.

---

## Privacy and Data Protection

All scenarios must use fictional, simulated or anonymised values.

The project must not request or process:

- real payslips;
- real tax returns;
- real credit responsibility maps;
- real bank statements;
- real personal identifiers;
- real client documents.

Any reference to supporting documents is educational only.

---

## Limitations

Scenario analysis in this project is simplified.

It does not include all factors that may affect real affordability, such as:

- full household expenses;
- variable income treatment;
- employment stability;
- savings capacity;
- credit history;
- legal documentation;
- full property valuation;
- regulatory requirements;
- bank-specific credit policies;
- macroeconomic conditions.

The results should always be interpreted as educational simulation outputs.

---

## Summary

Scenario analysis helps demonstrate how small changes in assumptions can materially affect financial affordability.

The **DSTI Affordability Calculator** uses scenario analysis to promote financial literacy, explainability, data validation and risk awareness.

It must never be interpreted as a lending decision engine or financial advice tool.
