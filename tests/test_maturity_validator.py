"""
Unit tests for maturity and age scenario validation.

These tests validate the core educational maturity simulation functions used by
the DSTI Affordability Calculator.

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

from maturity_validator import (
    calculate_age_at_end_of_loan,
    generate_maturity_interpretation,
    run_maturity_simulation,
    validate_age_range,
    validate_maturity_range,
)


def test_calculate_age_at_end_of_loan_base_case():
    result = calculate_age_at_end_of_loan(
        current_age=35,
        loan_maturity_years=30,
    )

    assert result == 65


def test_calculate_age_at_end_of_loan_raises_error_for_zero_age():
    with pytest.raises(ValueError):
        calculate_age_at_end_of_loan(
            current_age=0,
            loan_maturity_years=30,
        )


def test_calculate_age_at_end_of_loan_raises_error_for_zero_maturity():
    with pytest.raises(ValueError):
        calculate_age_at_end_of_loan(
            current_age=35,
            loan_maturity_years=0,
        )


def test_validate_age_range_warns_for_age_below_expected_range():
    warnings = validate_age_range(current_age=17)

    assert any(
        "below the expected range" in warning
        for warning in warnings
    )


def test_validate_age_range_warns_for_unusually_high_age():
    warnings = validate_age_range(current_age=105)

    assert any(
        "unusually high" in warning
        for warning in warnings
    )


def test_validate_age_range_no_warning_for_standard_age():
    warnings = validate_age_range(current_age=35)

    assert warnings == []


def test_validate_maturity_range_warns_for_long_maturity():
    warnings = validate_maturity_range(loan_maturity_years=55)

    assert any(
        "unusually long" in warning
        for warning in warnings
    )


def test_validate_maturity_range_no_warning_for_standard_maturity():
    warnings = validate_maturity_range(loan_maturity_years=30)

    assert warnings == []


def test_generate_maturity_interpretation_when_age_exceeds_configured_assumption():
    result = generate_maturity_interpretation(
        age_at_end_of_loan=85,
        configured_maximum_age_at_end=75,
        warnings=[],
    )

    assert "Risk awareness warning" in result
    assert "not an eligibility decision" in result


def test_generate_maturity_interpretation_when_age_is_high():
    result = generate_maturity_interpretation(
        age_at_end_of_loan=78,
        configured_maximum_age_at_end=85,
        warnings=[],
    )

    assert "Risk awareness warning" in result
    assert "educational flag" in result


def test_generate_maturity_interpretation_when_scenario_is_balanced():
    result = generate_maturity_interpretation(
        age_at_end_of_loan=65,
        configured_maximum_age_at_end=75,
        warnings=[],
    )

    assert "more balanced" in result
    assert "must not be interpreted as credit approval" in result


def test_generate_maturity_interpretation_raises_error_for_invalid_configured_age():
    with pytest.raises(ValueError):
        generate_maturity_interpretation(
            age_at_end_of_loan=65,
            configured_maximum_age_at_end=0,
            warnings=[],
        )


def test_run_maturity_simulation_returns_expected_result():
    result = run_maturity_simulation(
        current_age=35,
        loan_maturity_years=30,
        configured_maximum_age_at_end=75,
    )

    assert result.current_age == 35
    assert result.loan_maturity_years == 30
    assert result.age_at_end_of_loan == 65
    assert result.is_within_configured_assumption is True
    assert "more balanced" in result.interpretation


def test_run_maturity_simulation_flags_high_age_at_end():
    result = run_maturity_simulation(
        current_age=55,
        loan_maturity_years=30,
        configured_maximum_age_at_end=75,
    )

    assert result.age_at_end_of_loan == 85
    assert result.is_within_configured_assumption is False
    assert "Risk awareness warning" in result.interpretation
