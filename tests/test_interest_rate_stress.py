"""
Unit tests for interest rate stress testing logic.

These tests validate the simplified educational interest rate stress functions
used by the DSTI Affordability Calculator.

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

from interest_rate_stress import (
    calculate_payment_increase,
    calculate_payment_increase_percentage,
    generate_interest_rate_stress_interpretation,
    run_interest_rate_stress_test,
)


def test_calculate_payment_increase_base_case():
    result = calculate_payment_increase(
        base_monthly_payment=859.35,
        stressed_monthly_payment=1022.02,
    )

    assert round(result, 2) == 162.67


def test_calculate_payment_increase_allows_negative_difference():
    result = calculate_payment_increase(
        base_monthly_payment=900,
        stressed_monthly_payment=850,
    )

    assert result == -50


def test_calculate_payment_increase_raises_error_for_negative_base_payment():
    with pytest.raises(ValueError):
        calculate_payment_increase(
            base_monthly_payment=-1,
            stressed_monthly_payment=850,
        )


def test_calculate_payment_increase_raises_error_for_negative_stressed_payment():
    with pytest.raises(ValueError):
        calculate_payment_increase(
            base_monthly_payment=850,
            stressed_monthly_payment=-1,
        )


def test_calculate_payment_increase_percentage_base_case():
    result = calculate_payment_increase_percentage(
        base_monthly_payment=859.35,
        monthly_payment_increase=162.67,
    )

    assert round(result, 2) == 18.93


def test_calculate_payment_increase_percentage_negative_increase():
    result = calculate_payment_increase_percentage(
        base_monthly_payment=900,
        monthly_payment_increase=-50,
    )

    assert round(result, 2) == -5.56


def test_calculate_payment_increase_percentage_raises_error_for_zero_base_payment():
    with pytest.raises(ValueError):
        calculate_payment_increase_percentage(
            base_monthly_payment=0,
            monthly_payment_increase=100,
        )


def test_generate_interpretation_when_stressed_rate_is_lower_than_base_rate():
    result = generate_interest_rate_stress_interpretation(
        monthly_payment_increase=-50,
        monthly_payment_increase_percentage=-5.0,
        base_annual_interest_rate_percentage=5.0,
        stressed_annual_interest_rate_percentage=4.0,
    )

    assert "Data quality warning" in result
    assert "stressed interest rate is lower than the base interest rate" in result


def test_generate_interpretation_when_payment_does_not_increase():
    result = generate_interest_rate_stress_interpretation(
        monthly_payment_increase=0,
        monthly_payment_increase_percentage=0,
        base_annual_interest_rate_percentage=4.0,
        stressed_annual_interest_rate_percentage=4.0,
    )

    assert "does not increase the estimated monthly payment" in result
    assert "assumptions are coherent" in result


def test_generate_interpretation_for_material_increase():
    result = generate_interest_rate_stress_interpretation(
        monthly_payment_increase=250,
        monthly_payment_increase_percentage=25.0,
        base_annual_interest_rate_percentage=4.0,
        stressed_annual_interest_rate_percentage=6.5,
    )

    assert "Risk awareness warning" in result
    assert "material increase" in result


def test_generate_interpretation_for_standard_increase():
    result = generate_interest_rate_stress_interpretation(
        monthly_payment_increase=162.67,
        monthly_payment_increase_percentage=18.93,
        base_annual_interest_rate_percentage=4.0,
        stressed_annual_interest_rate_percentage=5.5,
    )

    assert "increases the estimated monthly payment" in result
    assert "educational only" in result


def test_run_interest_rate_stress_test_returns_expected_result():
    result = run_interest_rate_stress_test(
        loan_amount=180000,
        maturity_years=30,
        base_annual_interest_rate_percentage=4.0,
        stressed_annual_interest_rate_percentage=5.5,
    )

    assert result.loan_amount == 180000
    assert result.maturity_years == 30
    assert result.base_annual_interest_rate_percentage == 4.0
    assert result.stressed_annual_interest_rate_percentage == 5.5
    assert result.base_monthly_payment == 859.35
    assert result.stressed_monthly_payment == 1022.02
    assert result.monthly_payment_increase == 162.67
    assert result.monthly_payment_increase_percentage == 18.93
    assert result.base_total_repayment == 309366.44
    assert result.stressed_total_repayment == 367928.06
    assert result.total_repayment_increase == 58561.62
    assert "increases the estimated monthly payment" in result.interpretation
