# Methodology

## Purpose of the Methodology

This document explains the methodology behind the **DSTI Affordability Calculator**.

The objective is to describe how the simulation works, which assumptions are considered, how the main calculations are performed and how outputs should be interpreted.

This methodology is educational and demonstrative. It does not represent any bank's internal credit policy, underwriting model or formal lending decision process.

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

The tool is designed to help users understand how income, existing credit commitments, proposed instalments and stress scenarios may affect financial effort.

It does not approve, reject or recommend credit.

---

## Core Concept: DSTI

DSTI stands for **Debt Service-to-Income**.

It measures the relationship between monthly debt payments and monthly net income.

In simplified form:

```text
DSTI = Total Monthly Debt Payments / Monthly Net Income
```

Expressed as a percentage:

```text
DSTI (%) = (Total Monthly Debt Payments / Monthly Net Income) × 100
```

For this project:

```text
Total Monthly Debt Payments =
Existing Monthly Credit Commitments + Proposed Monthly Instalment
```

---

## Main Inputs

The simulation may use the following fictional, simulated or anonymised inputs:

- monthly net income;
- existing monthly credit commitments;
- proposed monthly instalment;
- stressed or aggravated instalment;
- loan amount;
- property acquisition value;
- property valuation value;
- loan maturity;
- interest rate assumption;
- borrower age;
- configured DSTI threshold;
- configured LTV threshold.

Users should not input real personal or sensitive financial information.

---

## Income Treatment

The calculator focuses on monthly net income.

Depending on the stage of the project, income may be entered as:

- individual monthly net income;
- aggregated household monthly net income;
- manually adjusted income;
- conservative income assumption;
- simulated income scenario.

The tool should clearly explain which income figure is being used in the calculation.

The income value must be validated before calculation.

---

## Existing Credit Commitments

Existing credit commitments represent current monthly debt payments.

Examples may include, in fictional and educational form:

- existing mortgage instalments;
- personal loans;
- car loans;
- credit card repayment assumptions;
- other recurring credit commitments.

The calculator adds existing credit commitments to the proposed new instalment in order to calculate total monthly debt payments.

---

## Proposed Instalment

The proposed instalment represents the estimated monthly payment of a new simulated credit scenario.

This value may be:

- manually inserted;
- calculated externally and entered by the user;
- estimated by a simplified formula in future versions.

The proposed instalment is not a bank quote, offer or approval indication.

---

## Stressed Instalment

The stressed instalment represents a more prudent scenario where the future instalment is higher than the base instalment.

This may reflect, for example:

- higher interest rates;
- less favourable repayment conditions;
- conservative affordability testing;
- risk awareness purposes.

The stressed instalment helps users understand how affordability may change under less favourable conditions.

---

## Base DSTI Calculation

The base DSTI calculation uses the proposed instalment:

```text
Base DSTI =
(Existing Monthly Credit Commitments + Proposed Monthly Instalment)
/
Monthly Net Income
```

Expressed as a percentage:

```text
Base DSTI (%) =
((Existing Monthly Credit Commitments + Proposed Monthly Instalment)
/
Monthly Net Income) × 100
```

---

## Stressed DSTI Calculation

The stressed DSTI calculation uses the stressed instalment:

```text
Stressed DSTI =
(Existing Monthly Credit Commitments + Stressed Instalment)
/
Monthly Net Income
```

Expressed as a percentage:

```text
Stressed DSTI (%) =
((Existing Monthly Credit Commitments + Stressed Instalment)
/
Monthly Net Income) × 100
```

The stressed DSTI is useful for understanding whether a scenario remains sustainable under less favourable assumptions.

---

## Repayment Capacity Simulation

The calculator may estimate an indicative maximum monthly debt service amount based on a configured DSTI threshold.

```text
Maximum Monthly Debt Service =
Monthly Net Income × Configured DSTI Threshold
```

The remaining repayment capacity can then be estimated as:

```text
Remaining Capacity =
Maximum Monthly Debt Service - Existing Monthly Credit Commitments
```

