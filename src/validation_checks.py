"""
Input validation logic for the DSTI Affordability Calculator.

This module validates fictional, simulated or anonymised financial inputs
before DSTI, LTV, maturity or affordability calculations are performed.

The validation layer supports the project's focus on financial data quality,
explainability, financial literacy and responsible financial simulations.

This project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
financial advisory tool or replacement for formal human credit analysis.
"""

from dataclasses import dataclass, field


@dataclass
class ValidationResult:
    """
    Stores validation results for a simulated affordability scenario.

    Attributes:
        is_valid:
            True when there are no blocking errors.

        blocking_errors:
            Issues that prevent the simulation from running safely.

        warnings:
            Non-blocking issues that should be reviewed by the user.

        info_messages:
            Educational or explanatory validation notes.
    """

    is_valid: bool
    blocking_errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    info_messages: list[str] = field(default_factory=list)


def is_missing(value) -> bool:
    """
    Check whether a value is missing.

    Args:
        value:
            Any input value.

    Returns:
        True if the value should be treated as missing.
    """

    return value is None or value == ""


def validate_required_number(
    value,
    field_name: str,
    allow_zero: bool = True,
) -> list[str]:
    """
    Validate whether a required numeric value is present and coherent.

    Args:
        value:
            Input value to validate.

        field_name:
            Human-readable field name used in the validation message.

        allow_zero:
            Whether zero is accepted as a valid value.

    Returns:
        List of blocking error messages.
    """

    errors = []

    if is_missing(value):
        errors.append(f"{field_name} is required.")
        return errors

    try:
        numeric_value = float(value)
    except (TypeError, ValueError):
        errors.append(f"{field_name} must be a valid number.")
        return errors

    if numeric_value < 0:
        errors.append(f"{field_name} cannot be negative.")

    if not allow_zero and numeric_value == 0:
        errors.append(f"{field_name} must be greater than zero.")

    return errors


def validate_percentage(
    value,
    field_name: str,
    minimum: float = 0,
    maximum: float = 100,
) -> list[str]:
    """
    Validate a percentage input.

    Args:
        value:
            Percentage value to validate.

        field_name:
            Human-readable field name.

        minimum:
            Minimum accepted percentage.

        maximum:
            Maximum accepted percentage.

    Returns:
        List of blocking error messages.
    """

    errors = []

    if is_missing(value):
        errors.append(f"{field_name} is required.")
        return errors

    try:
        percentage_value = float(value)
    except (TypeError, ValueError):
        errors.append(f"{field_name} must be a valid percentage.")
        return errors

    if percentage_value < minimum or percentage_value > maximum:
        errors.append(
            f"{field_name} must be between {minimum}% and {maximum}%."
        )

    return errors


def validate_income_reasonableness(monthly_net_income: float) -> list[str]:
    """
    Generate non-blocking warnings for unusual income assumptions.

    These checks are educational data quality alerts only.

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

    Returns:
        List of warning messages.
    """

    warnings = []

    if monthly_net_income < 500:
        warnings.append(
            "Monthly net income appears unusually low for this simulation. "
            "Please confirm that the value is fictional or simulated."
        )

    if monthly_net_income > 50000:
        warnings.append(
            "Monthly net income appears unusually high for this simulation. "
            "Please confirm that the value is fictional or simulated."
        )

    return warnings


def validate_commitments_reasonableness(
    monthly_net_income: float,
    existing_monthly_commitments: float,
) -> list[str]:
    """
    Generate warnings for unusually high existing commitments.

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        existing_monthly_commitments:
            Existing monthly credit commitments.

    Returns:
        List of warning messages.
    """

    warnings = []

    if monthly_net_income > 0:
        commitments_ratio = existing_monthly_commitments / monthly_net_income

        if commitments_ratio > 1:
            warnings.append(
                "Existing monthly commitments are higher than monthly net "
                "income. Please review the simulated values."
            )
        elif commitments_ratio > 0.70:
            warnings.append(
                "Existing monthly commitments appear high relative to monthly "
                "net income."
            )

    return warnings


