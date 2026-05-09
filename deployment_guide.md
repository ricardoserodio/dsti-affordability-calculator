# Deployment Guide

## Purpose of This Guide

This guide explains how the **DSTI Affordability Calculator** can be deployed as a Streamlit application.

The project is educational, demonstrative and portfolio-oriented.

The deployed application must remain a financial literacy and affordability simulation tool. It must not be presented as a credit approval system, underwriting engine, financial advisory tool or replacement for formal banking analysis.

All examples, inputs and outputs should use fictional, simulated or anonymised values only.

---

## Recommended Deployment Option

The recommended deployment option for this project is:

```text
Streamlit Community Cloud
```

Streamlit Community Cloud is suitable because the project is:

```text
Python-based
Streamlit-based
lightweight
portfolio-oriented
easy to share with recruiters
simple to maintain
```

---

## Repository Requirements

Before deployment, the GitHub repository should include:

```text
README.md
requirements.txt
app/streamlit_app.py
src/
examples/
tests/
.github/workflows/python-tests.yml
```

The main Streamlit app file is:

```text
app/streamlit_app.py
```

The dependencies are listed in:

```text
requirements.txt
```

---

## Deployment Steps

### 1. Push the Project to GitHub

Make sure all project files are committed to the `main` branch.

Important files:

```text
app/streamlit_app.py
requirements.txt
src/dsti_calculator.py
src/income_calculator.py
src/ltv_calculator.py
src/maturity_validator.py
src/validation_checks.py
src/scenario_engine.py
```

---

### 2. Go to Streamlit Community Cloud

Open Streamlit Community Cloud and connect the GitHub account that contains the repository.

Repository name:

```text
dsti-affordability-calculator
```

---

### 3. Select the Repository

Choose the GitHub repository:

```text
ricardoserodio/dsti-affordability-calculator
```

Select the branch:

```text
main
```

---

### 4. Define the App Entry Point

Set the main file path as:

```text
app/streamlit_app.py
```

This tells Streamlit which file should be executed when the app starts.

---

### 5. Deploy the App

Click deploy.

Streamlit will:

```text
clone the GitHub repository
install dependencies from requirements.txt
run app/streamlit_app.py
generate a public app URL
```

---

## Expected App Behaviour

After deployment, the app should display:

```text
DSTI Affordability Calculator
Educational simulation disclaimer
Income input section
Credit commitments section
DSTI assumptions
Optional LTV simulation
Optional maturity simulation
Simulation summary
Key metrics
Validation warnings
Scenario comparison
Footer disclaimer
```

---

## Important Deployment Disclaimer

The deployed version must clearly state that the tool:

```text
does not approve or reject credit
does not provide financial advice
does not replace formal banking analysis
does not use real client data
does not request real personal documents
does not represent any bank's internal policy
```

This disclaimer should remain visible in the app interface.

---

## Privacy Requirements

The deployed app must not collect, store or process real personal data.

Users should only enter:

```text
fictional values
simulated values
anonymised values
educational assumptions
```

The app must not request:

```text
real payslips
real tax returns
real credit responsibility maps
real bank statements
real personal identifiers
real client documents
```

---

## Data Storage

This version of the application should not store user inputs.

The app should run calculations during the session only.

Recommended principle:

```text
No database
No user accounts
No document uploads
No personal data storage
No OCR
No real client data
```

---

## Environment Variables

The initial version of the project does not require environment variables.

No API keys, database credentials or secrets should be needed.

If future versions require configuration, sensitive information should never be committed to GitHub.

---

## Testing Before Deployment

Before deploying, run the tests locally:

```bash
pytest tests/
```

The GitHub Actions workflow should also run automatically after commits to the `main` branch.

The workflow file is:

```text
.github/workflows/python-tests.yml
```

---

## Common Deployment Issues

### Missing Dependency

If Streamlit fails because a package is missing, add it to:

```text
requirements.txt
```

Then commit the change.

---

### Wrong App Path

If Streamlit cannot find the app file, confirm that the entry point is:

```text
app/streamlit_app.py
```

---

### Import Error

If the app cannot import modules from `src/`, check that `streamlit_app.py` includes the project root and `src` path correctly.

Expected structure:

```text
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
```

---

### Tests Failing

If GitHub Actions tests fail, review:

```text
Actions tab
Python error message
failed test name
affected module
```

Fix the issue in the relevant file and commit again.

---

## Suggested Public App Description

Suggested short description for the deployed app:

```text
Banking-inspired financial affordability and DSTI simulation tool focused on financial literacy, data validation, explainability and risk awareness.
```

---

## Suggested Portfolio Description

Suggested portfolio description:

```text
Built a Streamlit-based DSTI affordability simulator using Python, pandas and modular validation logic. The project demonstrates banking-inspired affordability analysis, financial data quality checks, scenario comparison, risk awareness and explainable financial outputs using fictional data only.
```

---

## Limitations of Deployment

The deployed app is still a simplified educational tool.

It does not include:

```text
formal credit scoring
real affordability verification
document validation
OCR
client onboarding
bank policy rules
regulatory assessment
personalised financial advice
database storage
authentication
```

---

## Responsible Use

The deployed version should always reinforce:

```text
financial literacy
responsible simulation
transparent assumptions
data validation
risk awareness
human-in-the-loop interpretation
privacy awareness
```

It should never encourage users to treat outputs as lending decisions.

---

## Summary

The **DSTI Affordability Calculator** can be deployed as a lightweight Streamlit app for portfolio demonstration.

The deployment should remain simple, transparent and privacy-conscious.

The app should be positioned as an educational financial affordability simulator, not as a credit approval or financial advice tool.
