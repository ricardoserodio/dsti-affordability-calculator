"""
Unit tests for loan payment calculation logic.

These tests validate the simplified educational loan payment functions used by
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

from loan_payment_calculator import (
    calculate_monthly_payment,
    calculate_total_interest,
    calculate_total_repayment,
    generate_loan_payment_interpretation,
    run_loan_payment_simulation,
)


def test_calculate_monthly_payment_base_case():
    result = calculate_monthly_payment(
        loan_amount=180000,
        annual_interest_rate_percentage=4.0,
        maturity_years=30,
    )

    assert round(result, 2) == 859.35


def test_calculate_monthly_payment_zero_interest_rate():
    result = calculate_monthly_payment(
        loan_amount=120000,
        annual_interest_rate_percentage=0.0,
        maturity_years=30,
    )

    assert round(result, 2) == 333.33


def test_calculate_monthly_payment_raises_error_for_zero_loan_amount():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            loan_amount=0,
            annual_interest_rate_percentage=4.0,
            maturity_years=30,
        )


def test_calculate_monthly_payment_raises_error_for_zero_maturity():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            loan_amount=180000,
            annual_interest_rate_percentage=4.0,
            maturity_years=0,
        )


def test_calculate_monthly_payment_raises_error_for_negative_interest_rate():
    with pytest.raises(ValueError):
        calculate_monthly_payment(
            loan_amount=180000,
            annual_interest_rate_percentage=-1.0,
            maturity_years=30,
        )


def test_calculate_total_repayment_base_case():
    result = calculate_total_repayment(
        monthly_payment=859.35,
        maturity_years=30,
    )

    assert round(result, 2) == 309366.00


def test_calculate_total_repayment_raises_error_for_negative_payment():
    with pytest.raises(ValueError):
        calculate_total_repayment(
            monthly_payment=-859.35,
            maturity_years=30,
        )


def test_calculate_total_repayment_raises_error_for_zero_maturity():
    with pytest.raises(ValueError):
        calculate_total_repayment(
            monthly_payment=859.35,
            maturity_years=0,
        )


def test_calculate_total_interest_base_case():
    result = calculate_total_interest(
        total_repayment=309366,
        loan_amount=180000,
    )

    assert round(result, 2) == 129366.00


def test_calculate_total_interest_raises_error_for_negative_total_repayment():
    with pytest.raises(ValueError):
        calculate_total_interest(
            total_repayment=-309366,
            loan_amount=180000,
        )


def test_calculate_total_interest_raises_error_for_zero_loan_amount():
    with pytest.raises(ValueError):
        calculate_total_interest(
            total_repayment=309366,
            loan_amount=0,
        )


def test_generate_loan_payment_interpretation_for_high_interest_rate():
    result = generate_loan_payment_interpretation(
        estimated_monthly_payment=1200,
        annual_interest_rate_percentage=11.0,
        maturity_years=30,
    )

    assert "Risk awareness warning" in result
    assert "annual interest rate assumption appears high" in result


def test_generate_loan_payment_interpretation_for_long_maturity():
    result = generate_loan_payment_interpretation(
        estimated_monthly_payment=650,
        annual_interest_rate_percentage=4.0,
        maturity_years=45,
    )

    assert "Risk awareness warning" in result
    assert "maturity assumption appears long" in result


def test_generate_loan_payment_interpretation_for_standard_case():
    result = generate_loan_payment_interpretation(
        estimated_monthly_payment=859.35,
        annual_interest_rate_percentage=4.0,
        maturity_years=30,
    )

    assert "educational estimate only" in result
    assert "must not be interpreted as a bank quote" in result


def test_run_loan_payment_simulation_returns_expected_result():
    result = run_loan_payment_simulation(
        loan_amount=180000,
        annual_interest_rate_percentage=4.0,
        maturity_years=30,
    )

    assert result.loan_amount == 180000
    assert result.annual_interest_rate_percentage == 4.0
    assert result.maturity_years == 30
    assert result.maturity_months == 360
    assert result.estimated_monthly_payment == 859.35
    assert result.total_repayment == 309365.11
    assert result.total_interest == 129365.11
    assert "educational estimate only" in result.interpretation
