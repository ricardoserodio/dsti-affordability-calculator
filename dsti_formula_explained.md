# DSTI Formula Explained

## What Is DSTI?

DSTI stands for **Debt Service-to-Income**.

It is a financial ratio that compares monthly debt payments with monthly net income.

In simple terms, DSTI helps answer the question:

```text
How much of the monthly net income is used to pay credit commitments?
```

This project uses DSTI as an educational indicator of financial effort and affordability awareness.

It must not be interpreted as credit approval, rejection, financial advice or a formal banking decision.

---

## Simplified DSTI Formula

The simplified formula used in this project is:

```text
DSTI = Total Monthly Debt Payments / Monthly Net Income
```

Expressed as a percentage:

```text
DSTI (%) = (Total Monthly Debt Payments / Monthly Net Income) × 100
```

---

## Total Monthly Debt Payments

For this project, total monthly debt payments are calculated as:

```text
Total Monthly Debt Payments =
Existing Monthly Credit Commitments + Proposed Monthly Instalment
```

Where:

- **Existing Monthly Credit Commitments** represent current recurring credit payments;
- **Proposed Monthly Instalment** represents the estimated instalment of a new simulated credit scenario.

---

## Example Calculation

Assume a fictional household has the following values:

```text
Monthly net income: €2,500
Existing monthly credit commitments: €300
Proposed monthly instalment: €650
```

The total monthly debt payments would be:

```text
€300 + €650 = €950
```

The DSTI calculation would be:

```text
DSTI = €950 / €2,500
DSTI = 0.38
DSTI = 38%
```

This means that, in this simulated scenario, 38% of monthly net income would be used to pay monthly credit commitments.

---

## Stressed DSTI

This project may also calculate a stressed DSTI.

The stressed DSTI uses a higher instalment assumption to simulate a less favourable scenario.

The formula is:

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

---

## Example of Stressed DSTI

Assume the same fictional household:

```text
Monthly net income: €2,500
Existing monthly credit commitments: €300
Base proposed instalment: €650
Stressed instalment: €780
```

The stressed total monthly debt payments would be:

```text
€300 + €780 = €1,080
```

The stressed DSTI calculation would be:

```text
Stressed DSTI = €1,080 / €2,500
Stressed DSTI = 0.432
Stressed DSTI = 43.2%
```

This shows how affordability may become more pressured if the instalment increases.

---

## Why Stressed DSTI Matters

A base DSTI scenario may look manageable under current assumptions.

However, affordability can change if:

- interest rates increase;
- monthly instalments rise;
- income decreases;
- existing credit commitments increase;
- financial assumptions are incomplete;
- the maturity or repayment structure changes.

The stressed DSTI helps users understand how sensitive a scenario may be to less favourable conditions.

---

## Remaining Repayment Capacity

The calculator may estimate an indicative maximum monthly debt service amount using a configured DSTI threshold.

```text
Maximum Monthly Debt Service =
Monthly Net Income × Configured DSTI Threshold
```

Then:

```text
Remaining Repayment Capacity =
Maximum Monthly Debt Service - Existing Monthly Credit Commitments
```

This value is only an educational simulation output.

It must not be interpreted as approved borrowing capacity or guaranteed affordability.

---

## Margin Against Stressed Scenario

The calculator may compare remaining repayment capacity with the stressed instalment:

```text
Margin Against Stressed Scenario =
Remaining Repayment Capacity - Stressed Instalment
```

A positive margin may indicate that the stressed instalment remains below the configured simulation threshold.

A negative margin may indicate that the stressed instalment exceeds the configured simulation threshold.

This is not a credit decision.

---

## Interpretation of DSTI Results

DSTI should be interpreted cautiously.

A lower DSTI may suggest more available income after debt payments.

A higher DSTI may suggest greater financial pressure.

However, DSTI alone does not provide a complete view of affordability.

Other factors may also matter, such as:

- essential living expenses;
- household composition;
- employment stability;
- income variability;
- savings capacity;
- emergency reserves;
- property valuation;
- credit history;
- interest rate changes;
- wider economic conditions.

---

## Educational Risk Bands

This project may use educational risk bands to help explain results.

Example:

```text
Lower DSTI: potentially lower financial pressure in the simulation
Moderate DSTI: relevant financial effort to monitor
Higher DSTI: increased affordability pressure in the simulation
Very high DSTI: significant risk awareness warning
```

These bands are configurable simulation assumptions.

They are not official regulatory thresholds, credit approval rules or bank-specific criteria.

---

## Important Limitations

The DSTI calculation in this project is simplified.

It does not:

- verify real income;
- verify real credit commitments;
- assess credit history;
- assess employment stability;
- assess property valuation;
- include all household expenses;
- include all legal or regulatory criteria;
- represent any bank's internal credit policy;
- approve or reject credit.

---

## Responsible Use

This formula should be used only for:

- educational simulation;
- financial literacy;
- affordability awareness;
- portfolio demonstration;
- explainable banking-inspired analysis;
- data validation practice.

It should not be used for personal financial decision-making without professional review.

---

## Summary

DSTI is a useful educational indicator for understanding the relationship between debt commitments and income.

In this project, DSTI is used to demonstrate how income, existing credit commitments, proposed instalments and stress scenarios can affect affordability.

The calculator is designed to explain financial effort, not to make lending decisions.
