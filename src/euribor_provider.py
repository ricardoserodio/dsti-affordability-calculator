"""
Manual EURIBOR reference provider for the DSTI Affordability Calculator.

This module does not fetch live market data.

It provides a structured way to handle manually entered simulated EURIBOR
assumptions, including tenor, value, source label and optional reference date.

The purpose is educational, demonstrative and portfolio-oriented.

This module is not a live benchmark data provider, bank pricing engine,
financial advisory tool, credit approval system or replacement for formal
human credit analysis.

All values should be fictional, simulated, manually entered or clearly labelled
as educational assumptions.
"""

from dataclasses import dataclass


ALLOWED_EURIBOR_TENORS = {"1M", "3M", "6M", "12M"}


@dataclass
class EuriborReferenceResult:
    """
    Stores a manually defined simulated EURIBOR reference.

    Attributes:
        tenor:
            Simulated EURIBOR tenor, such as 3M, 6M or 12M.

        euribor_percentage:
            Simulated EURIBOR value expressed as a percentage.

        source_label:
            Label describing the source of the EURIBOR assumption.

        reference_date:
            Optional reference date for the assumption.

        is_manual_input:
            Indicates that the value was manually entered.

        interpretation:
            Educational interpretation of the EURIBOR assumption.
    """

    tenor: str
    euribor_percentage: float
    source_label: str
    reference_date: str | None
    is_manual_input: bool
    interpretation: str


def normalise_euribor_tenor(tenor: str) -> str:
    """
    Normalise a EURIBOR tenor string.

    Args:
        tenor:
            EURIBOR tenor input.

    Returns:
        Normalised tenor string.

    Raises:
        ValueError:
            If tenor is missing or unsupported.
    """

    if tenor is None or str(tenor).strip() == "":
        raise ValueError("EURIBOR tenor is required.")

    normalised_tenor = str(tenor).strip().upper()

    if normalised_tenor not in ALLOWED_EURIBOR_TENORS:
        raise ValueError(
            "Unsupported EURIBOR tenor. Allowed values are: 1M, 3M, 6M, 12M."
        )

    return normalised_tenor


def validate_euribor_percentage(euribor_percentage: float) -> float:
    """
    Validate a simulated EURIBOR percentage.

    Args:
        euribor_percentage:
            Simulated EURIBOR value expressed as a percentage.

    Returns:
        The validated EURIBOR percentage.

    Raises:
        ValueError:
            If the value is missing or unrealistically high for this
            educational simulation.
    """

    if euribor_percentage is None:
        raise ValueError("EURIBOR percentage is required.")

    if euribor_percentage > 25:
        raise ValueError(
            "EURIBOR percentage appears unrealistically high for this "
            "educational simulation."
        )

    return euribor_percentage


def generate_euribor_reference_interpretation(
    tenor: str,
    euribor_percentage: float,
    source_label: str,
    reference_date: str | None,
) -> str:
    """
    Generate an educational interpretation for a simulated EURIBOR assumption.

    Args:
        tenor:
            Simulated EURIBOR tenor.

        euribor_percentage:
            Simulated EURIBOR value.

        source_label:
            Source label for the assumption.

        reference_date:
            Optional reference date.

    Returns:
        Educational interpretation string.
    """

    if euribor_percentage < 0:
        return (
            f"The simulated EURIBOR {tenor} assumption is negative. This may be "
            "intentional for scenario analysis, but should be reviewed before "
            "interpreting the result. The value is treated as a manual "
            "educational assumption, not as live market data."
        )

    if euribor_percentage > 10:
        return (
            f"Risk awareness warning: the simulated EURIBOR {tenor} assumption "
            "appears high. This may create significant affordability pressure "
            "when combined with spread and stress assumptions. The value is "
            "educational only and not financial advice."
        )

    if reference_date:
        return (
            f"The simulated EURIBOR {tenor} assumption is manually labelled with "
            f"source '{source_label}' and reference date {reference_date}. This "
            "value is used only for educational scenario analysis and is not "
            "live market data, a bank quote or financial advice."
        )

    return (
        f"The simulated EURIBOR {tenor} assumption is manually entered and "
        f"labelled as '{source_label}'. This value is used only for educational "
        "scenario analysis and is not live market data, a bank quote or "
        "financial advice."
    )


def build_manual_euribor_reference(
    tenor: str,
    euribor_percentage: float,
    source_label: str = "Manual simulated input",
    reference_date: str | None = None,
) -> EuriborReferenceResult:
    """
    Build a structured manual EURIBOR reference.

    Args:
        tenor:
            Simulated EURIBOR tenor.

        euribor_percentage:
            Simulated EURIBOR value expressed as a percentage.

        source_label:
            Label describing where the assumption came from.

        reference_date:
            Optional reference date for the assumption.

    Returns:
        EuriborReferenceResult object.
    """

    normalised_tenor = normalise_euribor_tenor(tenor)
    validated_euribor_percentage = validate_euribor_percentage(
        euribor_percentage=euribor_percentage
    )

    if source_label is None or str(source_label).strip() == "":
        source_label = "Manual simulated input"

    cleaned_source_label = str(source_label).strip()

    cleaned_reference_date = None

    if reference_date is not None and str(reference_date).strip() != "":
        cleaned_reference_date = str(reference_date).strip()

    interpretation = generate_euribor_reference_interpretation(
        tenor=normalised_tenor,
        euribor_percentage=validated_euribor_percentage,
        source_label=cleaned_source_label,
        reference_date=cleaned_reference_date,
    )

    return EuriborReferenceResult(
        tenor=normalised_tenor,
        euribor_percentage=round(validated_euribor_percentage, 2),
        source_label=cleaned_source_label,
        reference_date=cleaned_reference_date,
        is_manual_input=True,
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = build_manual_euribor_reference(
        tenor="6M",
        euribor_percentage=3.0,
        source_label="Manual simulated input",
        reference_date="2026-01-01",
    )

    print(example_result)
