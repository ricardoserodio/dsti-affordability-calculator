"""
Commitments analysis module for the DSTI Affordability Calculator.

This module separates existing monthly financial commitments into clear
educational categories before calculating the total existing monthly debt
service used in DSTI simulations.

The purpose is to improve financial data quality, explainability and risk
awareness.

This module is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
bank policy model, financial advisory tool or replacement for formal human
credit analysis.

All values should be fictional, simulated or anonymised.
"""

from dataclasses import dataclass


@dataclass
class CommitmentsResult:
    """
    Stores the result of a structured commitments analysis.

    Attributes:
        housing_commitment:
            Existing monthly housing-related credit commitment.

        auto_loan_commitment:
            Existing monthly auto loan commitment.

        personal_loan_commitment:
            Existing monthly personal loan commitment.

        credit_card_commitment:
            Existing monthly credit card commitment.

        other_credit_commitments:
            Other existing monthly credit commitments.

        total_existing_commitments:
            Total existing monthly commitments used in DSTI calculation.

        highest_commitment_category:
            Category with the highest monthly commitment.

        interpretation:
            Educational interpretation of the commitments profile.
    """

    housing_commitment: float
    auto_loan_commitment: float
    personal_loan_commitment: float
    credit_card_commitment: float
    other_credit_commitments: float
    total_existing_commitments: float
    highest_commitment_category: str
    interpretation: str


def validate_commitment_value(value: float, field_name: str) -> float:
    """
    Validate a monthly commitment value.

    Args:
        value:
            Monthly commitment amount.

        field_name:
            Name of the field being validated.

    Returns:
        Validated commitment value.

    Raises:
        ValueError:
            If the value is missing or negative.
    """

    if value is None:
        raise ValueError(f"{field_name} is required.")

    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")

    return float(value)


def calculate_total_existing_commitments(
    housing_commitment: float = 0.0,
    auto_loan_commitment: float = 0.0,
    personal_loan_commitment: float = 0.0,
    credit_card_commitment: float = 0.0,
    other_credit_commitments: float = 0.0,
) -> float:
    """
    Calculate total existing monthly credit commitments.

    Args:
        housing_commitment:
            Existing monthly housing-related credit commitment.

        auto_loan_commitment:
            Existing monthly auto loan commitment.

        personal_loan_commitment:
            Existing monthly personal loan commitment.

        credit_card_commitment:
            Existing monthly credit card commitment.

        other_credit_commitments:
            Other existing monthly credit commitments.

    Returns:
        Total existing monthly commitments.
    """

    validated_housing = validate_commitment_value(
        housing_commitment,
        "Housing commitment",
    )
    validated_auto_loan = validate_commitment_value(
        auto_loan_commitment,
        "Auto loan commitment",
    )
    validated_personal_loan = validate_commitment_value(
        personal_loan_commitment,
        "Personal loan commitment",
    )
    validated_credit_card = validate_commitment_value(
        credit_card_commitment,
        "Credit card commitment",
    )
    validated_other_credit = validate_commitment_value(
        other_credit_commitments,
        "Other credit commitments",
    )

    total_commitments = (
        validated_housing
        + validated_auto_loan
        + validated_personal_loan
        + validated_credit_card
        + validated_other_credit
    )

    return round(total_commitments, 2)


def identify_highest_commitment_category(
    housing_commitment: float = 0.0,
    auto_loan_commitment: float = 0.0,
    personal_loan_commitment: float = 0.0,
    credit_card_commitment: float = 0.0,
    other_credit_commitments: float = 0.0,
) -> str:
    """
    Identify the commitment category with the highest monthly value.

    Args:
        housing_commitment:
            Existing monthly housing-related credit commitment.

        auto_loan_commitment:
            Existing monthly auto loan commitment.

        personal_loan_commitment:
            Existing monthly personal loan commitment.

        credit_card_commitment:
            Existing monthly credit card commitment.

        other_credit_commitments:
            Other existing monthly credit commitments.

    Returns:
        Name of the highest commitment category.
    """

    commitment_categories = {
        "Housing commitment": housing_commitment,
        "Auto loan commitment": auto_loan_commitment,
        "Personal loan commitment": personal_loan_commitment,
        "Credit card commitment": credit_card_commitment,
        "Other credit commitments": other_credit_commitments,
    }

    if all(value == 0 for value in commitment_categories.values()):
        return "No existing commitments"

    return max(commitment_categories, key=commitment_categories.get)


