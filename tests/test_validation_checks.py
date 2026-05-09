"""
Unit tests for input validation logic.

These tests validate the core Financial Data Quality checks used by the
DSTI Affordability Calculator.

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

from validation_checks import (
    is_missing,
    validate_affordability_inputs,
    validate_dsti_outputs,
    validate_percentage,
    validate_required_number,
)


def test_is_missing_detects_none():
    assert is_missing(None) is True


def test_is_missing_detects_empty_string():
    assert is_missing("") is True


def test_is_missing_returns_false_for_zero():
    assert is_missing(0) is False


def test_validate_required_number_accepts_valid_number():
    errors = validate_required_number(
        value=2500,
        field_name="Monthly net income",
        allow_zero=False,
    )

    assert errors == []


def test_validate_required_number_rejects_missing_value():
    errors = validate_required_number(
        value=None,
        field_name="Monthly net income",
        allow_zero=False,
    )

    assert "Monthly net income is required." in errors


def test_validate_required_number_rejects_negative_value():
    errors = validate_required_number(
        value=-2500,
        field_name="Monthly net income",
        allow_zero=False,
    )

    assert "Monthly net income cannot be negative." in errors


def test_validate_required_number_rejects_zero_when_not_allowed():
    errors = validate_required_number(
        value=0,
        field_name="Monthly net income",
        allow_zero=False,
    )

    assert "Monthly net income must be greater than zero." in errors


def test_validate_percentage_accepts_valid_percentage():
    errors = validate_percentage(
        value=40,
        field_name="Configured DSTI threshold",
        minimum=0,
        maximum=100,
    )

    assert errors == []


def test_validate_percentage_rejects_invalid_percentage():
    errors = validate_percentage(
        value=120,
        field_name="Configured DSTI threshold",
        minimum=0,
        maximum=100,
    )

    assert "Configured DSTI threshold must be between 0% and 100%." in errors


def test_validate_affordability_inputs_valid_scenario():
    result = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        loan_amount=180000,
        property_value=215000,
        loan_maturity_years=30,
        current_age=35,
    )

    assert result.is_valid is True
    assert result.blocking_errors == []


def test_validate_affordability_inputs_rejects_zero_income():
    result = validate_affordability_inputs(
        monthly_net_income=0,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
    )

    assert result.is_valid is False
    assert "Monthly net income must be greater than zero." in result.blocking_errors


def test_validate_affordability_inputs_warns_when_stressed_instalment_is_lower():
    result = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=600,
        configured_dsti_threshold_percentage=40,
    )

    assert result.is_valid is True
    assert any(
        "stressed instalment is lower than the proposed instalment" in warning
        for warning in result.warnings
    )


def test_validate_affordability_inputs_warns_for_high_commitments():
    result = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=2000,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
    )

    assert result.is_valid is True
    assert any(
        "Existing monthly commitments appear high" in warning
        or "Existing monthly commitments are higher" in warning
        for warning in result.warnings
    )


def test_validate_affordability_inputs_rejects_invalid_ltv_inputs():
    result = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        loan_amount=180000,
        property_value=0,
    )

    assert result.is_valid is False
    assert "Property value must be greater than zero." in result.blocking_errors


def test_validate_affordability_inputs_warns_for_high_age_at_end_of_loan():
    result = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        loan_maturity_years=30,
        current_age=55,
    )

    assert result.is_valid is True
    assert any(
        "age at the end of the loan appears high" in warning
        for warning in result.warnings
    )


def test_validate_dsti_outputs_warns_for_high_base_dsti():
    warnings = validate_dsti_outputs(
        base_dsti_percentage=55,
        stressed_dsti_percentage=58,
    )

    assert any("Base DSTI appears high" in warning for warning in warnings)


def test_validate_dsti_outputs_warns_for_high_stressed_dsti():
    warnings = validate_dsti_outputs(
        base_dsti_percentage=38,
        stressed_dsti_percentage=65,
    )

    assert any("Stressed DSTI appears high" in warning for warning in warnings)
