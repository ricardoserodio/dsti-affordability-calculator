"""
Maturity and age scenario validation for the DSTI Affordability Calculator.

This module contains simple, explainable and educational checks related to
loan maturity and simulated age at the end of a loan.

The logic is banking-inspired, but it is not a credit approval system,
underwriting engine, financial advisory tool or replacement for formal
human credit analysis.

All values should be fictional, simulated or anonymised.
"""

from dataclasses import dataclass


@dataclass
class MaturityResult:
    """
    Stores the main maturity simulation outputs.

    Attributes:
        current_age:
            Fictional or anonymised current age used in the simulation.

        loan_maturity_years:
            Simulated loan maturity in years.

        age_at_end_of_loan:
            Estimated age at the end of the simulated loan.

        is_within_configured_assumption:
            True when age at end of loan is within the configured simulation
            assumption.

        interpretation:
            Educational interpretation of the simulated maturity result.
    """

    current_age: float
    loan_maturity_years: float
    age_at_end_of_loan: float
    is_within_configured_assumption: bool
    interpretation: str


def calculate_age_at_end_of_loan(
    current_age: float,
    loan_maturity_years: float,
) -> float:
    """
    Calculate the estimated age at the end of a simulated loan.

    Formula:
        Age at End of Loan = Current Age + Loan Maturity in Years

    Args:
        current_age:
            Fictional or anonymised current age used in the simulation.

        loan_maturity_years:
            Simulated loan maturity in years.

    Returns:
        Estimated age at the end of the simulated loan.

    Raises:
        ValueError:
            If current age is less than or equal to zero.
            If loan maturity is less than or equal to zero.
    """

    if current_age <= 0:
        raise ValueError("Current age must be greater than zero.")

    if loan_maturity_years <= 0:
        raise ValueError("Loan maturity must be greater than zero.")

    return current_age + loan_maturity_years


def validate_age_range(current_age: float) -> list[str]:
    """
    Generate educational warnings for unusual current age assumptions.

    Args:
        current_age:
            Fictional or anonymised current age used in the simulation.

    Returns:
        List of warning messages.
    """

    warnings = []

    if current_age < 18:
        warnings.append(
            "Current age appears below the expected range for this simulation. "
            "Please confirm that the value is fictional or anonymised."
        )

    if current_age > 100:
        warnings.append(
            "Current age appears unusually high for this simulation. "
            "Please review the assumption."
        )

    return warnings


def validate_maturity_range(loan_maturity_years: float) -> list[str]:
    """
    Generate educational warnings for unusual maturity assumptions.

    Args:
        loan_maturity_years:
            Simulated loan maturity in years.

    Returns:
        List of warning messages.
    """

    warnings = []

    if loan_maturity_years > 50:
        warnings.append(
            "Loan maturity appears unusually long for this simulation. "
            "Please review the assumption."
        )

    return warnings


def generate_maturity_interpretation(
    age_at_end_of_loan: float,
    configured_maximum_age_at_end: float,
    warnings: list[str] | None = None,
) -> str:
    """
    Generate an educational and non-decisive maturity interpretation.

    This function avoids approval/rejection language. It only provides an
    explainable simulation summary focused on risk awareness.

    Args:
        age_at_end_of_loan:
            Estimated age at the end of the simulated loan.

        configured_maximum_age_at_end:
            Configured maximum age assumption used for the simulation.

        warnings:
            Optional validation warnings.

    Returns:
        Educational interpretation string.
    """

    if configured_maximum_age_at_end <= 0:
        raise ValueError("Configured maximum age assumption must be greater than zero.")

    if warnings:
        warning_text = " ".join(warnings)
    else:
        warning_text = ""

    if age_at_end_of_loan > configured_maximum_age_at_end:
        return (
            "Risk awareness warning: the simulated age at the end of the loan "
            "exceeds the configured maximum age assumption for this simulation. "
            "This is not an eligibility decision or credit rejection. "
            f"{warning_text}"
        ).strip()

    if age_at_end_of_loan > 75:
        return (
            "Risk awareness warning: the simulated age at the end of the loan "
            "appears high. This should be interpreted only as an educational "
            f"flag. {warning_text}"
        ).strip()

    return (
        "Within the configured simulation assumptions, the maturity scenario "
        "appears more balanced. This result is purely indicative and must not "
        "be interpreted as credit approval, eligibility confirmation or "
        f"financial advice. {warning_text}"
    ).strip()


def run_maturity_simulation(
    current_age: float,
    loan_maturity_years: float,
    configured_maximum_age_at_end: float = 75,
) -> MaturityResult:
    """
    Run a complete educational maturity simulation.

    The simulation calculates:

    - age at the end of the simulated loan;
    - whether the age is within the configured assumption;
    - non-decisive educational interpretation.

    Args:
        current_age:
            Fictional or anonymised current age used in the simulation.

        loan_maturity_years:
            Simulated loan maturity in years.

        configured_maximum_age_at_end:
            Configured maximum age assumption used for the simulation.

    Returns:
        MaturityResult object with the simulation outputs.
    """

    age_at_end_of_loan = calculate_age_at_end_of_loan(
        current_age=current_age,
        loan_maturity_years=loan_maturity_years,
    )

    warnings = []
    warnings.extend(validate_age_range(current_age=current_age))
    warnings.extend(validate_maturity_range(loan_maturity_years=loan_maturity_years))

    is_within_configured_assumption = (
        age_at_end_of_loan <= configured_maximum_age_at_end
    )

    interpretation = generate_maturity_interpretation(
        age_at_end_of_loan=age_at_end_of_loan,
        configured_maximum_age_at_end=configured_maximum_age_at_end,
        warnings=warnings,
    )

    return MaturityResult(
        current_age=round(current_age, 2),
        loan_maturity_years=round(loan_maturity_years, 2),
        age_at_end_of_loan=round(age_at_end_of_loan, 2),
        is_within_configured_assumption=is_within_configured_assumption,
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_maturity_simulation(
        current_age=35,
        loan_maturity_years=30,
        configured_maximum_age_at_end=75,
    )

    print(example_result)
