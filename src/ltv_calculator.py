"""
Loan-to-Value (LTV) calculation logic for the DSTI Affordability Calculator.

This module contains simple, explainable and educational calculations related
to Loan-to-Value simulation.

The logic is banking-inspired, but it is not a credit approval system,
underwriting engine, financial advisory tool or replacement for formal
human credit analysis.

All examples and outputs should be interpreted as fictional, simulated or
anonymised educational results.
"""

from dataclasses import dataclass


@dataclass
class LTVResult:
    """
    Stores the main LTV simulation outputs.

    Attributes:
        ltv_percentage:
            Loan-to-Value percentage calculated using the selected property
            value assumption.

        property_value_used:
            Property value used in the LTV calculation.

        loan_amount:
            Simulated loan amount.

        interpretation:
            Educational interpretation of the simulated LTV result.
    """

    ltv_percentage: float
    property_value_used: float
    loan_amount: float
    interpretation: str


def select_property_value(
    acquisition_value: float | None = None,
    valuation_value: float | None = None,
    use_lower_value: bool = True,
) -> float:
    """
    Select the property value to be used in the LTV simulation.

    Args:
        acquisition_value:
            Simulated acquisition value.

        valuation_value:
            Simulated valuation value.

        use_lower_value:
            If True, the lower of acquisition value and valuation value is used
            when both values are available.

    Returns:
        Property value selected for the simulation.

    Raises:
        ValueError:
            If no valid property value is provided.
            If any provided property value is less than or equal to zero.
    """

    values = []

    if acquisition_value is not None:
        if acquisition_value <= 0:
            raise ValueError("Acquisition value must be greater than zero.")
        values.append(acquisition_value)

    if valuation_value is not None:
        if valuation_value <= 0:
            raise ValueError("Valuation value must be greater than zero.")
        values.append(valuation_value)

    if not values:
        raise ValueError("At least one property value must be provided.")

    if len(values) == 1:
        return values[0]

    if use_lower_value:
        return min(values)

    return valuation_value if valuation_value is not None else acquisition_value


def calculate_ltv(
    loan_amount: float,
    property_value: float,
) -> float:
    """
    Calculate Loan-to-Value.

    Formula:
        LTV (%) = Loan Amount / Property Value × 100

    Args:
        loan_amount:
            Simulated loan amount.

        property_value:
            Property value used in the simulation.

    Returns:
        LTV percentage.

    Raises:
        ValueError:
            If loan amount is less than or equal to zero.
            If property value is less than or equal to zero.
    """

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if property_value <= 0:
        raise ValueError("Property value must be greater than zero.")

    return (loan_amount / property_value) * 100


def generate_ltv_interpretation(
    ltv_percentage: float,
    configured_ltv_threshold_percentage: float | None = None,
) -> str:
    """
    Generate an educational and non-decisive interpretation of the LTV result.

    This function avoids approval/rejection language. It only provides an
    explainable simulation summary focused on financial literacy and risk
    awareness.

    Args:
        ltv_percentage:
            Loan-to-Value percentage calculated by the simulation.

        configured_ltv_threshold_percentage:
            Optional configured LTV threshold used as a simulation assumption.

    Returns:
        Educational interpretation string.
    """

    if configured_ltv_threshold_percentage is not None:
        if configured_ltv_threshold_percentage <= 0:
            raise ValueError("Configured LTV threshold must be greater than zero.")

        if configured_ltv_threshold_percentage > 100:
            raise ValueError("Configured LTV threshold cannot be greater than 100%.")

        if ltv_percentage > configured_ltv_threshold_percentage:
            return (
                "Risk awareness warning: the simulated LTV exceeds the configured "
                "simulation threshold. This does not represent credit rejection, "
                "but it suggests that the scenario may require careful review."
            )

    if ltv_percentage > 120:
        return (
            "Risk awareness warning: the simulated LTV appears unusually high. "
            "Please review the loan amount and property value assumptions. "
            "This is not a credit decision."
        )

    if ltv_percentage > 100:
        return (
            "Risk awareness warning: the simulated loan amount is higher than "
            "the selected property value assumption. This is an educational "
            "flag only and not a lending decision."
        )

    return (
        "Within the configured simulation assumptions, the LTV result appears "
        "more balanced. This result is purely indicative and must not be "
        "interpreted as credit approval, eligibility confirmation or financial "
        "advice."
    )


def run_ltv_simulation(
    loan_amount: float,
    acquisition_value: float | None = None,
    valuation_value: float | None = None,
    configured_ltv_threshold_percentage: float | None = None,
    use_lower_value: bool = True,
) -> LTVResult:
    """
    Run a complete educational LTV simulation.

    The simulation calculates:

    - selected property value;
    - LTV percentage;
    - non-decisive educational interpretation.

    Args:
        loan_amount:
            Simulated loan amount.

        acquisition_value:
            Optional simulated acquisition value.

        valuation_value:
            Optional simulated valuation value.

        configured_ltv_threshold_percentage:
            Optional configured LTV threshold expressed as a percentage.

        use_lower_value:
            If True, the lower of acquisition value and valuation value is used
            when both values are available.

    Returns:
        LTVResult object with the simulation outputs.
    """

    property_value_used = select_property_value(
        acquisition_value=acquisition_value,
        valuation_value=valuation_value,
        use_lower_value=use_lower_value,
    )

    ltv_percentage = calculate_ltv(
        loan_amount=loan_amount,
        property_value=property_value_used,
    )

    interpretation = generate_ltv_interpretation(
        ltv_percentage=ltv_percentage,
        configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
    )

    return LTVResult(
        ltv_percentage=round(ltv_percentage, 2),
        property_value_used=round(property_value_used, 2),
        loan_amount=round(loan_amount, 2),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_ltv_simulation(
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        use_lower_value=True,
    )

    print(example_result)