def validate_instalment_reasonableness(
    monthly_net_income: float,
    proposed_monthly_instalment: float,
    stressed_monthly_instalment: float,
) -> list[str]:
    """
    Generate warnings for proposed and stressed instalment assumptions.

    Args:
        monthly_net_income:
            Monthly net income used in the simulation.

        proposed_monthly_instalment:
            Proposed monthly instalment.

        stressed_monthly_instalment:
            Stressed monthly instalment.

    Returns:
        List of warning messages.
    """

    warnings = []

    if monthly_net_income > 0:
        proposed_ratio = proposed_monthly_instalment / monthly_net_income

        if proposed_ratio > 1:
            warnings.append(
                "The proposed monthly instalment is higher than monthly net "
                "income. Please review the simulated values."
            )
        elif proposed_ratio > 0.60:
            warnings.append(
                "The proposed monthly instalment appears high relative to "
                "monthly net income."
            )

    if stressed_monthly_instalment < proposed_monthly_instalment:
        warnings.append(
            "The stressed instalment is lower than the proposed instalment. "
            "Please confirm this assumption."
        )

    return warnings


def validate_ltv_inputs(
    loan_amount: float | None = None,
    property_value: float | None = None,
) -> tuple[list[str], list[str]]:
    """
    Validate optional LTV inputs.

    Args:
        loan_amount:
            Simulated loan amount.

        property_value:
            Property value used for LTV simulation.

    Returns:
        Tuple containing blocking errors and warnings.
    """

    errors = []
    warnings = []

    ltv_requested = not is_missing(loan_amount) or not is_missing(property_value)

    if not ltv_requested:
        return errors, warnings

    errors.extend(
        validate_required_number(
            loan_amount,
            "Loan amount",
            allow_zero=False,
        )
    )

    errors.extend(
        validate_required_number(
            property_value,
            "Property value",
            allow_zero=False,
        )
    )

    if errors:
        return errors, warnings

    loan_amount = float(loan_amount)
    property_value = float(property_value)

    ltv_percentage = (loan_amount / property_value) * 100

    if ltv_percentage > 100:
        warnings.append(
            "The simulated LTV is above 100%. This is a risk awareness flag "
            "only and not a credit decision."
        )

    if ltv_percentage > 120:
        warnings.append(
            "The simulated LTV appears unusually high. Please review the loan "
            "amount and property value assumptions."
        )

    return errors, warnings


def validate_maturity_inputs(
    loan_maturity_years: float | None = None,
    current_age: float | None = None,
) -> tuple[list[str], list[str]]:
    """
    Validate optional maturity and age assumptions.

    Args:
        loan_maturity_years:
            Simulated loan maturity in years.

        current_age:
            Fictional or anonymised current age.

    Returns:
        Tuple containing blocking errors and warnings.
    """

    errors = []
    warnings = []

    maturity_requested = (
        not is_missing(loan_maturity_years)
        or not is_missing(current_age)
    )

    if not maturity_requested:
        return errors, warnings

    errors.extend(
        validate_required_number(
            loan_maturity_years,
            "Loan maturity in years",
            allow_zero=False,
        )
    )

    errors.extend(
        validate_required_number(
            current_age,
            "Current age",
            allow_zero=False,
        )
    )

    if errors:
        return errors, warnings

    loan_maturity_years = float(loan_maturity_years)
    current_age = float(current_age)

    if loan_maturity_years > 50:
        warnings.append(
            "Loan maturity appears unusually long for this simulation."
        )

    if current_age < 18:
        warnings.append(
            "Current age appears below the expected range for this simulation."
        )

    if current_age > 100:
        warnings.append(
            "Current age appears unusually high for this simulation."
        )

    age_at_end_of_loan = current_age + loan_maturity_years

    if age_at_end_of_loan > 75:
        warnings.append(
            "The simulated age at the end of the loan appears high. This is a "
            "risk awareness flag only."
        )

    return errors, warnings


