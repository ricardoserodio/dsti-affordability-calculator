"""
DSTI calculation logic for the DSTI Affordability Calculator.

This module contains simple, explainable and educational financial calculations
related to Debt Service-to-Income (DSTI), repayment capacity and stressed
affordability scenarios.

The logic is banking-inspired, but it is not a credit approval system,
underwriting engine, financial advisory tool or replacement for formal
human credit analysis.

All examples and calculations should be interpreted as fictional, simulated
or anonymised educational outputs.
"""

from dataclasses import dataclass


@dataclass
class DSTIResult:
    """
    Stores the main DSTI simulation outputs.

    Attributes:
        base_dsti_percentage:
            DSTI calculated using the proposed monthly instalment.

        stressed_dsti_percentage:
            DSTI calculated using the stressed monthly instalment.

        maximum_monthly_debt_service:
            Indicative maximum monthly debt service based on the configured
            DSTI threshold.

        remaining_repayment_capacity:
            Indicative remaining capacity after existing monthly commitments.

        margin_against_stressed_instalment:
            Difference between remaining repayment capacity and stressed
            instalment.

        interpretation:
            Educational interpretation of the simulated result.
    """

    base_dsti_percentage: float
    stressed_dsti_percentage: float
    maximum_monthly_debt_service: float
    remaining_repayment_capacity: float
    margin_against_stressed_instalment: float
    interpretation: str


def calculate_dsti(
    monthly_net_income: float,
    existing_monthly_commitments: float,
    monthly_instalment: float,
) -> float:
    """
    Calculate the Debt Service-to-Income ratio.

    Formula:
        DSTI (%) =
        ((Existing Monthly Commitments + Monthly Instalment)
        / Monthly Net Income) * 100

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        existing_monthly_commitments:
            Existing monthly credit commitments.

        monthly_instalment:
            Proposed or stressed monthly instalment.

    Returns:
        DSTI percentage.

    Raises:
        ValueError:
            If monthly net income is less than or equal to zero.
            If commitments or instalment are negative.
    """

    if monthly_net_income <= 0:
        raise ValueError("Monthly net income must be greater than zero.")

    if existing_monthly_commitments < 0:
        raise ValueError("Existing monthly commitments cannot be negative.")

    if monthly_instalment < 0:
        raise ValueError("Monthly instalment cannot be negative.")

    total_monthly_debt_payments = existing_monthly_commitments + monthly_instalment

    return (total_monthly_debt_payments / monthly_net_income) * 100


def calculate_maximum_monthly_debt_service(
    monthly_net_income: float,
    configured_dsti_threshold_percentage: float,
) -> float:
    """
    Calculate indicative maximum monthly debt service based on a configured
    DSTI threshold.

    Formula:
        Maximum Monthly Debt Service =
        Monthly Net Income * Configured DSTI Threshold

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        configured_dsti_threshold_percentage:
            Configured DSTI threshold expressed as a percentage.

    Returns:
        Indicative maximum monthly debt service.

    Raises:
        ValueError:
            If income is less than or equal to zero.
            If the DSTI threshold is outside the 0-100 range.
    """

    if monthly_net_income <= 0:
        raise ValueError("Monthly net income must be greater than zero.")

    if configured_dsti_threshold_percentage <= 0:
        raise ValueError("DSTI threshold must be greater than zero.")

    if configured_dsti_threshold_percentage > 100:
        raise ValueError("DSTI threshold cannot be greater than 100%.")

    threshold_decimal = configured_dsti_threshold_percentage / 100

    return monthly_net_income * threshold_decimal


def calculate_remaining_repayment_capacity(
    monthly_net_income: float,
    existing_monthly_commitments: float,
    configured_dsti_threshold_percentage: float,
) -> float:
    """
    Calculate indicative remaining repayment capacity after existing
    commitments.

    Formula:
        Remaining Repayment Capacity =
        Maximum Monthly Debt Service - Existing Monthly Commitments

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        existing_monthly_commitments:
            Existing monthly credit commitments.

        configured_dsti_threshold_percentage:
            Configured DSTI threshold expressed as a percentage.

    Returns:
        Indicative remaining repayment capacity.

    Raises:
        ValueError:
            If existing monthly commitments are negative.
    """

    if existing_monthly_commitments < 0:
        raise ValueError("Existing monthly commitments cannot be negative.")

    maximum_monthly_debt_service = calculate_maximum_monthly_debt_service(
        monthly_net_income=monthly_net_income,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
    )

    return maximum_monthly_debt_service - existing_monthly_commitments


