"""
Unit tests for interest rate builder logic.

These tests validate the simulated EURIBOR + spread + stress buffer logic used
by the DSTI Affordability Calculator.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
bank pricing model, financial advisory tool or replacement for formal human
credit analysis.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from interest_rate_builder import (
    build_interest_rate_assumptions,
    calculate_base_annual_interest_rate,
    calculate_stressed_annual_interest_rate,
    generate_interest_rate_build_interpretation,
)


def test_calculate_base_annual_interest_rate_base_case():
    result = calculate_base_annual_interest_rate(
        simulated_euribor_percentage=3.0,
        simulated_spread_percentage=0.9,
    )

    assert result == 3.9


def test_calculate_base_annual_interest_rate_allows_negative_euribor():
    result = calculate_base_annual_interest_rate(
        simulated_euribor_percentage=-0.5,
        simulated_spread_percentage=1.0,
    )

    assert result == 0.5


def test_calculate_base_annual_interest_rate_raises_error_for_negative_spread():
    with pytest.raises(ValueError):
        calculate_base_annual_interest_rate(
            simulated_euribor_percentage=3.0,
            simulated_spread_percentage=-0.1,
        )


def test_calculate_stressed_annual_interest_rate_base_case():
    result = calculate_stressed_annual_interest_rate(
        base_annual_interest_rate_percentage=3.9,
        stress_buffer_percentage=1.5,
    )

    assert result == 5.4


def test_calculate_stressed_annual_interest_rate_with_zero_buffer():
    result = calculate_stressed_annual_interest_rate(
        base_annual_interest_rate_percentage=3.9,
        stress_buffer_percentage=0.0,
    )

    assert result == 3.9


def test_calculate_stressed_annual_interest_rate_raises_error_for_negative_buffer():
    with pytest.raises(ValueError):
        calculate_stressed_annual_interest_rate(
            base_annual_interest_rate_percentage=3.9,
            stress_buffer_percentage=-1.0,
        )


def test_generate_interpretation_for_negative_euribor():
    result = generate_interest_rate_build_interpretation(
        simulated_euribor_percentage=-0.5,
        simulated_spread_percentage=1.0,
        stress_buffer_percentage=1.5,
        base_annual_interest_rate_percentage=0.5,
        stressed_annual_interest_rate_percentage=2.0,
    )

    assert "Data quality note" in result
    assert "simulated EURIBOR assumption is negative" in result


def test_generate_interpretation_for_high_base_rate():
    result = generate_interest_rate_build_interpretation(
        simulated_euribor_percentage=9.5,
        simulated_spread_percentage=1.5,
        stress_buffer_percentage=1.5,
        base_annual_interest_rate_percentage=11.0,
        stressed_annual_interest_rate_percentage=12.5,
    )

    assert "Risk awareness warning" in result
    assert "base annual interest rate appears high" in result


def test_generate_interpretation_for_zero_stress_buffer():
    result = generate_interest_rate_build_interpretation(
        simulated_euribor_percentage=3.0,
        simulated_spread_percentage=0.9,
        stress_buffer_percentage=0.0,
        base_annual_interest_rate_percentage=3.9,
        stressed_annual_interest_rate_percentage=3.9,
    )

    assert "no stress buffer was applied" in result
    assert "separate stressed scenario" in result


def test_generate_interpretation_for_standard_case():
    result = generate_interest_rate_build_interpretation(
        simulated_euribor_percentage=3.0,
        simulated_spread_percentage=0.9,
        stress_buffer_percentage=1.5,
        base_annual_interest_rate_percentage=3.9,
        stressed_annual_interest_rate_percentage=5.4,
    )

    assert "simulated EURIBOR and simulated spread" in result
    assert "educational only" in result


def test_build_interest_rate_assumptions_returns_expected_result():
    result = build_interest_rate_assumptions(
        simulated_euribor_percentage=3.0,
        simulated_spread_percentage=0.9,
        stress_buffer_percentage=1.5,
    )

    assert result.simulated_euribor_percentage == 3.0
    assert result.simulated_spread_percentage == 0.9
    assert result.stress_buffer_percentage == 1.5
    assert result.base_annual_interest_rate_percentage == 3.9
    assert result.stressed_annual_interest_rate_percentage == 5.4
    assert "simulated EURIBOR and simulated spread" in result.interpretation
