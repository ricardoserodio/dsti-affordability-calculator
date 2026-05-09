# Data Validation Rules

## Purpose of This Document

This document defines the main data validation rules for the **DSTI Affordability Calculator**.

Financial data quality is a central part of this project.

The purpose of these rules is to ensure that inputs used in the simulation are complete, coherent, realistic and suitable for educational affordability analysis.

This project does not use real client data and must only rely on fictional, simulated or anonymised values.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

- financial literacy;
- DSTI calculation;
- affordability awareness;
- data validation;
- explainability;
- risk awareness;
- responsible financial simulations.

The validation rules are designed to improve the quality of simulated inputs before producing outputs.

They must not be interpreted as official banking rules, credit approval criteria or regulatory requirements.

---

## General Validation Principles

The application should validate inputs before performing any calculation.

Validation should identify:

- missing values;
- invalid values;
- negative values;
- zero income;
- unrealistic assumptions;
- incoherent scenarios;
- invalid percentages;
- inconsistent maturity values;
- extreme or unusual DSTI values.

The goal is not to approve or reject a scenario.

The goal is to help users understand whether the simulation inputs are reasonable enough to produce an educational output.

---

## Data Privacy Rule

The application must not request or process real personal data.

Users should only input fictional, simulated or anonymised values.

The application must not request:

- real payslips;
- real salary statements;
- real tax returns;
- real tax assessment statements;
- real credit responsibility maps;
- real personal identifiers;
- real bank statements;
- real client documents;
- confidential banking information.

Any reference to supporting documents is purely educational.

---

## Required Input Fields

The following fields may be required depending on the simulation mode:

```text
monthly_net_income
existing_monthly_commitments
proposed_monthly_instalment
stressed_monthly_instalment
configured_dsti_threshold
loan_amount
property_value
loan_maturity_years
current_age
```

If a required field is missing, the calculator should not produce a final result.

Instead, it should display a clear validation warning.

Example message:

```text
Monthly net income is required to calculate DSTI.
```

---

## Missing Values

Inputs should not be missing when required for calculation.

Invalid examples:

```text
monthly_net_income = null
proposed_monthly_instalment = ""
configured_dsti_threshold = None
```

Suggested warning:

```text
Missing value detected. Please provide a fictional or simulated value before running the calculation.
```

---

## Negative Values

Financial input values should not be negative unless explicitly justified by the simulation design.

The following fields should normally be greater than or equal to zero:

```text
existing_monthly_commitments
proposed_monthly_instalment
stressed_monthly_instalment
loan_amount
property_value
```

The following field should be strictly greater than zero:

```text
monthly_net_income
```

Invalid examples:

```text
monthly_net_income = -2500
proposed_monthly_instalment = -650
loan_amount = -180000
```

Suggested warning:

```text
Negative values are not valid for this simulation input.
```

---

## Zero Income

Monthly net income must be greater than zero.

Invalid example:

```text
monthly_net_income = 0
```

Reason:

```text
DSTI cannot be calculated when monthly net income is zero.
```

Suggested warning:

```text
Monthly net income must be greater than zero to calculate DSTI.
```

---

## Unrealistic Income Levels

The tool may flag income levels that appear unusually low or unusually high for an educational household affordability simulation.

Example configurable warning ranges:

```text
monthly_net_income < 500
monthly_net_income > 50000
```

These thresholds are not rules or eligibility criteria.

They are only data quality alerts.

Suggested warning:

```text
The monthly net income entered appears unusual. Please confirm that this is a fictional or simulated value.
```

---

## Unrealistic Expense or Commitment Levels

Existing credit commitments should be reviewed when they appear unusually high compared with income.

Example configurable checks:

```text
existing_monthly_commitments > monthly_net_income
existing_monthly_commitments > 0.70 × monthly_net_income
```

Suggested warning:

```text
Existing monthly commitments appear high relative to monthly net income.
```

This is a risk awareness warning, not a decision.

---

## Proposed Instalment Validation

The proposed monthly instalment should be greater than or equal to zero.

The tool may flag scenarios where the proposed instalment appears unusually high relative to income.

Example configurable checks:

```text
proposed_monthly_instalment > monthly_net_income
proposed_monthly_instalment > 0.60 × monthly_net_income
```

Suggested warning:

```text
The proposed instalment appears high relative to monthly net income.
```

---

## Stressed Instalment Validation

The stressed monthly instalment should normally be equal to or higher than the proposed monthly instalment.

Valid example:

```text
proposed_monthly_instalment = 650
stressed_monthly_instalment = 780
```

Potentially inconsistent example:

```text
proposed_monthly_instalment = 650
stressed_monthly_instalment = 600
```

Suggested warning:

```text
The stressed instalment is lower than the base proposed instalment. Please confirm the assumption.
```

This does not block the simulation automatically, but it should be clearly flagged.

---

## DSTI Threshold Validation

The configured DSTI threshold should be a percentage between 0 and 100.

Valid example:

```text
configured_dsti_threshold = 40
```

Invalid examples:

```text
configured_dsti_threshold = -10
configured_dsti_threshold = 120
```

Suggested warning:

```text
DSTI threshold must be between 0% and 100%.
```

The threshold is a simulation assumption only and must not be presented as a formal credit policy rule.

---

## Interest Rate Validation

If the project includes interest rate assumptions, rates should be validated as percentages.

Example fields:

```text
base_interest_rate
stressed_interest_rate
```

Suggested configurable checks:

```text
base_interest_rate >= 0
stressed_interest_rate >= 0
base_interest_rate <= 25
stressed_interest_rate <= 35
```

Suggested warning:

```text
The interest rate assumption appears unusual. Please confirm the simulated value.
```

These ranges are educational data quality checks only.

---

## Loan Amount Validation

Loan amount should be greater than zero when used.

Invalid examples:

```text
loan_amount = 0
loan_amount = -180000
```

Suggested warning:

```text
Loan amount must be greater than zero for this simulation.
```

The tool may also flag unusually high loan amounts for manual review.

---

## Property Value Validation

Property value should be greater than zero when used for LTV calculation.

Invalid examples:

```text
property_value = 0
property_value = -215000
```

Suggested warning:

```text
Property value must be greater than zero to calculate LTV.
```

---

## LTV Validation

LTV should be calculated only when both loan amount and property value are valid.

Formula:

```text
LTV (%) = Loan Amount / Property Value × 100
```

The tool may flag unusual LTV values.

Example configurable checks:

```text
LTV < 0
LTV > 100
LTV > 120
```

Suggested warning:

```text
The calculated LTV appears high or unusual for this simulation.
```

This warning is educational and must not be interpreted as a credit decision.

---

## Maturity Validation

Loan maturity should be greater than zero.

Example field:

```text
loan_maturity_years
```

Valid example:

```text
loan_maturity_years = 30
```

Invalid examples:

```text
loan_maturity_years = 0
loan_maturity_years = -5
loan_maturity_years = 80
```

Suggested warning:

```text
Loan maturity appears invalid or unrealistic. Please review the simulated value.
```

---

## Age Validation

Current age should be realistic for an educational affordability simulation.

Example configurable checks:

```text
current_age < 18
current_age > 100
```

Suggested warning:

```text
Current age appears outside the expected range for this simulation.
```

The project should avoid collecting real personal data. Age values should be fictional or anonymised.

---

## Age at End of Loan Validation

The calculator may estimate age at the end of the simulated loan:

```text
Age at End of Loan = Current Age + Loan Maturity in Years
```

The tool may flag high values for risk awareness.

Example configurable check:

```text
age_at_end_of_loan > 75
```

Suggested warning:

```text
The simulated age at the end of the loan appears high. This is a risk awareness flag only.
```

This should not be presented as an eligibility rule.

---

## DSTI Calculation Validation

DSTI should only be calculated when:

```text
monthly_net_income > 0
existing_monthly_commitments >= 0
proposed_monthly_instalment >= 0
```

Formula:

```text
Base DSTI (%) =
((Existing Monthly Credit Commitments + Proposed Monthly Instalment)
/
Monthly Net Income) × 100
```

If any required input is invalid, the calculation should not be performed.

Suggested warning:

```text
DSTI cannot be calculated because one or more required inputs are invalid.
```

---

## Stressed DSTI Calculation Validation

Stressed DSTI should only be calculated when:

```text
monthly_net_income > 0
existing_monthly_commitments >= 0
stressed_monthly_instalment >= 0
```

Formula:

```text
Stressed DSTI (%) =
((Existing Monthly Credit Commitments + Stressed Instalment)
/
Monthly Net Income) × 100
```

Suggested warning:

```text
Stressed DSTI cannot be calculated because one or more required inputs are invalid.
```

---

## Extreme DSTI Values

The tool may flag unusually high DSTI results.

Example configurable checks:

```text
base_dsti > 50
stressed_dsti > 60
base_dsti > 100
stressed_dsti > 100
```

Suggested warning:

```text
The calculated DSTI is unusually high. Please review the assumptions used in the simulation.
```

High DSTI values should be presented as risk awareness indicators only.

They should not be treated as automatic rejection.

---

## Incoherent Credit Scenarios

The tool should flag scenarios that appear incoherent.

Examples:

```text
loan_amount > 0 but proposed_monthly_instalment = 0
property_value = 0 but LTV calculation requested
stressed_instalment < proposed_instalment
loan_maturity_years = 0 but loan_amount > 0
monthly_net_income = 0 but DSTI calculation requested
```

Suggested warning:

```text
The scenario contains inconsistent assumptions. Please review the input values before interpreting the output.
```

---

## Incomplete Assumptions

The tool should identify cases where a scenario is incomplete.

Examples:

```text
missing stressed instalment
missing DSTI threshold
missing loan maturity
missing property value for LTV
```

Suggested warning:

```text
Some assumptions are incomplete. The simulation output may be limited.
```

---

## Warning Severity Levels

The project may use warning severity levels.

Suggested structure:

```text
Info: explanatory note
Warning: input should be reviewed
High warning: scenario may be materially affected
Blocking error: calculation cannot be performed
```

Example:

```text
Info:
This simulation uses fictional values only.

Warning:
The stressed instalment is lower than the proposed instalment.

High warning:
The stressed DSTI is unusually high.

Blocking error:
Monthly net income must be greater than zero.
```

---

## Blocking Errors

The following issues should normally block calculation:

```text
missing monthly net income
monthly net income <= 0
negative proposed instalment
negative existing commitments
invalid DSTI threshold
loan amount <= 0 when LTV is requested
property value <= 0 when LTV is requested
```

Blocking errors prevent misleading outputs.

---

## Non-Blocking Warnings

The following issues may allow calculation but should be clearly flagged:

```text
unusually high income
unusually high existing commitments
proposed instalment greater than income
stressed instalment lower than proposed instalment
high DSTI
high stressed DSTI
high age at end of loan
high LTV
incomplete optional assumptions
```

Non-blocking warnings support explainability and risk awareness.

---

## Example Validation Output

Example fictional input:

```text
monthly_net_income = 2500
existing_monthly_commitments = 300
proposed_monthly_instalment = 650
stressed_monthly_instalment = 780
configured_dsti_threshold = 40
loan_amount = 180000
property_value = 215000
loan_maturity_years = 30
current_age = 35
```

Possible validation result:

```text
Validation status: Passed with no blocking errors

Warnings:
- Stressed DSTI should be reviewed if it exceeds the configured threshold.
- LTV is calculated using the property value assumption selected by the user.
```

---

## Example Blocking Error Output

Example fictional input:

```text
monthly_net_income = 0
existing_monthly_commitments = 300
proposed_monthly_instalment = 650
```

Possible validation result:

```text
Validation status: Failed

Blocking errors:
- Monthly net income must be greater than zero to calculate DSTI.
```

---

## Responsible Validation Design

Validation messages should be:

- clear;
- neutral;
- educational;
- non-alarming;
- non-advisory;
- transparent;
- easy to understand.

The tool should avoid language such as:

```text
Approved
Rejected
Eligible
Not eligible
Credit accepted
Credit refused
```

Preferred wording:

```text
Scenario requires review
Risk awareness warning
Input assumption appears unusual
Calculation cannot be completed with current inputs
Scenario exceeds configured simulation threshold
```

---

## Summary

The validation rules in this document are designed to support responsible financial simulations.

They help ensure that the **DSTI Affordability Calculator** produces outputs based on coherent, complete and explainable inputs.

The validation layer supports the project’s focus on financial data quality, explainability, financial literacy and risk awareness.

These rules are educational and must not be interpreted as formal credit policy, financial advice or lending decision criteria.
