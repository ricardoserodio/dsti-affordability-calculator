"""
Streamlit application for the DSTI Affordability Calculator.

This app provides a clean, educational and banking-inspired interface for
simulating financial affordability, DSTI, LTV and maturity scenarios.

The application is for educational, demonstrative and portfolio purposes only.
It does not approve or reject credit, provide financial advice or replace
formal human credit analysis.

All values entered should be fictional, simulated or anonymised.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from scenario_engine import compare_scenarios, run_affordability_scenario


st.set_page_config(
    page_title="DSTI Affordability Calculator",
    page_icon="🏦",
    layout="wide",
)


def format_currency(value: float | None) -> str:
    """
    Format numeric values as euros for display.

    Args:
        value:
            Numeric value to format.

    Returns:
        Formatted euro string.
    """

    if value is None:
        return "N/A"

    return f"€{value:,.2f}"


def format_percentage(value: float | None) -> str:
    """
    Format numeric values as percentages for display.

    Args:
        value:
            Numeric value to format.

    Returns:
        Formatted percentage string.
    """

    if value is None:
        return "N/A"

    return f"{value:.2f}%"


st.title("DSTI Affordability Calculator")

st.caption(
    "Banking-inspired financial affordability and DSTI simulation tool focused "
    "on financial literacy, data validation, explainability and risk awareness."
)

st.warning(
    "Educational simulation only. This tool does not approve or reject credit, "
    "does not provide financial advice and does not replace formal banking "
    "analysis. Use fictional, simulated or anonymised values only."
)

with st.sidebar:
    st.header("Simulation Inputs")

    st.subheader("Income")
    income_source_1 = st.number_input(
        "Monthly net income — Source 1 (€)",
        min_value=0.0,
        value=1500.0,
        step=50.0,
    )

    income_source_2 = st.number_input(
        "Monthly net income — Source 2 (€)",
        min_value=0.0,
        value=1000.0,
        step=50.0,
    )

    use_conservative_income = st.checkbox(
        "Use conservative income assumption",
        value=False,
    )

    conservative_factor = st.slider(
        "Conservative income factor",
        min_value=0.50,
        max_value=1.00,
        value=0.90,
        step=0.01,
    )

    st.subheader("Credit Commitments")
    existing_monthly_commitments = st.number_input(
        "Existing monthly credit commitments (€)",
        min_value=0.0,
        value=300.0,
        step=25.0,
    )

    proposed_monthly_instalment = st.number_input(
        "Proposed monthly instalment (€)",
        min_value=0.0,
        value=650.0,
        step=25.0,
    )

    stressed_monthly_instalment = st.number_input(
        "Stressed monthly instalment (€)",
        min_value=0.0,
        value=780.0,
        step=25.0,
    )

    configured_dsti_threshold_percentage = st.slider(
        "Configured DSTI threshold for simulation (%)",
        min_value=1.0,
        max_value=100.0,
        value=40.0,
        step=1.0,
    )

    st.subheader("Optional LTV Inputs")
    include_ltv = st.checkbox("Include LTV simulation", value=True)

    if include_ltv:
        loan_amount = st.number_input(
            "Simulated loan amount (€)",
            min_value=0.0,
            value=180000.0,
            step=1000.0,
        )

        acquisition_value = st.number_input(
            "Simulated acquisition value (€)",
            min_value=0.0,
            value=220000.0,
            step=1000.0,
        )

        valuation_value = st.number_input(
            "Simulated valuation value (€)",
            min_value=0.0,
            value=215000.0,
            step=1000.0,
        )

        configured_ltv_threshold_percentage = st.slider(
            "Configured LTV threshold for simulation (%)",
            min_value=1.0,
            max_value=100.0,
            value=90.0,
            step=1.0,
        )

        use_lower_property_value = st.checkbox(
            "Use lower of acquisition and valuation value",
            value=True,
        )
    else:
        loan_amount = None
        acquisition_value = None
        valuation_value = None
        configured_ltv_threshold_percentage = None
        use_lower_property_value = True

    st.subheader("Optional Maturity Inputs")
    include_maturity = st.checkbox("Include maturity simulation", value=True)

    if include_maturity:
        current_age = st.number_input(
            "Fictional or anonymised current age",
            min_value=0.0,
            value=35.0,
            step=1.0,
        )

        loan_maturity_years = st.number_input(
            "Simulated loan maturity in years",
            min_value=0.0,
            value=30.0,
            step=1.0,
        )

        configured_maximum_age_at_end = st.number_input(
            "Configured maximum age assumption",
            min_value=1.0,
            value=75.0,
            step=1.0,
        )
    else:
        current_age = None
        loan_maturity_years = None
        configured_maximum_age_at_end = 75.0


income_sources = [income_source_1, income_source_2]

scenario = run_affordability_scenario(
    scenario_name="Base simulation",
    income_sources=income_sources,
    existing_monthly_commitments=existing_monthly_commitments,
    proposed_monthly_instalment=proposed_monthly_instalment,
    stressed_monthly_instalment=stressed_monthly_instalment,
    configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
    use_conservative_income=use_conservative_income,
    conservative_factor=conservative_factor,
    loan_amount=loan_amount,
    acquisition_value=acquisition_value,
    valuation_value=valuation_value,
    configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
    use_lower_property_value=use_lower_property_value,
    loan_maturity_years=loan_maturity_years,
    current_age=current_age,
    configured_maximum_age_at_end=configured_maximum_age_at_end,
)

st.header("Simulation Summary")

st.write(scenario.summary)

if not scenario.validation.is_valid:
    st.error("Blocking validation errors were identified.")

    for error in scenario.validation.blocking_errors:
        st.write(f"- {error}")

else:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Monthly Net Income",
            format_currency(scenario.income.monthly_net_income),
        )

    with col2:
        st.metric(
            "Base DSTI",
            format_percentage(scenario.dsti.base_dsti_percentage),
        )

    with col3:
        st.metric(
            "Stressed DSTI",
            format_percentage(scenario.dsti.stressed_dsti_percentage),
        )

    with col4:
        st.metric(
            "Remaining Capacity",
            format_currency(scenario.dsti.remaining_repayment_capacity),
        )

    st.subheader("DSTI Details")

    dsti_table = pd.DataFrame(
        [
            {
                "Metric": "Base DSTI",
                "Value": format_percentage(scenario.dsti.base_dsti_percentage),
            },
            {
                "Metric": "Stressed DSTI",
                "Value": format_percentage(
                    scenario.dsti.stressed_dsti_percentage
                ),
            },
            {
                "Metric": "Maximum monthly debt service",
                "Value": format_currency(
                    scenario.dsti.maximum_monthly_debt_service
                ),
            },
            {
                "Metric": "Remaining repayment capacity",
                "Value": format_currency(
                    scenario.dsti.remaining_repayment_capacity
                ),
            },
            {
                "Metric": "Margin against stressed instalment",
                "Value": format_currency(
                    scenario.dsti.margin_against_stressed_instalment
                ),
            },
        ]
    )

    st.dataframe(dsti_table, use_container_width=True)

    if scenario.ltv is not None:
        st.subheader("LTV Details")

        ltv_table = pd.DataFrame(
            [
                {
                    "Metric": "Loan amount",
                    "Value": format_currency(scenario.ltv.loan_amount),
                },
                {
                    "Metric": "Property value used",
                    "Value": format_currency(scenario.ltv.property_value_used),
                },
                {
                    "Metric": "Simulated LTV",
                    "Value": format_percentage(scenario.ltv.ltv_percentage),
                },
            ]
        )

        st.dataframe(ltv_table, use_container_width=True)

    if scenario.maturity is not None:
        st.subheader("Maturity Details")

        maturity_table = pd.DataFrame(
            [
                {
                    "Metric": "Current age",
                    "Value": scenario.maturity.current_age,
                },
                {
                    "Metric": "Loan maturity in years",
                    "Value": scenario.maturity.loan_maturity_years,
                },
                {
                    "Metric": "Age at end of loan",
                    "Value": scenario.maturity.age_at_end_of_loan,
                },
                {
                    "Metric": "Within configured assumption",
                    "Value": scenario.maturity.is_within_configured_assumption,
                },
            ]
        )

        st.dataframe(maturity_table, use_container_width=True)

    st.subheader("Validation Notes")

    if scenario.validation.warnings:
        st.warning("Non-blocking validation warnings were identified.")

        for warning in scenario.validation.warnings:
            st.write(f"- {warning}")
    else:
        st.success("No non-blocking validation warnings were identified.")

    with st.expander("Information messages"):
        for message in scenario.validation.info_messages:
            st.write(f"- {message}")

    st.subheader("Scenario Comparison Example")

    prudent_scenario = run_affordability_scenario(
        scenario_name="Prudent income simulation",
        income_sources=income_sources,
        existing_monthly_commitments=existing_monthly_commitments,
        proposed_monthly_instalment=proposed_monthly_instalment,
        stressed_monthly_instalment=stressed_monthly_instalment,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
        use_conservative_income=True,
        conservative_factor=conservative_factor,
        loan_amount=loan_amount,
        acquisition_value=acquisition_value,
        valuation_value=valuation_value,
        configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
        use_lower_property_value=use_lower_property_value,
        loan_maturity_years=loan_maturity_years,
        current_age=current_age,
        configured_maximum_age_at_end=configured_maximum_age_at_end,
    )

    comparison_table = pd.DataFrame(
        compare_scenarios([scenario, prudent_scenario])
    )

    st.dataframe(comparison_table, use_container_width=True)

st.divider()

st.caption(
    "This project is educational and demonstrative. It does not use real client "
    "data, does not process personal documents and does not represent any "
    "bank's internal credit policy."
)
