"""
Unit tests for the DSTI calculation logic.

These tests validate the core educational calculation functions used by the
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

from dsti_calculator import (
    calculate_dsti,
    calculate_margin_against_stressed_instalment,
    calculate_maximum_monthly_debt_service,
    calculate_remaining_repayment_capacity,
    generate_dsti_interpretation,
    run_dsti_simulation,
)


def test_calculate_dsti_base_case():
    result = calculate_dsti(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        monthly_instalment=650,
    )

    assert round(result, 2) == 38.00


def test_calculate_dsti_stressed_case():
    result = calculate_dsti(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        monthly_instalment=780,
    )

    assert round(result, 2) == 43.20


def test_calculate_dsti_raises_error_for_zero_income():
    with pytest.raises(ValueError):
        calculate_dsti(
            monthly_net_income=0,
            existing_monthly_commitments=300,
            monthly_instalment=650,
        )


def test_calculate_dsti_raises_error_for_negative_commitments():
    with pytest.raises(ValueError):
        calculate_dsti(
            monthly_net_income=2500,
            existing_monthly_commitments=-300,
            monthly_instalment=650,
        )


def test_calculate_dsti_raises_error_for_negative_instalment():
    with pytest.raises(ValueError):
        calculate_dsti(
            monthly_net_income=2500,
            existing_monthly_commitments=300,
            monthly_instalment=-650,
        )


def test_calculate_maximum_monthly_debt_service():
    result = calculate_maximum_monthly_debt_service(
        monthly_net_income=2500,
        configured_dsti_threshold_percentage=40,
    )

    assert round(result, 2) == 1000.00


def test_calculate_maximum_monthly_debt_service_raises_error_for_invalid_threshold():
    with pytest.raises(ValueError):
        calculate_maximum_monthly_debt_service(
            monthly_net_income=2500,
            configured_dsti_threshold_percentage=120,
        )


def test_calculate_remaining_repayment_capacity():
    result = calculate_remaining_repayment_capacity(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        configured_dsti_threshold_percentage=40,
    )

    assert round(result, 2) == 700.00


def test_calculate_margin_against_stressed_instalment_positive_margin():
    result = calculate_margin_against_stressed_instalment(
        remaining_repayment_capacity=900,
        stressed_monthly_instalment=780,
    )

    assert round(result, 2) == 120.00


def test_calculate_margin_against_stressed_instalment_negative_margin():
    result = calculate_margin_against_stressed_instalment(
        remaining_repayment_capacity=700,
        stressed_monthly_instalment=780,
    )

    assert round(result, 2) == -80.00


def test_generate_dsti_interpretation_when_stressed_dsti_exceeds_threshold():
    result = generate_dsti_interpretation(
        base_dsti_percentage=38,
        stressed_dsti_percentage=43.2,
        configured_dsti_threshold_percentage=40,
        margin_against_stressed_instalment=-80,
    )

    assert "Risk awareness warning" in result
    assert "does not represent credit rejection" in result


def test_generate_dsti_interpretation_when_scenario_is_more_favourable():
    result = generate_dsti_interpretation(
        base_dsti_percentage=30,
        stressed_dsti_percentage=35,
        configured_dsti_threshold_percentage=40,
        margin_against_stressed_instalment=100,
    )

    assert "more favourable affordability position" in result
    assert "must not be interpreted as credit approval" in result


def test_run_dsti_simulation_returns_expected_result():
    result = run_dsti_simulation(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
    )

    assert result.base_dsti_percentage == 38.00
    assert result.stressed_dsti_percentage == 43.20
    assert result.maximum_monthly_debt_service == 1000.00
    assert result.remaining_repayment_capacity == 700.00
    assert result.margin_against_stressed_instalment == -80.00
    assert "Risk awareness warning" in result.interpretation