def validate_dsti_outputs(
    base_dsti_percentage: float | None = None,
    stressed_dsti_percentage: float | None = None,
) -> list[str]:
    """
    Generate warnings for unusual DSTI outputs.

    Args:
        base_dsti_percentage:
            Base DSTI calculated by the simulation.

        stressed_dsti_percentage:
            Stressed DSTI calculated by the simulation.

    Returns:
        List of warning messages.
    """

    warnings = []

    if base_dsti_percentage is not None:
        if base_dsti_percentage > 100:
            warnings.append(
                "Base DSTI is above 100%, meaning simulated debt payments are "
                "higher than monthly net income."
            )
        elif base_dsti_percentage > 50:
            warnings.append(
                "Base DSTI appears high. This is an educational risk "
                "awareness warning only."
            )

    if stressed_dsti_percentage is not None:
        if stressed_dsti_percentage > 100:
            warnings.append(
                "Stressed DSTI is above 100%, meaning simulated stressed debt "
                "payments are higher than monthly net income."
            )
        elif stressed_dsti_percentage > 60:
            warnings.append(
                "Stressed DSTI appears high. This is an educational risk "
                "awareness warning only."
            )

    return warnings


def validate_affordability_inputs(
    monthly_net_income,
    existing_monthly_commitments,
    proposed_monthly_instalment,
    stressed_monthly_instalment,
    configured_dsti_threshold_percentage,
    loan_amount=None,
    property_value=None,
    loan_maturity_years=None,
    current_age=None,
) -> ValidationResult:
    """
    Validate a complete fictional affordability simulation scenario.

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

        loan_amount:
            Optional simulated loan amount for LTV calculation.

        property_value:
            Optional property value for LTV calculation.

        loan_maturity_years:
            Optional simulated loan maturity in years.

        current_age:
            Optional fictional or anonymised current age.

    Returns:
        ValidationResult object.
    """

    blocking_errors = []
    warnings = []
    info_messages = [
        "This project is educational and uses fictional, simulated or "
        "anonymised values only.",
        "Validation warnings are not credit decisions, eligibility checks or "
        "financial advice.",
    ]

    blocking_errors.extend(
        validate_required_number(
            monthly_net_income,
            "Monthly net income",
            allow_zero=False,
        )
    )

    blocking_errors.extend(
        validate_required_number(
            existing_monthly_commitments,
            "Existing monthly commitments",
            allow_zero=True,
        )
    )

    blocking_errors.extend(
        validate_required_number(
            proposed_monthly_instalment,
            "Proposed monthly instalment",
            allow_zero=True,
        )
    )

    blocking_errors.extend(
        validate_required_number(
            stressed_monthly_instalment,
            "Stressed monthly instalment",
            allow_zero=True,
        )
    )

    blocking_errors.extend(
        validate_percentage(
            configured_dsti_threshold_percentage,
            "Configured DSTI threshold",
            minimum=0,
            maximum=100,
        )
    )

    ltv_errors, ltv_warnings = validate_ltv_inputs(
        loan_amount=loan_amount,
        property_value=property_value,
    )
    blocking_errors.extend(ltv_errors)
    warnings.extend(ltv_warnings)

    maturity_errors, maturity_warnings = validate_maturity_inputs(
        loan_maturity_years=loan_maturity_years,
        current_age=current_age,
    )
    blocking_errors.extend(maturity_errors)
    warnings.extend(maturity_warnings)

    if blocking_errors:
        return ValidationResult(
            is_valid=False,
            blocking_errors=blocking_errors,
            warnings=warnings,
            info_messages=info_messages,
        )

    monthly_net_income = float(monthly_net_income)
    existing_monthly_commitments = float(existing_monthly_commitments)
    proposed_monthly_instalment = float(proposed_monthly_instalment)
    stressed_monthly_instalment = float(stressed_monthly_instalment)

    warnings.extend(
        validate_income_reasonableness(
            monthly_net_income=monthly_net_income,
        )
    )

    warnings.extend(
        validate_commitments_reasonableness(
            monthly_net_income=monthly_net_income,
            existing_monthly_commitments=existing_monthly_commitments,
        )
    )

    warnings.extend(
        validate_instalment_reasonableness(
            monthly_net_income=monthly_net_income,
            proposed_monthly_instalment=proposed_monthly_instalment,
            stressed_monthly_instalment=stressed_monthly_instalment,
        )
    )

    return ValidationResult(
        is_valid=True,
        blocking_errors=blocking_errors,
        warnings=warnings,
        info_messages=info_messages,
    )


if __name__ == "__main__":
    example_validation = validate_affordability_inputs(
        monthly_net_income=2500,
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        loan_amount=180000,
        property_value=215000,
        loan_maturity_years=30,
        current_age=35,
    )

    print(example_validation)