This value is only indicative and based on simplified assumptions.

It must not be interpreted as an approved borrowing capacity.

---

## Margin Against Stressed Scenario

The calculator may compare the remaining capacity against the stressed instalment:

```text
Margin Against Stressed Scenario =
Remaining Capacity - Stressed Instalment
```

A positive margin may indicate that, within the simulation assumptions, the stressed instalment remains below the configured limit.

A negative margin may indicate that the stressed instalment exceeds the configured limit.

This is not a credit decision.

---

## Loan-to-Value Simulation

The tool may include a simplified LTV calculation.

LTV stands for **Loan-to-Value** and compares the loan amount with a property value assumption.

```text
LTV (%) = Loan Amount / Property Value × 100
```

The property value used in the simulation should be clearly explained, for example:

- acquisition value;
- valuation value;
- lower of acquisition and valuation value;
- manually configured value.

Any LTV threshold used in the tool must be presented as a configurable simulation assumption, not as a formal banking rule.

---

## Maturity and Age Scenario Check

The calculator may include a maturity-related check.

This can compare:

- current age;
- simulated loan maturity;
- estimated age at the end of the loan;
- configured maximum age assumption.

Example:

```text
Age at End of Loan = Current Age + Loan Maturity in Years
```

This check is educational and should not be interpreted as a formal eligibility rule.

---

## Scenario Analysis

The project may compare different scenarios, such as:

- base scenario;
- prudent scenario;
- stressed interest rate scenario;
- higher instalment scenario;
- lower income scenario;
- increased existing commitments scenario.

The goal is to show how small changes in assumptions may affect affordability.

---

## Risk Warnings

The tool may generate risk warnings when the simulation identifies factors such as:

- high DSTI;
- stressed DSTI significantly above base DSTI;
- low remaining capacity;
- negative margin against stressed scenario;
- unrealistic inputs;
- missing values;
- inconsistent maturity assumptions;
- unusual LTV values.

These warnings are educational indicators only.

They do not represent approval, rejection, suitability assessment or formal credit risk classification.

---

## Data Validation Methodology

Financial data quality is central to this project.

Before producing outputs, the tool should validate inputs for:

- missing values;
- negative values;
- zero income;
- invalid percentages;
- unrealistic income assumptions;
- unrealistic expense assumptions;
- inconsistent maturities;
- incoherent loan scenarios;
- incomplete assumptions;
- extreme or unusual DSTI values.

The purpose is to demonstrate responsible financial simulation design.

---

## Explainability Approach

Each output should be accompanied by a clear explanation.

The tool should explain:

- which inputs were used;
- how DSTI was calculated;
- why a scenario may be risky;
- how stressed assumptions affect affordability;
- what the main limitations are;
- why the result should not be interpreted as a decision.

The interface should be understandable by both banking professionals and non-technical users.

---

## Human-in-the-Loop Approach

This project follows a human-in-the-loop principle.

The calculator supports structured analysis, but interpretation must remain cautious and contextual.

The tool should never automatically approve or reject a credit scenario.

Human judgement, professional review and formal verification remain essential in real banking processes.

---

## Privacy and Data Protection

The project must not request, store, process or analyse real personal documents or real client data.

Any reference to documents such as payslips, tax statements, credit responsibility maps or loan simulations is purely educational.

Users should only input fictional, simulated or anonymised values.

The application should not perform OCR, document verification or client onboarding.

---

## Main Limitations

This simulation has several limitations:

- it uses simplified assumptions;
- it does not verify real income;
- it does not assess credit history;
- it does not assess employment stability;
- it does not perform property valuation;
- it does not consider all legal or regulatory requirements;
- it does not represent any bank's internal policy;
- it does not replace professional advice or formal credit analysis.

---

## Summary

The methodology behind this project is designed to be transparent, prudent and educational.

The calculator aims to demonstrate how DSTI, financial effort, stress scenarios and data validation can be combined into a responsible banking-inspired simulation tool.

It should always be interpreted as a financial literacy and portfolio project, not as a credit decision engine.
