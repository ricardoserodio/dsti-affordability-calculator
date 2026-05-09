# UI Mockup

## Purpose of This Document

This document describes the proposed user interface for the **DSTI Affordability Calculator**.

The objective is to design a clean, professional and explainable interface suitable for a GitHub portfolio project.

The interface should be understandable by both banking professionals and non-technical users.

The application is educational and demonstrative only. It must not approve or reject credit, provide financial advice or replace formal banking analysis.

---

## UI Positioning

The interface should support the following principles:

- financial literacy;
- explainability;
- responsible simulation;
- financial data validation;
- risk awareness;
- transparency;
- human-in-the-loop interpretation.

The interface should avoid any wording that suggests a lending decision.

Avoid labels such as:

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
Simulation summary
Risk awareness warning
Scenario requires review
Configured simulation threshold exceeded
Indicative result
Educational output only
```

---

## Proposed Page Title

```text
DSTI Affordability Calculator
```

Suggested subtitle:

```text
Banking-inspired financial affordability and DSTI simulation tool focused on financial literacy, data validation, explainability and risk awareness.
```

---

## Disclaimer Banner

A warning banner should be displayed at the top of the application.

Suggested text:

```text
Educational simulation only. This tool does not approve or reject credit, does not provide financial advice and does not replace formal banking analysis. Use fictional, simulated or anonymised values only.
```

---

## Main Layout

The application should use a simple two-area layout:

```text
Sidebar:
- User inputs
- Scenario assumptions
- Optional LTV inputs
- Optional maturity inputs

Main page:
- Simulation summary
- Key metrics
- DSTI details
- LTV details
- Maturity details
- Validation warnings
- Scenario comparison
- Methodology notes
```

---

## Sidebar Structure

The sidebar should contain all user inputs.

Suggested sections:

```text
1. Income
2. Credit Commitments
3. DSTI Assumptions
4. Optional LTV Inputs
5. Optional Maturity Inputs
6. Scenario Settings
```

---

## Income Section

Suggested fields:

```text
Monthly net income — Source 1 (€)
Monthly net income — Source 2 (€)
Use conservative income assumption
Conservative income factor
```

Purpose:

```text
Allow the user to simulate household income and optionally apply a conservative income assumption.
```

Important note:

```text
Income values should be fictional, simulated or anonymised.
```

---

## Credit Commitments Section

Suggested fields:

```text
Existing monthly credit commitments (€)
Proposed monthly instalment (€)
Stressed monthly instalment (€)
```

Purpose:

```text
Allow the user to compare current debt commitments with a proposed and stressed future instalment.
```

Validation notes:

```text
- values should not be negative;
- stressed instalment should normally be equal to or higher than proposed instalment;
- high instalments relative to income should trigger warnings.
```

---

## DSTI Assumptions Section

Suggested field:

```text
Configured DSTI threshold for simulation (%)
```

Purpose:

```text
Allow the user to define a simulation threshold for educational scenario comparison.
```

Important wording:

```text
This threshold is a configurable simulation assumption only. It is not an official banking rule or eligibility criterion.
```

---

## Optional LTV Inputs Section

Suggested fields:

```text
Include LTV simulation
Simulated loan amount (€)
Simulated acquisition value (€)
Simulated valuation value (€)
Configured LTV threshold for simulation (%)
Use lower of acquisition and valuation value
```

Purpose:

```text
Allow the user to understand the relationship between simulated loan amount and property value assumptions.
```

Important wording:

```text
Any LTV threshold used is a simulation assumption only and must not be interpreted as a formal lending rule.
```

---

## Optional Maturity Inputs Section

Suggested fields:

```text
Include maturity simulation
Fictional or anonymised current age
Simulated loan maturity in years
Configured maximum age assumption
```

Purpose:

```text
Allow the user to understand how maturity and age-at-end-of-loan assumptions affect risk awareness.
```

Important wording:

```text
The maturity check is educational only and does not represent an eligibility decision.
```

---

## Main Page Structure

The main page should be organised as follows:

```text
1. Simulation Summary
2. Key Metrics
3. DSTI Details
4. LTV Details
5. Maturity Details
6. Validation Notes
7. Scenario Comparison
8. Methodology and Limitations
```

---

## Simulation Summary Section

This section should provide a short explainable summary of the scenario.

Suggested title:

```text
Simulation Summary
```

Suggested content style:

```text
The scenario was processed using fictional, simulated or anonymised values.

The output is educational and must not be interpreted as credit approval, rejection, eligibility confirmation or financial advice.

Base DSTI: 38.0%.
Stressed DSTI: 43.2%.

