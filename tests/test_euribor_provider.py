"""
Unit tests for the manual EURIBOR reference provider.

These tests validate the simulated manual EURIBOR reference logic used by the
DSTI Affordability Calculator.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a live benchmark data provider, credit approval
system, bank pricing model, financial advisory tool or replacement for formal
human credit analysis.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from euribor_provider import (
    ALLOWED_EURIBOR_TENORS,
    build_manual_euribor_reference,
    generate_euribor_reference_interpretation,
    normalise_euribor_tenor,
    validate_euribor_percentage,
)


def test_allowed_euribor_tenors():
    assert ALLOWED_EURIBOR_TENORS == {"1M", "3M", "6M", "12M"}


def test_normalise_euribor_tenor_base_case():
    result = normalise_euribor_tenor("6M")

    assert result == "6M"


def test_normalise_euribor_tenor_lowercase_and_spaces():
    result = normalise_euribor_tenor(" 12m ")

    assert result == "12M"


def test_normalise_euribor_tenor_raises_error_for_missing_value():
    with pytest.raises(ValueError):
        normalise_euribor_tenor("")


def test_normalise_euribor_tenor_raises_error_for_unsupported_value():
    with pytest.raises(ValueError):
        normalise_euribor_tenor("2Y")


def test_validate_euribor_percentage_base_case():
    result = validate_euribor_percentage(3.0)

    assert result == 3.0


def test_validate_euribor_percentage_allows_negative_value():
    result = validate_euribor_percentage(-0.5)

    assert result == -0.5


def test_validate_euribor_percentage_raises_error_for_missing_value():
    with pytest.raises(ValueError):
        validate_euribor_percentage(None)


def test_validate_euribor_percentage_raises_error_for_unrealistically_high_value():
    with pytest.raises(ValueError):
        validate_euribor_percentage(26.0)


def test_generate_interpretation_for_negative_euribor():
    result = generate_euribor_reference_interpretation(
        tenor="6M",
        euribor_percentage=-0.5,
        source_label="Manual simulated input",
        reference_date=None,
    )

    assert "simulated EURIBOR 6M assumption is negative" in result
    assert "manual educational assumption" in result


def test_generate_interpretation_for_high_euribor():
    result = generate_euribor_reference_interpretation(
        tenor="6M",
        euribor_percentage=11.0,
        source_label="Manual simulated input",
        reference_date=None,
    )

    assert "Risk awareness warning" in result
    assert "appears high" in result


def test_generate_interpretation_with_reference_date():
    result = generate_euribor_reference_interpretation(
        tenor="6M",
        euribor_percentage=3.0,
        source_label="Manual simulated input",
        reference_date="2026-01-01",
    )

    assert "source 'Manual simulated input'" in result
    assert "reference date 2026-01-01" in result
    assert "not live market data" in result


def test_generate_interpretation_without_reference_date():
    result = generate_euribor_reference_interpretation(
        tenor="6M",
        euribor_percentage=3.0,
        source_label="Manual simulated input",
        reference_date=None,
    )

    assert "manually entered" in result
    assert "Manual simulated input" in result
    assert "not live market data" in result


def test_build_manual_euribor_reference_returns_expected_result():
    result = build_manual_euribor_reference(
        tenor="6m",
        euribor_percentage=3.0,
        source_label="Manual simulated input",
        reference_date="2026-01-01",
    )

    assert result.tenor == "6M"
    assert result.euribor_percentage == 3.0
    assert result.source_label == "Manual simulated input"
    assert result.reference_date == "2026-01-01"
    assert result.is_manual_input is True
    assert "reference date 2026-01-01" in result.interpretation


def test_build_manual_euribor_reference_uses_default_source_label():
    result = build_manual_euribor_reference(
        tenor="3M",
        euribor_percentage=2.5,
        source_label="",
        reference_date=None,
    )

    assert result.tenor == "3M"
    assert result.euribor_percentage == 2.5
    assert result.source_label == "Manual simulated input"
    assert result.reference_date is None
    assert result.is_manual_input is True


def test_build_manual_euribor_reference_cleans_reference_date():
    result = build_manual_euribor_reference(
        tenor="12M",
        euribor_percentage=3.25,
        source_label="Manual input",
        reference_date=" 2026-01-01 ",
    )

    assert result.reference_date == "2026-01-01"
