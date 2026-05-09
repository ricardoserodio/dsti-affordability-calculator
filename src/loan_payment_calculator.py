"""
Loan payment calculation logic for the DSTI Affordability Calculator.

This module contains simplified, explainable and educational calculations for
estimating monthly loan instalments based on loan amount, annual interest rate
and maturity.

The logic is banking-inspired, but it is not a credit approval system,
underwriting engine, financial advisory tool or replacement for formal human
credit analysis.

All values should be fictional, simulated or anonymised.

The calculated instalment is an educational estimate only. It is not a bank
quote, offer, approval indication or financial advice.
"""

from dataclasses import dataclass


@dataclass
class LoanPaymentResult:
    """
    Stores the main loan payment simulation outputs.

    Attributes:
        loan_amount:
            Simulated loan amount.

        annual_interest_rate_percentage:
            Annual interest rate assumption used in the simulation.

        maturity_years:
            Simulated loan maturity in years.

        maturity_months:
            Simulated loan maturity in months.

        estimated_monthly_payment:
            Estimated monthly instalment using a simplified amortising loan
            formula.

        total_repayment:
            Estimated total amount repaid over the simulated maturity.

        total_interest:
            Estimated total interest paid over the simulated maturity.

        interpretation:
            Educational interpretation of the simulated loan payment result.
    """

    loan_amount: float
    annual_interest_rate_percentage: float
    maturity_years: float
    maturity_months: int
    estimated_monthly_payment: float
    total_repayment: float
    total_interest: float
    interpretation: str


def calculate_monthly_payment(
    loan_amount: float,
    annual_interest_rate_percentage: float,
    maturity_years: float,
) -> float:
    """
    Calculate an estimated monthly payment using a simplified amortising loan
    formula.

    Formula:
        Monthly Payment =
        P × r × (1 + r)^n / ((1 + r)^n - 1)

    Where:
        P = loan amount
        r = monthly interest rate
        n = number of monthly payments

    Args:
        loan_amount:
            Simulated loan amount.

        annual_interest_rate_percentage:
            Annual interest rate assumption expressed as a percentage.

        maturity_years:
            Simulated loan maturity in years.

    Returns:
        Estimated monthly payment.

    Raises:
        ValueError:
            If loan amount is less than or equal to zero.
            If maturity is less than or equal to zero.
            If interest rate is negative.
    """

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if maturity_years <= 0:
        raise ValueError("Loan maturity must be greater than zero.")

    if annual_interest_rate_percentage < 0:
        raise ValueError("Annual interest rate cannot be negative.")

    maturity_months = int(maturity_years * 12)

    if maturity_months <= 0:
        raise ValueError("Loan maturity must result in at least one monthly payment.")

    if annual_interest_rate_percentage == 0:
        return loan_amount / maturity_months

    monthly_interest_rate = annual_interest_rate_percentage / 100 / 12

    monthly_payment = (
        loan_amount
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** maturity_months
        / ((1 + monthly_interest_rate) ** maturity_months - 1)
    )

    return monthly_payment


def calculate_total_repayment(
    monthly_payment: float,
    maturity_years: float,
) -> float:
    """
    Calculate the estimated total repayment over the simulated maturity.

    Args:
        monthly_payment:
            Estimated monthly payment.

        maturity_years:
            Simulated loan maturity in years.

    Returns:
        Estimated total repayment.

    Raises:
        ValueError:
            If monthly payment is negative.
            If maturity is less than or equal to zero.
    """

    if monthly_payment < 0:
        raise ValueError("Monthly payment cannot be negative.")

    if maturity_years <= 0:
        raise ValueError("Loan maturity must be greater than zero.")

    maturity_months = int(maturity_years * 12)

    return monthly_payment * maturity_months


def calculate_total_interest(
    total_repayment: float,
    loan_amount: float,
) -> float:
    """
    Calculate estimated total interest paid over the simulated maturity.

    Args:
        total_repayment:
            Estimated total repayment.

        loan_amount:
            Simulated loan amount.

    Returns:
        Estimated total interest.

    Raises:
        ValueError:
            If total repayment is negative.
            If loan amount is less than or equal to zero.
    """

    if total_repayment < 0:
        raise ValueError("Total repayment cannot be negative.")

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    return total_repayment - loan_amount


def generate_loan_payment_interpretation(
    estimated_monthly_payment: float,
    annual_interest_rate_percentage: float,
    maturity_years: float,
) -> str:
    """
    Generate an educational and non-decisive interpretation of the estimated
    monthly payment.

    Args:
        estimated_monthly_payment:
            Estimated monthly instalment.

        annual_interest_rate_percentage:
            Annual interest rate assumption used in the simulation.

        maturity_years:
            Simulated loan maturity in years.

    Returns:
        Educational interpretation string.
    """

    if annual_interest_rate_percentage > 10:
        return (
            "Risk awareness warning: the annual interest rate assumption appears "
            "high for this educational simulation. The estimated instalment may "
            "place greater pressure on affordability. This is not financial "
            "advice or a credit decision."
        )

    if maturity_years > 40:
        return (
            "Risk awareness warning: the maturity assumption appears long. A "
            "longer maturity may reduce the monthly instalment but can increase "
            "the estimated total repayment over time. This is educational only."
        )

    return (
        "The estimated monthly payment is calculated using simplified loan "
        "amortisation assumptions. It is an educational estimate only and must "
        "not be interpreted as a bank quote, offer, credit approval or financial "
        "advice."
    )


def run_loan_payment_simulation(
    loan_amount: float,
    annual_interest_rate_percentage: float,
    maturity_years: float,
) -> LoanPaymentResult:
    """
    Run a complete educational loan payment simulation.

    The simulation calculates:

    - estimated monthly payment;
    - total repayment;
    - estimated total interest;
    - non-decisive educational interpretation.

    Args:
        loan_amount:
            Simulated loan amount.

        annual_interest_rate_percentage:
            Annual interest rate assumption expressed as a percentage.

        maturity_years:
            Simulated loan maturity in years.

    Returns:
        LoanPaymentResult object with the simulation outputs.
    """

    estimated_monthly_payment = calculate_monthly_payment(
        loan_amount=loan_amount,
        annual_interest_rate_percentage=annual_interest_rate_percentage,
        maturity_years=maturity_years,
    )

    total_repayment = calculate_total_repayment(
        monthly_payment=estimated_monthly_payment,
        maturity_years=maturity_years,
    )

    total_interest = calculate_total_interest(
        total_repayment=total_repayment,
        loan_amount=loan_amount,
    )

    interpretation = generate_loan_payment_interpretation(
        estimated_monthly_payment=estimated_monthly_payment,
        annual_interest_rate_percentage=annual_interest_rate_percentage,
        maturity_years=maturity_years,
    )

    return LoanPaymentResult(
        loan_amount=round(loan_amount, 2),
        annual_interest_rate_percentage=round(annual_interest_rate_percentage, 2),
        maturity_years=round(maturity_years, 2),
        maturity_months=int(maturity_years * 12),
        estimated_monthly_payment=round(estimated_monthly_payment, 2),
        total_repayment=round(total_repayment, 2),
        total_interest=round(total_interest, 2),
        interpretation=interpretation,
    )


if __name__ == "__main__":
    example_result = run_loan_payment_simulation(
        loan_amount=180000,
        annual_interest_rate_percentage=4.0,
        maturity_years=30,
    )

    print(example_result)
