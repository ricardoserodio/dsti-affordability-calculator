"""
Income handling logic for the DSTI Affordability Calculator.

This module contains simple, explainable and educational income calculations
used in affordability and DSTI simulations.

The logic is banking-inspired, but it is not a credit approval system,
underwriting engine, financial advisory tool or replacement for formal
human credit analysis.

All income values should be fictional, simulated or anonymised.
"""

from dataclasses import dataclass


@dataclass
class IncomeResult:
    """
    Stores the main income simulation outputs.

    Attributes:
        monthly_net_income:
            Final monthly net income used in the simulation.

        annual_net_income:
            Estimated annual net income based on the selected monthly income.

        income_source_count:
            Number of simulated income sources considered.

        conservative_monthly_income:
            Conservative monthly income assumption.

        interpretation:
            Educational interpretation of the income assumption.
    """

    monthly_net_income: float
    annual_net_income: float
    income_source_count: int
    conservative_monthly_income: float
    interpretation: str


def calculate_total_monthly_income(income_sources: list[float]) -> float:
    """
    Calculate total monthly net income from multiple simulated income sources.

    Args:
        income_sources:
            List of fictional, simulated or anonymised monthly net income values.

    Returns:
        Total monthly net income.

    Raises:
        ValueError:
            If no income sources are provided.
            If any income source is negative.
    """

    if not income_sources:
        raise ValueError("At least one income source must be provided.")

    for income in income_sources:
        if income < 0:
            raise ValueError("Income sources cannot be negative.")

    return sum(income_sources)


def calculate_annual_net_income(monthly_net_income: float) -> float:
    """
    Estimate annual net income based on monthly net income.

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

    Returns:
        Estimated annual net income.

    Raises:
        ValueError:
            If monthly net income is negative.
    """

    if monthly_net_income < 0:
        raise ValueError("Monthly net income cannot be negative.")

    return monthly_net_income * 12


def calculate_conservative_income(
    income_sources: list[float],
    conservative_factor: float = 0.90,
) -> float:
    """
    Calculate a conservative monthly income assumption.

    The conservative factor reduces total monthly income to simulate a more
    prudent affordability scenario.

    Example:
        Total income = 2500
        Conservative factor = 0.90
        Conservative income = 2250

    Args:
        income_sources:
            List of fictional, simulated or anonymised monthly net income values.

        conservative_factor:
            Factor applied to total income. Must be between 0 and 1.

    Returns:
        Conservative monthly income assumption.

    Raises:
        ValueError:
            If the conservative factor is outside the 0-1 range.
    """

    if conservative_factor <= 0 or conservative_factor > 1:
        raise ValueError("Conservative factor must be greater than 0 and up to 1.")

    total_income = calculate_total_monthly_income(income_sources)

    return total_income * conservative_factor


def select_income_for_simulation(
    income_sources: list[float],
    use_conservative_income: bool = False,
    conservative_factor: float = 0.90,
) -> float:
    """
    Select the monthly income value to be used in the simulation.

    Args:
        income_sources:
            List of fictional, simulated or anonymised monthly net income values.

        use_conservative_income:
            If True, applies the conservative income factor.

        conservative_factor:
            Factor used when conservative income is selected.

    Returns:
        Monthly net income selected for the simulation.
    """

    if use_conservative_income:
        return calculate_conservative_income(
            income_sources=income_sources,
            conservative_factor=conservative_factor,
        )

    return calculate_total_monthly_income(income_sources)


def generate_income_interpretation(
    monthly_net_income: float,
    conservative_monthly_income: float,
    use_conservative_income: bool,
) -> str:
    """
    Generate an educational and non-decisive interpretation of the income
    assumption used in the simulation.

    Args:
        monthly_net_income:
            Monthly income selected for the simulation.

        conservative_monthly_income:
            Conservative monthly income calculated from income sources.

        use_conservative_income:
            Whether the conservative income assumption was selected.

    Returns:
        Educational interpretation string.
    """

    if monthly_net_income <= 0:
        return (
            "Risk awareness warning: monthly net income must be greater than "
            "zero for affordability calculations. This is a validation issue, "
            "not a credit decision."
        )

    if use_conservative_income:
        return (
            "The simulation uses a conservative income assumption. This helps "
            "illustrate how affordability may change when income is adjusted "
            "prudently. This is educational only and not a formal banking rule."
        )

    if monthly_net_income < 500:
        return (
            "Risk awareness warning: the monthly income assumption appears "
            "unusually low for this simulation. Please review the fictional or "
            "simulated value."
        )

    if monthly_net_income > 50000:
        return (
            "Risk awareness warning: the monthly income assumption appears "
            "unusually high for this simulation. Please review the fictional or "
            "simulated value."
        )

    return (
        "The selected monthly income assumption is used only for this "
        "educational affordability simulation. It does not represent verified "
        "income, financial advice or a formal credit assessment."
    )


def run_income_simulation(
    income_sources: list[float],
    use_conservative_income: bool = False,
    conservative_factor: float = 0.90,
) -> IncomeResult:
    """
    Run a complete educational income simulation.

    The simulation calculates:

    - total monthly income;
    - conservative monthly income;
    - selected monthly income for the simulation;
    - annual net income estimate;
    - non-decisive educational interpretation.

    Args:
        income_sources:
            List of fictional, simulated or anonymised monthly net income values.

        use_conservative_income:
            If True, the conservative income assumption is used.

        conservative_factor:
            Factor applied to total income when conservative income is used.

    Returns:
        IncomeResult object with the simulation outputs.
    """

    conservative_monthly_income = calculate_conservative_income(
        income_sources=income_sources,
        conservative_factor=conservative_factor,
    )

    monthly_net_income = select_income_for_simulation(
        income_sources=income_sources,
        use_conservative_income=use_conservative_income,
        conservative_factor=conservative_factor,
    )

    annual_net_income = calculate_annual_net_income(
        monthly_net_income=monthly_net_income,
    )

    interpretation = generate_income_interpretation(
        monthly_net_income=monthly_net_income,
        conservative_monthly_income=conservative_monthly_income,
        use_conservative_income=use_conservative_income,
    )

    return IncomeResult(
        monthly_net_income=round(monthly_net_income, 2),
        annual_net_income=round(annual_net_income, 2),
        income_source_count=len(income_sources),
        conservative_monthly_income=round(conservative_monthly_income, 2),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_income_simulation(
        income_sources=[1500, 1000],
        use_conservative_income=True,
        conservative_factor=0.90,
    )

    print(example_result)
