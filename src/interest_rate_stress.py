"""
Interest rate stress testing logic for the DSTI Affordability Calculator.

This module estimates how a simulated monthly loan instalment may change when
the annual interest rate assumption increases.

The logic is educational, explainable and banking-inspired. It is not a credit
approval system, underwriting engine, bank pricing model, financial advisory
tool or replacement for formal human credit analysis.

All values should be fictional, simulated or anonymised.
"""

from dataclasses import dataclass

from loan_payment_calculator import run_loan_payment_simulation


@dataclass
class InterestRateStressResult:
    """
    Stores the outputs of an interest rate stress simulation.

    Attributes:
        loan_amount:
            Simulated loan amount.

        maturity_years:
            Simulated loan maturity in years.

        base_annual_interest_rate_percentage:
            Base annual interest rate assumption.

        stressed_annual_interest_rate_percentage:
            Stressed annual interest rate assumption.

        base_monthly_payment:
            Estimated monthly payment under the base rate assumption.

        stressed_monthly_payment:
            Estimated monthly payment under the stressed rate assumption.

        monthly_payment_increase:
            Difference between stressed and base monthly payment.

        monthly_payment_increase_percentage:
            Percentage increase from base to stressed monthly payment.

        base_total_repayment:
            Estimated total repayment under the base rate assumption.

        stressed_total_repayment:
            Estimated total repayment under the stressed rate assumption.

        total_repayment_increase:
            Difference between stressed and base total repayment.

        interpretation:
            Educational interpretation of the stress test.
    """

    loan_amount: float
    maturity_years: float
    base_annual_interest_rate_percentage: float
    stressed_annual_interest_rate_percentage: float
    base_monthly_payment: float
    stressed_monthly_payment: float
    monthly_payment_increase: float
    monthly_payment_increase_percentage: float
    base_total_repayment: float
    stressed_total_repayment: float
    total_repayment_increase: float
    interpretation: str


def calculate_payment_increase(
    base_monthly_payment: float,
    stressed_monthly_payment: float,
) -> float:
    """
    Calculate the monthly payment increase between base and stressed scenarios.

    Args:
        base_monthly_payment:
            Estimated monthly payment under the base rate assumption.

        stressed_monthly_payment:
            Estimated monthly payment under the stressed rate assumption.

    Returns:
        Difference between stressed and base monthly payment.

    Raises:
        ValueError:
            If either payment is negative.
    """

    if base_monthly_payment < 0:
        raise ValueError("Base monthly payment cannot be negative.")

    if stressed_monthly_payment < 0:
        raise ValueError("Stressed monthly payment cannot be negative.")

    return stressed_monthly_payment - base_monthly_payment


def calculate_payment_increase_percentage(
    base_monthly_payment: float,
    monthly_payment_increase: float,
) -> float:
    """
    Calculate the payment increase as a percentage of the base monthly payment.

    Args:
        base_monthly_payment:
            Estimated monthly payment under the base rate assumption.

        monthly_payment_increase:
            Difference between stressed and base monthly payment.

    Returns:
        Percentage increase from base monthly payment.

    Raises:
        ValueError:
            If base monthly payment is less than or equal to zero.
    """

    if base_monthly_payment <= 0:
        raise ValueError("Base monthly payment must be greater than zero.")

    return (monthly_payment_increase / base_monthly_payment) * 100


