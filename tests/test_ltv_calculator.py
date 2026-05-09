"""
Unit tests for Loan-to-Value calculation logic.

These tests validate the core educational LTV simulation functions used by the
DSTI Affordability Calculator.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
financial advisory tool or replacement for formal human credit analysis.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from ltv_calculator import (
    calculate_ltv,
    generate_ltv_interpretation,
    run_ltv_simulation,
    select_property_value,
)


def test_select_property_value_uses_lower_value_when_enabled():
    result = select_property_value(
        acquisition_value=220000,
        valuation_value=215000,
        use_lower_value=True,
    )

    assert result == 215000


def test_select_property_value_uses_valuation_when_lower_value_disabled():
    result = select_property_value(
        acquisition_value=220000,
        valuation_value=215000,
        use_lower_value=False,
    )

    assert result == 215000


def test_select_property_value_uses_single_acquisition_value():
    result = select_property_value(
        acquisition_value=220000,
        valuation_value=None,
        use_lower_value=True,
    )

    assert result == 220000


def test_select_property_value_uses_single_valuation_value():
    result = select_property_value(
        acquisition_value=None,
        valuation_value=215000,
        use_lower_value=True,
    )

    assert result == 215000


def test_select_property_value_raises_error_when_no_value_is_provided():
    with pytest.raises(ValueError):
        select_property_value(
            acquisition_value=None,
            valuation_value=None,
            use_lower_value=True,
        )


def test_select_property_value_raises_error_for_invalid_acquisition_value():
    with pytest.raises(ValueError):
        select_property_value(
            acquisition_value=0,
            valuation_value=215000,
            use_lower_value=True,
        )


def test_select_property_value_raises_error_for_invalid_valuation_value():
    with pytest.raises(ValueError):
        select_property_value(
            acquisition_value=220000,
            valuation_value=0,
            use_lower_value=True,
        )


def test_calculate_ltv_base_case():
    result = calculate_ltv(
        loan_amount=180000,
        property_value=215000,
    )

    assert round(result, 2) == 83.72


def test_calculate_ltv_raises_error_for_zero_loan_amount():
    with pytest.raises(ValueError):
        calculate_ltv(
            loan_amount=0,
            property_value=215000,
        )


def test_calculate_ltv_raises_error_for_zero_property_value():
    with pytest.raises(ValueError):
        calculate_ltv(
            loan_amount=180000,
            property_value=0,
        )


def test_generate_ltv_interpretation_when_ltv_exceeds_configured_threshold():
    result = generate_ltv_interpretation(
        ltv_percentage=95,
        configured_ltv_threshold_percentage=90,
    )

    assert "Risk awareness warning" in result
    assert "does not represent credit rejection" in result


def test_generate_ltv_interpretation_when_ltv_is_above_100():
    result = generate_ltv_interpretation(
        ltv_percentage=105,
        configured_ltv_threshold_percentage=None,
    )

    assert "Risk awareness warning" in result
    assert "not a lending decision" in result


def test_generate_ltv_interpretation_when_ltv_is_more_balanced():
    result = generate_ltv_interpretation(
        ltv_percentage=83.72,
        configured_ltv_threshold_percentage=90,
    )

    assert "more balanced" in result
    assert "must not be interpreted as credit approval" in result


def test_generate_ltv_interpretation_raises_error_for_invalid_threshold():
    with pytest.raises(ValueError):
        generate_ltv_interpretation(
            ltv_percentage=83.72,
            configured_ltv_threshold_percentage=120,
        )


def test_run_ltv_simulation_returns_expected_result():
    result = run_ltv_simulation(
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        use_lower_value=True,
    )

    assert result.loan_amount == 180000
    assert result.property_value_used == 215000
    assert result.ltv_percentage == 83.72
    assert "more balanced" in result.interpretation
