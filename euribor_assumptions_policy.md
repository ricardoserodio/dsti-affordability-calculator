# EURIBOR Assumptions Policy

## Purpose of This Document

This document explains how EURIBOR assumptions are handled in the **DSTI Affordability Calculator**.

The purpose is to keep the project transparent, educational, robust and portfolio-safe.

The app may use a simulated EURIBOR assumption as part of the interest rate build logic:

```text
Simulated EURIBOR + Simulated Spread = Base Annual Interest Rate
```

Then:

```text
Base Annual Interest Rate + Stress Buffer = Stressed Annual Interest Rate
```

This approach makes the simulation more realistic while keeping the project clearly educational.

---

## Project Positioning

The **DSTI Affordability Calculator** is a banking-inspired financial affordability simulation tool focused on:

```text
Financial literacy
DSTI simulation
Affordability analysis
Interest rate sensitivity
Data validation
Explainability
Risk awareness
Human-in-the-loop interpretation
```

It is not:

```text
A credit approval system
A lending decision engine
A bank pricing model
A financial advisory tool
A real-time market data platform
A replacement for formal banking analysis
```

---

## How EURIBOR Is Used in This Project

In the current version, EURIBOR is treated as a **manual simulated assumption**.

This means the user enters a fictional, simulated or educational EURIBOR value.

Example:

```text
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
```

The app then calculates:

```text
Base annual interest rate = 3.00% + 0.90%
Base annual interest rate = 3.90%
```

And:

```text
Stressed annual interest rate = 3.90% + 1.50%
Stressed annual interest rate = 5.40%
```

These values are then used to estimate base and stressed instalments.

---

## Why EURIBOR Is Manual in the First Version

The first version uses manual EURIBOR input because it is:

```text
More transparent
Easier to test
Easier to explain
Less dependent on external data sources
More robust for portfolio demonstration
Safer from a compliance and data quality perspective
```

Manual input also avoids the risk of the app failing because an external data source is unavailable.

---

## Not Live Market Data

The EURIBOR value entered in the app is not live market data.

It should be interpreted only as:

```text
A simulated assumption
A manual educational input
A scenario analysis variable
A risk awareness parameter
```

It must not be interpreted as:

```text
An official EURIBOR quote
A real-time benchmark value
A bank pricing input
A loan offer
A recommendation
A financial advice output
```

---

## Future Automatic EURIBOR Update

A future version of the project may include optional automatic EURIBOR retrieval.

However, automatic retrieval should be designed carefully.

A responsible future implementation should include:

```text
Source name
Reference date
Last update date
Selected EURIBOR tenor
Fallback to manual input
Clear disclaimer
Error handling
Data validation checks
No dependency on unofficial scraping
```

The app should remain usable even if automatic EURIBOR retrieval fails.

---

## Recommended Future Architecture

A future automatic EURIBOR module could follow this structure:

```text
src/euribor_provider.py
```

Possible workflow:

```text
1. Try to fetch EURIBOR reference data from a suitable public source.
2. Validate the returned value.
3. Validate the reference date.
4. Display the source and last updated date.
5. If fetching fails, fall back to manual EURIBOR input.
6. Clearly label whether the value is manual or automatically retrieved.
```

---

## Manual Fallback Principle

The manual fallback is important.

The app should never become unusable just because a data source is unavailable.

Recommended behaviour:

```text
If automatic EURIBOR retrieval succeeds:
    Use retrieved value as optional reference.

If automatic EURIBOR retrieval fails:
    Show a warning.
    Continue with manual simulated EURIBOR input.
```

This supports robustness and responsible data quality design.

---

## Data Quality Checks for EURIBOR

The app should treat EURIBOR assumptions as financial data inputs that require validation.

Potential checks include:

```text
Missing EURIBOR value
Non-numeric EURIBOR value
Extremely high EURIBOR value
Negative EURIBOR value
Outdated automatic reference date
Missing source name
Missing last updated date
Manual value not clearly labelled
Automatically retrieved value not validated
```

Some issues may block calculation.

Other issues may generate warnings or review notes.

---

## Negative EURIBOR

Negative EURIBOR assumptions may be allowed for educational scenario analysis because negative reference rate environments have existed historically.

However, negative EURIBOR should trigger a data quality note.

Example:

```text
Simulated EURIBOR: -0.50%
Simulated spread: 1.00%

Base annual interest rate = 0.50%
```

Recommended interpretation:

```text
The simulated EURIBOR assumption is negative. This may be intentional for scenario analysis, but should be reviewed before interpreting the output.
```

---

## EURIBOR Tenor Considerations

A future version may allow the user to select a simulated EURIBOR tenor.

Examples:

```text
EURIBOR 3M
EURIBOR 6M
EURIBOR 12M
```

However, the app should not imply that one tenor is recommended.

The tenor should be treated only as an educational scenario assumption.

---

## Spread Assumption

The spread in this project is also simulated.

Example:

```text
Simulated spread: 0.90%
```

The spread should not be interpreted as:

```text
A real bank spread
A negotiated spread
A guaranteed spread
A pricing offer
A credit approval indication
```

It is simply a manual assumption used to build an educational annual interest rate.

---

## Stress Buffer Assumption

The stress buffer is used to simulate a less favourable interest rate scenario.

Example:

```text
Stress buffer: 1.50%
```

The stress buffer is not:

```text
A regulatory rule
A bank policy rule
A formal stress test
A guarantee of future interest rate movement
```

It is a configurable educational assumption.

---

## Full Example

Assume the following fictional inputs:

```text
Loan amount: €180,000
Loan maturity: 30 years
Simulated EURIBOR: 3.00%
Simulated spread: 0.90%
Stress buffer: 1.50%
```

Base annual rate:

```text
3.00% + 0.90% = 3.90%
```

Stressed annual rate:

```text
3.90% + 1.50% = 5.40%
```

The app may then estimate:

```text
Base monthly instalment
Stressed monthly instalment
Base DSTI
Stressed DSTI
Monthly payment increase
Total repayment increase
```

All results remain educational and indicative only.

---

## Responsible Wording

Preferred wording:

```text
Simulated EURIBOR assumption
Manual EURIBOR input
Reference rate assumption
Simulated spread
Configured stress buffer
Base annual interest rate assumption
Stressed annual interest rate assumption
Educational simulation
```

Avoid wording:

```text
Live EURIBOR
Official rate
Guaranteed rate
Approved rate
Bank pricing
Credit offer
Best available spread
Recommended interest rate
```

---

## Privacy and Data Protection

EURIBOR assumptions do not require personal data.

Users should not enter:

```text
Real client identifiers
Real loan contracts
Real bank pricing documents
Confidential bank information
Personal financial documents
Internal credit policy information
```

The app should only use fictional, simulated, manual or public reference values.

---

## Human-in-the-Loop Principle

EURIBOR assumptions should be interpreted by a human.

A human reviewer should consider:

```text
Whether the EURIBOR assumption is reasonable
Whether the spread assumption is coherent
Whether the stress buffer is appropriate for the scenario
Whether the base annual rate appears unusually high or low
Whether the stressed rate creates affordability pressure
Whether the output should be interpreted cautiously
```

The tool supports understanding.

It does not replace judgement.

---

## Summary

The **DSTI Affordability Calculator** currently treats EURIBOR as a manual simulated assumption.

This keeps the project transparent, testable and robust.

A future version may include optional automatic EURIBOR retrieval, but only with clear source labelling, validation, fallback logic and disclaimers.

The project should always remain educational, explainable, privacy-conscious and human-in-the-loop.