Risk awareness warning: the stressed DSTI exceeds the configured simulation threshold. This does not represent credit rejection, but it suggests that the scenario may require careful review.
```

---

## Key Metrics Section

Suggested metrics:

```text
Monthly Net Income
Base DSTI
Stressed DSTI
Remaining Capacity
```

Example layout:

```text
| Monthly Net Income | Base DSTI | Stressed DSTI | Remaining Capacity |
|--------------------|-----------|---------------|--------------------|
| €2,500.00          | 38.00%    | 43.20%        | €700.00            |
```

The metrics should be visually clear and easy to interpret.

---

## DSTI Details Section

Suggested table:

```text
Metric                              Value
Base DSTI                           38.00%
Stressed DSTI                       43.20%
Maximum monthly debt service        €1,000.00
Remaining repayment capacity        €700.00
Margin against stressed instalment  -€80.00
```

Purpose:

```text
Explain how the scenario behaves under both base and stressed assumptions.
```

---

## LTV Details Section

Suggested table:

```text
Metric               Value
Loan amount          €180,000.00
Property value used  €215,000.00
Simulated LTV        83.72%
```

Purpose:

```text
Explain the relationship between loan amount and property value assumption.
```

---

## Maturity Details Section

Suggested table:

```text
Metric                         Value
Current age                    35
Loan maturity in years         30
Age at end of loan             65
Within configured assumption   True
```

Purpose:

```text
Explain maturity and age-at-end-of-loan assumptions clearly.
```

---

## Validation Notes Section

This section should display validation results.

Suggested structure:

```text
Validation Status
- Passed
- Passed with warnings
- Failed due to blocking errors
```

Example non-blocking warning:

```text
The stressed instalment is lower than the proposed instalment. Please confirm this assumption.
```

Example blocking error:

```text
Monthly net income must be greater than zero to calculate DSTI.
```

---

## Scenario Comparison Section

The application should include a comparison between at least two scenarios:

```text
Base simulation
Prudent income simulation
```

Suggested comparison table:

```text
scenario_name                 validation_status  warning_count  base_dsti_percentage  stressed_dsti_percentage  remaining_repayment_capacity
Base simulation               valid              1              38.00                 43.20                     700.00
Prudent income simulation     valid              1              42.22                 48.00                     600.00
```

Purpose:

```text
Show how a conservative income assumption changes affordability indicators.
```

---

## Methodology and Limitations Section

The UI should include an expandable section with methodology notes.

Suggested title:

```text
Methodology and Limitations
```

Suggested text:

```text
This simulation uses simplified assumptions and does not verify income, credit history, employment stability, property valuation, legal documentation or bank-specific credit policy.

The outputs are educational and indicative only.
```

---

## Privacy Notice Section

The interface should include a clear privacy notice.

Suggested text:

```text
This tool does not request, store, process or analyse real personal documents.

Users should only enter fictional, simulated or anonymised values.

References to payslips, tax statements, credit responsibility maps or loan simulations are educational only.
```

---

## Suggested Visual Style

The interface should be:

```text
Professional
Clean
Minimalistic
Readable
Neutral
Banking-inspired
Portfolio-friendly
```

Avoid overly aggressive colours or sales-oriented language.

Suggested visual priorities:

```text
- clear headings;
- short explanatory text;
- simple input sections;
- metric cards;
- tables for details;
- warnings displayed in neutral language;
- expandable methodology notes;
- footer disclaimer.
```

---

## Suggested User Flow

Recommended user flow:

```text
1. User reads the educational disclaimer.
2. User enters fictional income values.
3. User enters existing commitments.
4. User enters proposed and stressed instalments.
5. User optionally includes LTV assumptions.
6. User optionally includes maturity assumptions.
7. App validates inputs.
8. App displays DSTI and scenario outputs.
9. App displays warnings and explanations.
10. User reviews methodology and limitations.
```

---

## Example Wireframe

```text
+------------------------------------------------------------+
| DSTI Affordability Calculator                              |
| Banking-inspired affordability simulation                  |
+------------------------------------------------------------+
| Educational simulation only disclaimer banner              |
+-------------------------+----------------------------------+
| Sidebar Inputs          | Simulation Summary               |
|                         |                                  |
| Income                  | Key Metrics                      |
| - Source 1              | [Income] [Base DSTI] [Stress]    |
| - Source 2              |                                  |
| - Conservative option   | DSTI Details                     |
|                         |                                  |
| Credit Commitments      | LTV Details                      |
| - Existing commitments  |                                  |
| - Proposed instalment   | Maturity Details                 |
| - Stressed instalment   |                                  |
|                         | Validation Notes                 |
| LTV Inputs              |                                  |
|                         | Scenario Comparison              |
| Maturity Inputs         |                                  |
+-------------------------+----------------------------------+
| Footer disclaimer and privacy note                         |
+------------------------------------------------------------+
```

---

## Language Guidelines

Use clear and prudent wording.

Preferred phrases:

```text
Indicative simulation
Educational output
Risk awareness warning
Configured simulation assumption
Scenario requires review
Financial effort
Affordability pressure
```

Avoid phrases:

```text
Approved
Rejected
Eligible
Not eligible
Safe
Guaranteed
Recommended
Bank accepted
Bank refused
```

---

## Summary

The UI should make the simulation easy to understand, transparent and professionally presented.

The design should reinforce the project's key principles:

```text
Financial literacy
Data validation
Explainability
Risk awareness
Prudent affordability analysis
Human-in-the-loop interpretation
Privacy awareness
```

The application must always remain educational, demonstrative and portfolio-oriented.
