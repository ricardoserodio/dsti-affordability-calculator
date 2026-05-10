"""
Unit tests for the commitments analysis module.

These tests validate the structured monthly commitments logic used by the
DSTI Affordability Calculator.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
bank policy model, financial advisory tool or replacement for formal human
credit analysis.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from commitments_analyzer import (
    analyse_existing_commitments,
    calculate_total_existing_commitments,
    generate_commitments_interpretation,
    identify_highest_commitment_category,
    validate_commitment_value,
)


def test_validate_commitment_value_base_case():
    result = validate_commitment_value(150, "Auto loan commitment")

    assert result == 150.0


def test_validate_commitment_value_allows_zero():
    result = validate_commitment_value(0, "Housing commitment")

    assert result == 0.0


def test_validate_commitment_value_raises_error_for_missing_value():
    with pytest.raises(ValueError):
        validate_commitment_value(None, "Housing commitment")


def test_validate_commitment_value_raises_error_for_negative_value():
    with pytest.raises(ValueError):
        validate_commitment_value(-1, "Personal loan commitment")


def test_calculate_total_existing_commitments_base_case():
    result = calculate_total_existing_commitments(
        housing_commitment=0,
        auto_loan_commitment=150,
        personal_loan_commitment=100,
        credit_card_commitment=50,
        other_credit_commitments=25,
    )

    assert result == 325.0


def test_calculate_total_existing_commitments_all_zero():
    result = calculate_total_existing_commitments(
        housing_commitment=0,
        auto_loan_commitment=0,
        personal_loan_commitment=0,
        credit_card_commitment=0,
        other_credit_commitments=0,
    )

    assert result == 0.0


def test_calculate_total_existing_commitments_raises_error_for_negative_value():
    with pytest.raises(ValueError):
        calculate_total_existing_commitments(
            housing_commitment=0,
            auto_loan_commitment=-150,
            personal_loan_commitment=100,
            credit_card_commitment=50,
            other_credit_commitments=25,
        )


def test_identify_highest_commitment_category_base_case():
    result = identify_highest_commitment_category(
        housing_commitment=0,
        auto_loan_commitment=150,
        personal_loan_commitment=100,
        credit_card_commitment=50,
        other_credit_commitments=25,
    )

    assert result == "Auto loan commitment"


def test_identify_highest_commitment_category_housing_highest():
    result = identify_highest_commitment_category(
        housing_commitment=600,
        auto_loan_commitment=150,
        personal_loan_commitment=100,
        credit_card_commitment=50,
        other_credit_commitments=25,
    )

    assert result == "Housing commitment"


def test_identify_highest_commitment_category_all_zero():
    result = identify_highest_commitment_category(
        housing_commitment=0,
        auto_loan_commitment=0,
        personal_loan_commitment=0,
        credit_card_commitment=0,
        other_credit_commitments=0,
    )

    assert result == "No existing commitments"


def test_generate_commitments_interpretation_no_commitments():
    result = generate_commitments_interpretation(
        total_existing_commitments=0,
        highest_commitment_category="No existing commitments",
    )

    assert "No existing monthly credit commitments" in result
    assert "fictional scenario" in result


def test_generate_commitments_interpretation_high_commitments():
    result = generate_commitments_interpretation(
        total_existing_commitments=2500,
        highest_commitment_category="Housing commitment",
    )

    assert "Risk awareness warning" in result
    assert "appear high" in result
    assert "Housing commitment" in result


def test_generate_commitments_interpretation_standard_case():
    result = generate_commitments_interpretation(
        total_existing_commitments=325,
        highest_commitment_category="Auto loan commitment",
    )

    assert "financial data quality" in result
    assert "DSTI calculation" in result
    assert "Auto loan commitment" in result


def test_analyse_existing_commitments_returns_expected_result():
    result = analyse_existing_commitments(
        housing_commitment=0,
        auto_loan_commitment=150,
        personal_loan_commitment=100,
        credit_card_commitment=50,
        other_credit_commitments=25,
    )

    assert result.housing_commitment == 0.0
    assert result.auto_loan_commitment == 150.0
    assert result.personal_loan_commitment == 100.0
    assert result.credit_card_commitment == 50.0
    assert result.other_credit_commitments == 25.0
    assert result.total_existing_commitments == 325.0
    assert result.highest_commitment_category == "Auto loan commitment"
    assert "financial data quality" in result.interpretation


def test_analyse_existing_commitments_zero_commitments():
    result = analyse_existing_commitments(
        housing_commitment=0,
        auto_loan_commitment=0,
        personal_loan_commitment=0,
        credit_card_commitment=0,
        other_credit_commitments=0,
    )

    assert result.total_existing_commitments == 0.0
    assert result.highest_commitment_category == "No existing commitments"
    assert "No existing monthly credit commitments" in result.interpretation


def test_analyse_existing_commitments_raises_error_for_negative_commitment():
    with pytest.raises(ValueError):
        analyse_existing_commitments(
            housing_commitment=0,
            auto_loan_commitment=150,
            personal_loan_commitment=-100,
            credit_card_commitment=50,
            other_credit_commitments=25,
        )