def generate_interest_rate_stress_interpretation(
    monthly_payment_increase: float,
    monthly_payment_increase_percentage: float,
    base_annual_interest_rate_percentage: float,
    stressed_annual_interest_rate_percentage: float,
) -> str:
    """
    Generate an educational interpretation of the interest rate stress test.

    Args:
        monthly_payment_increase:
            Difference between stressed and base monthly payment.

        monthly_payment_increase_percentage:
            Percentage increase from base monthly payment.

        base_annual_interest_rate_percentage:
            Base annual interest rate assumption.

        stressed_annual_interest_rate_percentage:
            Stressed annual interest rate assumption.

    Returns:
        Educational, non-decisive interpretation.
    """

    if stressed_annual_interest_rate_percentage < base_annual_interest_rate_percentage:
        return (
            "Data quality warning: the stressed interest rate is lower than the "
            "base interest rate. This may be intentional for scenario analysis, "
            "but should be reviewed before interpreting the result."
        )

    if monthly_payment_increase <= 0:
        return (
            "The stressed scenario does not increase the estimated monthly "
            "payment under the configured assumptions. This should be reviewed "
            "to confirm that the assumptions are coherent."
        )

    if monthly_payment_increase_percentage >= 20:
        return (
            "Risk awareness warning: the stressed interest rate assumption "
            "creates a material increase in the estimated monthly payment. This "
            "may place additional pressure on affordability under the simulated "
            "scenario. This is educational only and not financial advice."
        )

    return (
        "The stressed interest rate assumption increases the estimated monthly "
        "payment compared with the base scenario. This helps illustrate how "
        "interest rate changes may affect affordability. The result is "
        "educational only and is not a bank quote, credit decision or financial "
        "advice."
    )


def run_interest_rate_stress_test(
    loan_amount: float,
    maturity_years: float,
    base_annual_interest_rate_percentage: float,
    stressed_annual_interest_rate_percentage: float,
) -> InterestRateStressResult:
    """
    Run a complete interest rate stress test.

    The simulation estimates:

    - base monthly payment;
    - stressed monthly payment;
    - monthly payment increase;
    - monthly payment increase percentage;
    - base total repayment;
    - stressed total repayment;
    - total repayment increase;
    - educational interpretation.

    Args:
        loan_amount:
            Simulated loan amount.

        maturity_years:
            Simulated loan maturity in years.

        base_annual_interest_rate_percentage:
            Base annual interest rate assumption.

        stressed_annual_interest_rate_percentage:
            Stressed annual interest rate assumption.

    Returns:
        InterestRateStressResult object.
    """

    base_result = run_loan_payment_simulation(
        loan_amount=loan_amount,
        annual_interest_rate_percentage=base_annual_interest_rate_percentage,
        maturity_years=maturity_years,
    )

    stressed_result = run_loan_payment_simulation(
        loan_amount=loan_amount,
        annual_interest_rate_percentage=stressed_annual_interest_rate_percentage,
        maturity_years=maturity_years,
    )

    monthly_payment_increase = calculate_payment_increase(
        base_monthly_payment=base_result.estimated_monthly_payment,
        stressed_monthly_payment=stressed_result.estimated_monthly_payment,
    )

    monthly_payment_increase_percentage = calculate_payment_increase_percentage(
        base_monthly_payment=base_result.estimated_monthly_payment,
        monthly_payment_increase=monthly_payment_increase,
    )

    total_repayment_increase = (
        stressed_result.total_repayment - base_result.total_repayment
    )

    interpretation = generate_interest_rate_stress_interpretation(
        monthly_payment_increase=monthly_payment_increase,
        monthly_payment_increase_percentage=monthly_payment_increase_percentage,
        base_annual_interest_rate_percentage=base_annual_interest_rate_percentage,
        stressed_annual_interest_rate_percentage=stressed_annual_interest_rate_percentage,
    )

    return InterestRateStressResult(
        loan_amount=round(loan_amount, 2),
        maturity_years=round(maturity_years, 2),
        base_annual_interest_rate_percentage=round(
            base_annual_interest_rate_percentage, 2
        ),
        stressed_annual_interest_rate_percentage=round(
            stressed_annual_interest_rate_percentage, 2
        ),
        base_monthly_payment=round(base_result.estimated_monthly_payment, 2),
        stressed_monthly_payment=round(
            stressed_result.estimated_monthly_payment, 2
        ),
        monthly_payment_increase=round(monthly_payment_increase, 2),
        monthly_payment_increase_percentage=round(
            monthly_payment_increase_percentage, 2
        ),
        base_total_repayment=round(base_result.total_repayment, 2),
        stressed_total_repayment=round(stressed_result.total_repayment, 2),
        total_repayment_increase=round(total_repayment_increase, 2),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_interest_rate_stress_test(
        loan_amount=180000,
        maturity_years=30,
        base_annual_interest_rate_percentage=4.0,
        stressed_annual_interest_rate_percentage=5.5,
    )

    print(example_result)
