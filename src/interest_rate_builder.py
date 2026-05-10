"""
Interest rate builder logic for the DSTI Affordability Calculator.

This module builds simulated annual interest rate assumptions using:

- simulated EURIBOR;
- simulated spread;
- optional stress buffer.

The purpose is educational and demonstrative only.

This module does not fetch live market data, provide bank pricing, produce a
loan offer, approve credit or provide financial advice.

All values should be fictional, simulated, manually entered or anonymised.
"""

from dataclasses import dataclass


@dataclass
class InterestRateBuildResult:
    """
    Stores the simulated interest rate build outputs.

    Attributes:
        simulated_euribor_percentage:
            Simulated EURIBOR assumption.

        simulated_spread_percentage:
            Simulated spread assumption.

        stress_buffer_percentage:
            Additional interest rate stress buffer.

        base_annual_interest_rate_percentage:
            Simulated base annual interest rate calculated as EURIBOR + spread.

        stressed_annual_interest_rate_percentage:
            Simulated stressed annual interest rate calculated as base rate
            plus stress buffer.

        interpretation:
            Educational explanation of the simulated interest rate build.
    """

    simulated_euribor_percentage: float
    simulated_spread_percentage: float
    stress_buffer_percentage: float
    base_annual_interest_rate_percentage: float
    stressed_annual_interest_rate_percentage: float
    interpretation: str


def calculate_base_annual_interest_rate(
    simulated_euribor_percentage: float,
    simulated_spread_percentage: float,
) -> float:
    """
    Calculate the simulated base annual interest rate.

    Formula:
        Base Annual Interest Rate = Simulated EURIBOR + Simulated Spread

    Args:
        simulated_euribor_percentage:
            Simulated EURIBOR assumption.

        simulated_spread_percentage:
            Simulated spread assumption.

    Returns:
        Simulated base annual interest rate.

    Raises:
        ValueError:
            If the spread is negative.
    """

    if simulated_spread_percentage < 0:
        raise ValueError("Simulated spread cannot be negative.")

    return simulated_euribor_percentage + simulated_spread_percentage


def calculate_stressed_annual_interest_rate(
    base_annual_interest_rate_percentage: float,
    stress_buffer_percentage: float,
) -> float:
    """
    Calculate the simulated stressed annual interest rate.

    Formula:
        Stressed Annual Interest Rate = Base Annual Interest Rate + Stress Buffer

    Args:
        base_annual_interest_rate_percentage:
            Simulated base annual interest rate.

        stress_buffer_percentage:
            Additional stress buffer assumption.

    Returns:
        Simulated stressed annual interest rate.

    Raises:
        ValueError:
            If the stress buffer is negative.
    """

    if stress_buffer_percentage < 0:
        raise ValueError("Stress buffer cannot be negative.")

    return base_annual_interest_rate_percentage + stress_buffer_percentage


def generate_interest_rate_build_interpretation(
    simulated_euribor_percentage: float,
    simulated_spread_percentage: float,
    stress_buffer_percentage: float,
    base_annual_interest_rate_percentage: float,
    stressed_annual_interest_rate_percentage: float,
) -> str:
    """
    Generate an educational interpretation of the simulated interest rate build.

    Args:
        simulated_euribor_percentage:
            Simulated EURIBOR assumption.

        simulated_spread_percentage:
            Simulated spread assumption.

        stress_buffer_percentage:
            Additional stress buffer assumption.

        base_annual_interest_rate_percentage:
            Simulated base annual interest rate.

        stressed_annual_interest_rate_percentage:
            Simulated stressed annual interest rate.

    Returns:
        Educational interpretation string.
    """

    if simulated_euribor_percentage < 0:
        return (
            "Data quality note: the simulated EURIBOR assumption is negative. "
            "This may be intentional for scenario analysis, but should be "
            "reviewed before interpreting the output. The result is educational "
            "only and not financial advice."
        )

    if base_annual_interest_rate_percentage > 10:
        return (
            "Risk awareness warning: the simulated base annual interest rate "
            "appears high. This may create significant affordability pressure "
            "in the DSTI simulation. The result is educational only and not a "
            "bank quote, credit decision or financial advice."
        )

    if stress_buffer_percentage == 0:
        return (
            "The simulated stressed annual interest rate is equal to the base "
            "annual interest rate because no stress buffer was applied. This may "
            "be useful for a base scenario, but a separate stressed scenario can "
            "help demonstrate interest rate sensitivity."
        )

    return (
        "The simulated base annual interest rate was calculated by adding the "
        "simulated EURIBOR and simulated spread. The stressed annual interest "
        "rate then adds a stress buffer to illustrate how affordability may "
        "change under less favourable interest rate assumptions. This is "
        "educational only and not a bank quote, credit decision or financial "
        "advice."
    )


def build_interest_rate_assumptions(
    simulated_euribor_percentage: float,
    simulated_spread_percentage: float,
    stress_buffer_percentage: float,
) -> InterestRateBuildResult:
    """
    Build simulated base and stressed annual interest rate assumptions.

    Args:
        simulated_euribor_percentage:
            Simulated EURIBOR assumption.

        simulated_spread_percentage:
            Simulated spread assumption.

        stress_buffer_percentage:
            Additional stress buffer assumption.

    Returns:
        InterestRateBuildResult object.
    """

    base_annual_interest_rate_percentage = calculate_base_annual_interest_rate(
        simulated_euribor_percentage=simulated_euribor_percentage,
        simulated_spread_percentage=simulated_spread_percentage,
    )

    stressed_annual_interest_rate_percentage = calculate_stressed_annual_interest_rate(
        base_annual_interest_rate_percentage=base_annual_interest_rate_percentage,
        stress_buffer_percentage=stress_buffer_percentage,
    )

    interpretation = generate_interest_rate_build_interpretation(
        simulated_euribor_percentage=simulated_euribor_percentage,
        simulated_spread_percentage=simulated_spread_percentage,
        stress_buffer_percentage=stress_buffer_percentage,
        base_annual_interest_rate_percentage=base_annual_interest_rate_percentage,
        stressed_annual_interest_rate_percentage=stressed_annual_interest_rate_percentage,
    )

    return InterestRateBuildResult(
        simulated_euribor_percentage=round(simulated_euribor_percentage, 2),
        simulated_spread_percentage=round(simulated_spread_percentage, 2),
        stress_buffer_percentage=round(stress_buffer_percentage, 2),
        base_annual_interest_rate_percentage=round(
            base_annual_interest_rate_percentage, 2
        ),
        stressed_annual_interest_rate_percentage=round(
            stressed_annual_interest_rate_percentage, 2
        ),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = build_interest_rate_assumptions(
        simulated_euribor_percentage=3.0,
        simulated_spread_percentage=0.9,
        stress_buffer_percentage=1.5,
    )

    print(example_result)