def calculate_margin_against_stressed_instalment(
    remaining_repayment_capacity: float,
    stressed_monthly_instalment: float,
) -> float:
    """
    Calculate the margin between remaining repayment capacity and the stressed
    monthly instalment.

    Formula:
        Margin Against Stressed Instalment =
        Remaining Repayment Capacity - Stressed Monthly Instalment

    Args:
        remaining_repayment_capacity:
            Indicative remaining repayment capacity.

        stressed_monthly_instalment:
            Stressed monthly instalment used in the simulation.

    Returns:
        Margin against stressed monthly instalment.

    Raises:
        ValueError:
            If stressed monthly instalment is negative.
    """

    if stressed_monthly_instalment < 0:
        raise ValueError("Stressed monthly instalment cannot be negative.")

    return remaining_repayment_capacity - stressed_monthly_instalment


def generate_dsti_interpretation(
    base_dsti_percentage: float,
    stressed_dsti_percentage: float,
    configured_dsti_threshold_percentage: float,
    margin_against_stressed_instalment: float,
) -> str:
    """
    Generate an educational and non-decisive interpretation of the DSTI result.

    This function avoids approval/rejection language. It only provides an
    explainable simulation summary focused on financial literacy and risk
    awareness.

    Args:
        base_dsti_percentage:
            DSTI calculated using the proposed monthly instalment.

        stressed_dsti_percentage:
            DSTI calculated using the stressed monthly instalment.

        configured_dsti_threshold_percentage:
            Configured DSTI threshold used for the simulation.

        margin_against_stressed_instalment:
            Difference between remaining repayment capacity and stressed
            monthly instalment.

    Returns:
        Educational interpretation string.
    """

    if stressed_dsti_percentage > configured_dsti_threshold_percentage:
        return (
            "Risk awareness warning: the stressed DSTI exceeds the configured "
            "simulation threshold. This does not represent credit rejection, "
            "but it suggests that the scenario may require careful review."
        )

    if base_dsti_percentage > configured_dsti_threshold_percentage:
        return (
            "Risk awareness warning: the base DSTI exceeds the configured "
            "simulation threshold. This does not represent a lending decision, "
            "but the scenario may indicate increased financial pressure."
        )

    if margin_against_stressed_instalment < 0:
        return (
            "Risk awareness warning: the stressed instalment is above the "
            "indicative remaining repayment capacity. This is an educational "
            "simulation flag and not a credit decision."
        )

    return (
        "Within the configured simulation assumptions, the scenario shows a "
        "more favourable affordability position. This result is purely "
        "indicative and must not be interpreted as credit approval, eligibility "
        "confirmation or financial advice."
    )


def run_dsti_simulation(
    monthly_net_income: float,
    existing_monthly_commitments: float,
    proposed_monthly_instalment: float,
    stressed_monthly_instalment: float,
    configured_dsti_threshold_percentage: float,
) -> DSTIResult:
    """
    Run a complete educational DSTI simulation.

    The simulation calculates:

    - base DSTI;
    - stressed DSTI;
    - indicative maximum monthly debt service;
    - remaining repayment capacity;
    - margin against stressed instalment;
    - non-decisive educational interpretation.

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        existing_monthly_commitments:
            Existing monthly credit commitments.

        proposed_monthly_instalment:
            Proposed monthly instalment.

        stressed_monthly_instalment:
            Stressed monthly instalment.

        configured_dsti_threshold_percentage:
            Configured DSTI threshold expressed as a percentage.

    Returns:
        DSTIResult object with the simulation outputs.
    """

    base_dsti_percentage = calculate_dsti(
        monthly_net_income=monthly_net_income,
        existing_monthly_commitments=existing_monthly_commitments,
        monthly_instalment=proposed_monthly_instalment,
    )

    stressed_dsti_percentage = calculate_dsti(
        monthly_net_income=monthly_net_income,
        existing_monthly_commitments=existing_monthly_commitments,
        monthly_instalment=stressed_monthly_instalment,
    )

    maximum_monthly_debt_service = calculate_maximum_monthly_debt_service(
        monthly_net_income=monthly_net_income,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
    )

    remaining_repayment_capacity = calculate_remaining_repayment_capacity(
        monthly_net_income=monthly_net_income,
        existing_monthly_commitments=existing_monthly_commitments,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
    )

    margin_against_stressed_instalment = calculate_margin_against_stressed_instalment(
        remaining_repayment_capacity=remaining_repayment_capacity,
        stressed_monthly_instalment=stressed_monthly_instalment,
    )

    interpretation = generate_dsti_interpretation(
        base_dsti_percentage=base_dsti_percentage,
        stressed_dsti_percentage=stressed_dsti_percentage,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
        margin_against_stressed_instalment=margin_against_stressed_instalment,
    )

    return DSTIResult(
        base_dsti_percentage=round(base_dsti_percentage, 2),
        stressed_dsti_percentage=round(stressed_dsti_percentage, 2),
        maximum_monthly_debt_service=round(maximum_monthly_debt_service, 2),
        remaining_repayment_capacity=round(remaining_repayment_capacity, 2),
        margin_against_stressed_instalment=round(
            margin_against_stressed_instalment,
            2,
        ),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_dsti_simulation(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
    )

    print(example_result)