def generate_commitments_interpretation(
    total_existing_commitments: float,
    highest_commitment_category: str,
) -> str:
    """
    Generate an educational interpretation of existing commitments.

    Args:
        total_existing_commitments:
            Total existing monthly commitments.

        highest_commitment_category:
            Category with the highest monthly commitment.

    Returns:
        Educational interpretation string.
    """

    if total_existing_commitments == 0:
        return (
            "No existing monthly credit commitments were entered. This may be "
            "valid for a fictional scenario, but the assumption should be "
            "reviewed before interpreting the DSTI result."
        )

    if total_existing_commitments > 2000:
        return (
            "Risk awareness warning: total existing monthly commitments appear "
            "high for an educational affordability simulation. This may place "
            "additional pressure on DSTI and remaining repayment capacity. "
            f"The largest category is: {highest_commitment_category}."
        )

    return (
        "Existing monthly commitments were grouped by category to improve "
        "financial data quality and explainability. These commitments are used "
        "as part of the DSTI calculation. The largest category is: "
        f"{highest_commitment_category}."
    )


def analyse_existing_commitments(
    housing_commitment: float = 0.0,
    auto_loan_commitment: float = 0.0,
    personal_loan_commitment: float = 0.0,
    credit_card_commitment: float = 0.0,
    other_credit_commitments: float = 0.0,
) -> CommitmentsResult:
    """
    Analyse existing monthly commitments by category.

    Args:
        housing_commitment:
            Existing monthly housing-related credit commitment.

        auto_loan_commitment:
            Existing monthly auto loan commitment.

        personal_loan_commitment:
            Existing monthly personal loan commitment.

        credit_card_commitment:
            Existing monthly credit card commitment.

        other_credit_commitments:
            Other existing monthly credit commitments.

    Returns:
        CommitmentsResult object.
    """

    validated_housing = validate_commitment_value(
        housing_commitment,
        "Housing commitment",
    )
    validated_auto_loan = validate_commitment_value(
        auto_loan_commitment,
        "Auto loan commitment",
    )
    validated_personal_loan = validate_commitment_value(
        personal_loan_commitment,
        "Personal loan commitment",
    )
    validated_credit_card = validate_commitment_value(
        credit_card_commitment,
        "Credit card commitment",
    )
    validated_other_credit = validate_commitment_value(
        other_credit_commitments,
        "Other credit commitments",
    )

    total_existing_commitments = calculate_total_existing_commitments(
        housing_commitment=validated_housing,
        auto_loan_commitment=validated_auto_loan,
        personal_loan_commitment=validated_personal_loan,
        credit_card_commitment=validated_credit_card,
        other_credit_commitments=validated_other_credit,
    )

    highest_commitment_category = identify_highest_commitment_category(
        housing_commitment=validated_housing,
        auto_loan_commitment=validated_auto_loan,
        personal_loan_commitment=validated_personal_loan,
        credit_card_commitment=validated_credit_card,
        other_credit_commitments=validated_other_credit,
    )

    interpretation = generate_commitments_interpretation(
        total_existing_commitments=total_existing_commitments,
        highest_commitment_category=highest_commitment_category,
    )

    return CommitmentsResult(
        housing_commitment=round(validated_housing, 2),
        auto_loan_commitment=round(validated_auto_loan, 2),
        personal_loan_commitment=round(validated_personal_loan, 2),
        credit_card_commitment=round(validated_credit_card, 2),
        other_credit_commitments=round(validated_other_credit, 2),
        total_existing_commitments=total_existing_commitments,
        highest_commitment_category=highest_commitment_category,
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = analyse_existing_commitments(
        housing_commitment=0,
        auto_loan_commitment=150,
        personal_loan_commitment=100,
        credit_card_commitment=50,
        other_credit_commitments=0,
    )

    print(example_result)
