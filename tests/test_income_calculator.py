"""
Unit tests for income calculation logic.

These tests validate the core educational income handling functions used by the
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

from income_calculator import (
    calculate_annual_net_income,
    calculate_conservative_income,
    calculate_total_monthly_income,
    generate_income_interpretation,
    run_income_simulation,
    select_income_for_simulation,
)


def test_calculate_total_monthly_income_base_case():
    result = calculate_total_monthly_income(
        income_sources=[1500, 1000],
    )

    assert result == 2500


def test_calculate_total_monthly_income_raises_error_for_empty_list():
    with pytest.raises(ValueError):
        calculate_total_monthly_income(
            income_sources=[],
        )


def test_calculate_total_monthly_income_raises_error_for_negative_income():
    with pytest.raises(ValueError):
        calculate_total_monthly_income(
            income_sources=[1500, -1000],
        )


def test_calculate_annual_net_income_base_case():
    result = calculate_annual_net_income(
        monthly_net_income=2500,
    )

    assert result == 30000


def test_calculate_annual_net_income_raises_error_for_negative_income():
    with pytest.raises(ValueError):
        calculate_annual_net_income(
            monthly_net_income=-2500,
        )


def test_calculate_conservative_income_base_case():
    result = calculate_conservative_income(
        income_sources=[1500, 1000],
        conservative_factor=0.90,
    )

    assert result == 2250


def test_calculate_conservative_income_raises_error_for_invalid_factor_above_one():
    with pytest.raises(ValueError):
        calculate_conservative_income(
            income_sources=[1500, 1000],
            conservative_factor=1.20,
        )


def test_calculate_conservative_income_raises_error_for_invalid_factor_zero():
    with pytest.raises(ValueError):
        calculate_conservative_income(
            income_sources=[1500, 1000],
            conservative_factor=0,
        )


def test_select_income_for_simulation_uses_standard_income():
    result = select_income_for_simulation(
        income_sources=[1500, 1000],
        use_conservative_income=False,
        conservative_factor=0.90,
    )

    assert result == 2500


def test_select_income_for_simulation_uses_conservative_income():
    result = select_income_for_simulation(
        income_sources=[1500, 1000],
        use_conservative_income=True,
        conservative_factor=0.90,
    )

    assert result == 2250


def test_generate_income_interpretation_for_conservative_income():
    result = generate_income_interpretation(
        monthly_net_income=2250,
        conservative_monthly_income=2250,
        use_conservative_income=True,
    )

    assert "conservative income assumption" in result
    assert "educational only" in result


def test_generate_income_interpretation_for_zero_income():
    result = generate_income_interpretation(
        monthly_net_income=0,
        conservative_monthly_income=0,
        use_conservative_income=False,
    )

    assert "Risk awareness warning" in result
    assert "greater than zero" in result


def test_generate_income_interpretation_for_unusually_low_income():
    result = generate_income_interpretation(
        monthly_net_income=400,
        conservative_monthly_income=360,
        use_conservative_income=False,
    )

    assert "unusually low" in result


def test_generate_income_interpretation_for_unusually_high_income():
    result = generate_income_interpretation(
        monthly_net_income=60000,
        conservative_monthly_income=54000,
        use_conservative_income=False,
    )

    assert "unusually high" in result


def test_generate_income_interpretation_for_standard_income():
    result = generate_income_interpretation(
        monthly_net_income=2500,
        conservative_monthly_income=2250,
        use_conservative_income=False,
    )

    assert "educational affordability simulation" in result
    assert "does not represent verified income" in result


def test_run_income_simulation_standard_income():
    result = run_income_simulation(
        income_sources=[1500, 1000],
        use_conservative_income=False,
        conservative_factor=0.90,
    )

    assert result.monthly_net_income == 2500
    assert result.annual_net_income == 30000
    assert result.income_source_count == 2
    assert result.conservative_monthly_income == 2250
    assert "educational affordability simulation" in result.interpretation


def test_run_income_simulation_conservative_income():
    result = run_income_simulation(
        income_sources=[1500, 1000],
        use_conservative_income=True,
        conservative_factor=0.90,
    )

    assert result.monthly_net_income == 2250
    assert result.annual_net_income == 27000
    assert result.income_source_count == 2
    assert result.conservative_monthly_income == 2250
    assert "conservative income assumption" in result.interpretation
