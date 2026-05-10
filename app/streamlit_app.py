"""
Streamlit application for the DSTI Affordability Calculator.

This app provides a clean, educational and banking-inspired interface for
simulating financial affordability, DSTI, LTV, maturity and interest rate
stress scenarios.

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

from interest_rate_builder import build_interest_rate_assumptions
from interest_rate_stress import run_interest_rate_stress_test
from scenario_engine import compare_scenarios, run_affordability_scenario


st.set_page_config(
    page_title="DSTI Affordability Calculator",
    page_icon="🏦",
    layout="wide",
)


def format_currency(value: float | None) -> str:
    """
    Format numeric values as euros for display.
    """

    if value is None:
        return "N/A"

    return f"€{value:,.2f}"


def format_percentage(value: float | None) -> str:
    """
    Format numeric values as percentages for display.
    """

    if value is None:
        return "N/A"

    return f"{value:.2f}%"


def render_header() -> None:
    """
    Render the premium application header.
    """

    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-label">Wisestrike Finance Lab</div>
            <h1>DSTI Affordability Calculator</h1>
            <p>
                Banking-inspired financial affordability and DSTI simulation tool
                focused on financial literacy, data validation, explainability,
                interest rate sensitivity and risk awareness.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric_card(title: str, value: str, subtitle: str) -> None:
    """
    Render a styled metric card.
    """

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title: str, description: str) -> None:
    """
    Render a styled section heading.
    """

    st.markdown(
        f"""
        <div class="section-title">
            <h2>{title}</h2>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1320px;
        }

        .hero-section {
            background: linear-gradient(135deg, #0F3D5E 0%, #17324D 100%);
            padding: 2.4rem 2.2rem;
            border-radius: 24px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 12px 32px rgba(15, 61, 94, 0.18);
        }

        .hero-section h1 {
            font-size: 2.4rem;
            margin-bottom: 0.6rem;
            color: white;
        }

        .hero-section p {
            font-size: 1.05rem;
            max-width: 880px;
            line-height: 1.6;
            color: #E8F1F8;
        }

        .hero-label {
            display: inline-block;
            font-size: 0.82rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            background: rgba(255, 255, 255, 0.14);
            border: 1px solid rgba(255, 255, 255, 0.22);
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            margin-bottom: 0.9rem;
            color: #D8E8F4;
        }

        .disclaimer-box {
            background: #FFF8E8;
            border: 1px solid #F2D28A;
            border-left: 6px solid #C58A1A;
            padding: 1rem 1.2rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            color: #4B3A13;
            line-height: 1.55;
        }

        .section-title {
            margin-top: 1.8rem;
            margin-bottom: 0.9rem;
        }

        .section-title h2 {
            font-size: 1.35rem;
            margin-bottom: 0.25rem;
            color: #1B2430;
        }

        .section-title p {
            color: #5B6875;
            margin-bottom: 0;
        }

        .metric-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 20px;
            padding: 1.25rem 1.15rem;
            box-shadow: 0 8px 24px rgba(15, 61, 94, 0.07);
            min-height: 132px;
        }

        .metric-title {
            font-size: 0.82rem;
            color: #5B6875;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 0.55rem;
        }

        .metric-value {
            font-size: 1.75rem;
            font-weight: 700;
            color: #0F3D5E;
            margin-bottom: 0.35rem;
        }

        .metric-subtitle {
            font-size: 0.9rem;
            color: #64748B;
            line-height: 1.35;
        }

        .summary-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 20px;
            padding: 1.25rem 1.35rem;
            line-height: 1.65;
            color: #263442;
            margin-bottom: 1rem;
        }

        .info-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 20px;
            padding: 1.2rem 1.3rem;
            box-shadow: 0 8px 24px rgba(15, 61, 94, 0.06);
            margin-bottom: 1rem;
            line-height: 1.6;
            color: #263442;
        }

        .footer-note {
            margin-top: 2rem;
            background: #F3F6F9;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 1rem 1.2rem;
            color: #5B6875;
            font-size: 0.92rem;
            line-height: 1.55;
        }

        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            padding: 1rem;
            border-radius: 18px;
            box-shadow: 0 8px 20px rgba(15, 61, 94, 0.06);
        }

        section[data-testid="stSidebar"] {
            background-color: #F3F6F9;
        }

        .stDataFrame {
            border-radius: 16px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


render_header()

st.markdown(
    """
    <div class="disclaimer-box">
        <strong>Educational simulation only.</strong>
        This tool does not approve or reject credit, does not provide financial advice,
        does not replace formal banking analysis and does not represent any bank's
        internal credit policy. Use fictional, simulated or anonymised values only.
    </div>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.header("Simulation Inputs")

    st.caption(
        "Use fictional, simulated or anonymised values only. "
        "Do not enter real personal or sensitive financial data."
    )

    st.divider()

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

    st.divider()

    st.subheader("Loan and Interest Rate Assumptions")

    loan_amount = st.number_input(
        "Simulated loan amount (€)",
        min_value=1.0,
        value=180000.0,
        step=1000.0,
    )

    loan_maturity_years = st.number_input(
        "Simulated loan maturity in years",
        min_value=1.0,
        value=30.0,
        step=1.0,
    )

    simulated_euribor_percentage = st.number_input(
        "Simulated EURIBOR assumption (%)",
        value=3.00,
        step=0.05,
    )

    simulated_spread_percentage = st.number_input(
        "Simulated spread assumption (%)",
        min_value=0.0,
        value=0.90,
        step=0.05,
    )

    stress_buffer_percentage = st.number_input(
        "Interest rate stress buffer (%)",
        min_value=0.0,
        value=1.50,
        step=0.05,
    )

    use_calculated_instalments = st.checkbox(
        "Estimate instalments from EURIBOR + spread",
        value=True,
    )

    st.divider()

    st.subheader("Credit Commitments")

    existing_monthly_commitments = st.number_input(
        "Existing monthly credit commitments (€)",
        min_value=0.0,
        value=300.0,
        step=25.0,
    )

    configured_dsti_threshold_percentage = st.slider(
        "Configured DSTI threshold for simulation (%)",
        min_value=1.0,
        max_value=100.0,
        value=40.0,
        step=1.0,
    )

    if use_calculated_instalments:
        interest_rate_build = build_interest_rate_assumptions(
            simulated_euribor_percentage=simulated_euribor_percentage,
            simulated_spread_percentage=simulated_spread_percentage,
            stress_buffer_percentage=stress_buffer_percentage,
        )

        interest_rate_stress = run_interest_rate_stress_test(
            loan_amount=loan_amount,
            maturity_years=loan_maturity_years,
            base_annual_interest_rate_percentage=(
                interest_rate_build.base_annual_interest_rate_percentage
            ),
            stressed_annual_interest_rate_percentage=(
                interest_rate_build.stressed_annual_interest_rate_percentage
            ),
        )

        proposed_monthly_instalment = interest_rate_stress.base_monthly_payment
        stressed_monthly_instalment = interest_rate_stress.stressed_monthly_payment

        st.info(
            "Monthly instalments are being estimated from the simulated "
            "EURIBOR, spread, stress buffer, loan amount and maturity."
        )

        st.write(
            f"Base estimated instalment: "
            f"{format_currency(proposed_monthly_instalment)}"
        )
        st.write(
            f"Stressed estimated instalment: "
            f"{format_currency(stressed_monthly_instalment)}"
        )

    else:
        interest_rate_build = None
        interest_rate_stress = None

        proposed_monthly_instalment = st.number_input(
            "Manual proposed monthly instalment (€)",
            min_value=0.0,
            value=650.0,
            step=25.0,
        )

        stressed_monthly_instalment = st.number_input(
            "Manual stressed monthly instalment (€)",
            min_value=0.0,
            value=780.0,
            step=25.0,
        )

    st.divider()

    st.subheader("Optional LTV Inputs")

    include_ltv = st.checkbox("Include LTV simulation", value=True)

    if include_ltv:
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
        acquisition_value = None
        valuation_value = None
        configured_ltv_threshold_percentage = None
        use_lower_property_value = True

    st.divider()

    st.subheader("Optional Maturity Inputs")

    include_maturity = st.checkbox("Include maturity simulation", value=True)

    if include_maturity:
        current_age = st.number_input(
            "Fictional or anonymised current age",
            min_value=0.0,
            value=35.0,
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
    loan_amount=loan_amount if include_ltv else None,
    acquisition_value=acquisition_value,
    valuation_value=valuation_value,
    configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
    use_lower_property_value=use_lower_property_value,
    loan_maturity_years=loan_maturity_years if include_maturity else None,
    current_age=current_age,
    configured_maximum_age_at_end=configured_maximum_age_at_end,
)


render_section_title(
    "Simulation Summary",
    "Indicative educational output based on the configured fictional assumptions.",
)

st.markdown(
    f"""
    <div class="summary-card">
        {scenario.summary}
    </div>
    """,
    unsafe_allow_html=True,
)


if not scenario.validation.is_valid:
    st.error("Blocking validation errors were identified.")

    for error in scenario.validation.blocking_errors:
        st.write(f"- {error}")

else:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_metric_card(
            "Monthly Net Income",
            format_currency(scenario.income.monthly_net_income),
            "Selected income assumption used in this simulation.",
        )

    with col2:
        render_metric_card(
            "Base DSTI",
            format_percentage(scenario.dsti.base_dsti_percentage),
            "Debt service using the proposed instalment.",
        )

    with col3:
        render_metric_card(
            "Stressed DSTI",
            format_percentage(scenario.dsti.stressed_dsti_percentage),
            "Debt service using the stressed instalment.",
        )

    with col4:
        render_metric_card(
            "Remaining Capacity",
            format_currency(scenario.dsti.remaining_repayment_capacity),
            "Indicative margin before the configured DSTI threshold.",
        )

    if interest_rate_build is not None and interest_rate_stress is not None:
        render_section_title(
            "Interest Rate Assumptions",
            "Simulated EURIBOR, spread and stress buffer used to estimate instalments.",
        )

        rate_col1, rate_col2, rate_col3, rate_col4 = st.columns(4)

        with rate_col1:
            render_metric_card(
                "Simulated EURIBOR",
                format_percentage(interest_rate_build.simulated_euribor_percentage),
                "Manual educational EURIBOR assumption.",
            )

        with rate_col2:
            render_metric_card(
                "Simulated Spread",
                format_percentage(interest_rate_build.simulated_spread_percentage),
                "Manual educational spread assumption.",
            )

        with rate_col3:
            render_metric_card(
                "Base Annual Rate",
                format_percentage(
                    interest_rate_build.base_annual_interest_rate_percentage
                ),
                "EURIBOR plus spread.",
            )

        with rate_col4:
            render_metric_card(
                "Stressed Annual Rate",
                format_percentage(
                    interest_rate_build.stressed_annual_interest_rate_percentage
                ),
                "Base rate plus stress buffer.",
            )

        interest_rate_table = pd.DataFrame(
            [
                {
                    "Metric": "Simulated EURIBOR",
                    "Value": format_percentage(
                        interest_rate_build.simulated_euribor_percentage
                    ),
                },
                {
                    "Metric": "Simulated spread",
                    "Value": format_percentage(
                        interest_rate_build.simulated_spread_percentage
                    ),
                },
                {
                    "Metric": "Stress buffer",
                    "Value": format_percentage(
                        interest_rate_build.stress_buffer_percentage
                    ),
                },
                {
                    "Metric": "Base annual interest rate",
                    "Value": format_percentage(
                        interest_rate_build.base_annual_interest_rate_percentage
                    ),
                },
                {
                    "Metric": "Stressed annual interest rate",
                    "Value": format_percentage(
                        interest_rate_build.stressed_annual_interest_rate_percentage
                    ),
                },
                {
                    "Metric": "Base estimated monthly instalment",
                    "Value": format_currency(
                        interest_rate_stress.base_monthly_payment
                    ),
                },
                {
                    "Metric": "Stressed estimated monthly instalment",
                    "Value": format_currency(
                        interest_rate_stress.stressed_monthly_payment
                    ),
                },
                {
                    "Metric": "Monthly payment increase",
                    "Value": format_currency(
                        interest_rate_stress.monthly_payment_increase
                    ),
                },
                {
                    "Metric": "Monthly payment increase percentage",
                    "Value": format_percentage(
                        interest_rate_stress.monthly_payment_increase_percentage
                    ),
                },
                {
                    "Metric": "Total repayment increase",
                    "Value": format_currency(
                        interest_rate_stress.total_repayment_increase
                    ),
                },
            ]
        )

        st.dataframe(
            interest_rate_table,
            use_container_width=True,
            hide_index=True,
        )

        st.markdown(
            f"""
            <div class="info-card">
                {interest_rate_build.interpretation}
                <br><br>
                {interest_rate_stress.interpretation}
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_section_title(
        "DSTI Details",
        "Breakdown of base, stressed and capacity-related affordability indicators.",
    )

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

    st.dataframe(dsti_table, use_container_width=True, hide_index=True)

    if scenario.ltv is not None:
        render_section_title(
            "LTV Details",
            "Loan-to-Value simulation based on the selected property value assumption.",
        )

        ltv_col1, ltv_col2, ltv_col3 = st.columns(3)

        with ltv_col1:
            render_metric_card(
                "Loan Amount",
                format_currency(scenario.ltv.loan_amount),
                "Simulated loan amount.",
            )

        with ltv_col2:
            render_metric_card(
                "Property Value Used",
                format_currency(scenario.ltv.property_value_used),
                "Selected property value assumption.",
            )

        with ltv_col3:
            render_metric_card(
                "Simulated LTV",
                format_percentage(scenario.ltv.ltv_percentage),
                "Educational Loan-to-Value indicator.",
            )

    if scenario.maturity is not None:
        render_section_title(
            "Maturity Details",
            "Age and maturity assumptions used for risk awareness.",
        )

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

        st.dataframe(maturity_table, use_container_width=True, hide_index=True)

    render_section_title(
        "Validation Notes",
        "Financial data quality checks applied before interpreting the simulation.",
    )

    if scenario.validation.warnings:
        st.warning("Non-blocking validation warnings were identified.")

        for warning in scenario.validation.warnings:
            st.write(f"- {warning}")
    else:
        st.success("No non-blocking validation warnings were identified.")

    with st.expander("Information messages"):
        for message in scenario.validation.info_messages:
            st.write(f"- {message}")

    render_section_title(
        "Scenario Comparison",
        "Comparison between the base simulation and a prudent income scenario.",
    )

    prudent_scenario = run_affordability_scenario(
        scenario_name="Prudent income simulation",
        income_sources=income_sources,
        existing_monthly_commitments=existing_monthly_commitments,
        proposed_monthly_instalment=proposed_monthly_instalment,
        stressed_monthly_instalment=stressed_monthly_instalment,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
        use_conservative_income=True,
        conservative_factor=conservative_factor,
        loan_amount=loan_amount if include_ltv else None,
        acquisition_value=acquisition_value,
        valuation_value=valuation_value,
        configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
        use_lower_property_value=use_lower_property_value,
        loan_maturity_years=loan_maturity_years if include_maturity else None,
        current_age=current_age,
        configured_maximum_age_at_end=configured_maximum_age_at_end,
    )

    comparison_table = pd.DataFrame(
        compare_scenarios([scenario, prudent_scenario])
    )

    st.dataframe(comparison_table, use_container_width=True, hide_index=True)

    with st.expander("Methodology and limitations"):
        st.write(
            "This simulation uses simplified assumptions and does not verify "
            "income, credit history, employment stability, property valuation, "
            "legal documentation, regulatory requirements or bank-specific "
            "credit policy."
        )
        st.write(
            "EURIBOR, spread and stress buffer values are manually entered "
            "simulation assumptions. They are not live market data, bank pricing, "
            "loan offers or financial advice."
        )
        st.write(
            "The outputs are educational and indicative only. They must not be "
            "interpreted as credit approval, rejection, eligibility confirmation "
            "or financial advice."
        )

st.markdown(
    """
    <div class="footer-note">
        This project is educational and demonstrative. It does not use real client
        data, does not process personal documents, does not perform OCR and does
        not represent any bank's internal credit policy. EURIBOR, spread and stress
        values are simulated assumptions only. All values should be fictional,
        simulated or anonymised.
    </div>
    """,
    unsafe_allow_html=True,
)
