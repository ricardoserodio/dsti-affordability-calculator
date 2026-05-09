"""
Unit tests for scenario analysis engine.

These tests validate how the DSTI Affordability Calculator combines income,
DSTI, LTV, maturity and validation logic into complete simulated scenarios.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
financial advisory tool or replacement for formal human credit analysis.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from scenario_engine import (
    compare_scenarios,
    generate_scenario_summary,
    run_affordability_scenario,
)
from validation_checks import ValidationResult


def test_run_affordability_scenario_base_case():
    result = run_affordability_scenario(
        scenario_name="Base simulation",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    assert result.scenario_name == "Base simulation"
    assert result.validation.is_valid is True
    assert result.income.monthly_net_income == 2500
    assert result.dsti.base_dsti_percentage == 38.00
    assert result.dsti.stressed_dsti_percentage == 43.20
    assert result.ltv.ltv_percentage == 83.72
    assert result.maturity.age_at_end_of_loan == 65
    assert "educational" in result.summary.lower()


def test_run_affordability_scenario_with_conservative_income():
    result = run_affordability_scenario(
        scenario_name="Prudent income simulation",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=True,
        conservative_factor=0.90,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    assert result.scenario_name == "Prudent income simulation"
    assert result.validation.is_valid is True
    assert result.income.monthly_net_income == 2250
    assert result.dsti.base_dsti_percentage == 42.22
    assert result.dsti.stressed_dsti_percentage == 48.00
    assert "Risk awareness warning" in result.dsti.interpretation


def test_run_affordability_scenario_without_ltv_or_maturity():
    result = run_affordability_scenario(
        scenario_name="DSTI only simulation",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
        loan_amount=None,
        acquisition_value=None,
        valuation_value=None,
        loan_maturity_years=None,
        current_age=None,
    )

    assert result.validation.is_valid is True
    assert result.dsti is not None
    assert result.ltv is None
    assert result.maturity is None
    assert result.dsti.base_dsti_percentage == 38.00


def test_run_affordability_scenario_with_blocking_validation_error():
    result = run_affordability_scenario(
        scenario_name="Invalid income simulation",
        income_sources=[0],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
    )

    assert result.validation.is_valid is False
    assert result.dsti is None
    assert result.ltv is None
    assert result.maturity is None
    assert "blocking validation issues" in result.summary


def test_generate_scenario_summary_for_invalid_validation():
    validation = ValidationResult(
        is_valid=False,
        blocking_errors=["Monthly net income must be greater than zero."],
        warnings=[],
        info_messages=[],
    )

    summary = generate_scenario_summary(
        scenario_name="Invalid scenario",
        validation=validation,
    )

    assert "blocking validation issues" in summary
    assert "not a credit decision" in summary


def test_compare_scenarios_returns_expected_structure():
    base_scenario = run_affordability_scenario(
        scenario_name="Base simulation",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    prudent_scenario = run_affordability_scenario(
        scenario_name="Prudent income simulation",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=True,
        conservative_factor=0.90,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    comparison = compare_scenarios([base_scenario, prudent_scenario])

    assert len(comparison) == 2
    assert comparison[0]["scenario_name"] == "Base simulation"
    assert comparison[0]["validation_status"] == "valid"
    assert comparison[0]["base_dsti_percentage"] == 38.00
    assert comparison[0]["stressed_dsti_percentage"] == 43.20
    assert comparison[0]["ltv_percentage"] == 83.72
    assert comparison[0]["age_at_end_of_loan"] == 65

    assert comparison[1]["scenario_name"] == "Prudent income simulation"
    assert comparison[1]["validation_status"] == "valid"
    assert comparison[1]["base_dsti_percentage"] == 42.22
    assert comparison[1]["stressed_dsti_percentage"] == 48.00


def test_compare_scenarios_handles_invalid_scenario():
    invalid_scenario = run_affordability_scenario(
        scenario_name="Invalid income simulation",
        income_sources=[0],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
    )

    comparison = compare_scenarios([invalid_scenario])

    assert len(comparison) == 1
    assert comparison[0]["scenario_name"] == "Invalid income simulation"
    assert comparison[0]["validation_status"] == "invalid"
    assert comparison[0]["base_dsti_percentage"] is None
    assert comparison[0]["stressed_dsti_percentage"] is None
    assert comparison[0]["ltv_percentage"] is None
    assert comparison[0]["age_at_end_of_loan"] is None
