"""
Scenario analysis engine for the DSTI Affordability Calculator.

This module combines income, DSTI, LTV and maturity simulation outputs into
structured affordability scenarios.

The purpose is educational, demonstrative and portfolio-oriented.

This module must not be interpreted as a credit approval system, underwriting
engine, financial advisory tool or replacement for formal human credit analysis.

All examples, inputs and outputs should use fictional, simulated or anonymised
data only.
"""

from dataclasses import dataclass

from dsti_calculator import DSTIResult, run_dsti_simulation
from income_calculator import IncomeResult, run_income_simulation
from ltv_calculator import LTVResult, run_ltv_simulation
from maturity_validator import MaturityResult, run_maturity_simulation
from validation_checks import ValidationResult, validate_affordability_inputs


@dataclass
class ScenarioResult:
    """
    Stores a complete simulated affordability scenario.

    Attributes:
        scenario_name:
            Name of the simulated scenario.

        validation:
            ValidationResult object with blocking errors, warnings and notes.

        income:
            IncomeResult object with income assumptions.

        dsti:
            DSTIResult object with DSTI simulation outputs.

        ltv:
            Optional LTVResult object with LTV simulation outputs.

        maturity:
            Optional MaturityResult object with maturity simulation outputs.

        summary:
            Educational, non-decisive scenario summary.
    """

    scenario_name: str
    validation: ValidationResult
    income: IncomeResult | None
    dsti: DSTIResult | None
    ltv: LTVResult | None
    maturity: MaturityResult | None
    summary: str


def generate_scenario_summary(
    scenario_name: str,
    validation: ValidationResult,
    dsti: DSTIResult | None = None,
    ltv: LTVResult | None = None,
    maturity: MaturityResult | None = None,
) -> str:
    """
    Generate a clear and non-decisive summary for a simulated scenario.

    The wording intentionally avoids approval/rejection language.

    Args:
        scenario_name:
            Name of the scenario.

        validation:
            ValidationResult object.

        dsti:
            Optional DSTIResult object.

        ltv:
            Optional LTVResult object.

        maturity:
            Optional MaturityResult object.

    Returns:
        Educational scenario summary.
    """

    if not validation.is_valid:
        return (
            f"The scenario '{scenario_name}' contains blocking validation "
            "issues. The simulation should not be interpreted until the input "
            "assumptions are corrected. This is a data quality outcome, not a "
            "credit decision."
        )

    warning_count = len(validation.warnings)

    summary_parts = [
        f"The scenario '{scenario_name}' was processed using fictional, "
        "simulated or anonymised values.",
        "The output is educational and must not be interpreted as credit "
        "approval, rejection, eligibility confirmation or financial advice.",
    ]

    if dsti is not None:
        summary_parts.append(
            f"Base DSTI: {dsti.base_dsti_percentage}%. "
            f"Stressed DSTI: {dsti.stressed_dsti_percentage}%."
        )

        summary_parts.append(dsti.interpretation)

    if ltv is not None:
        summary_parts.append(
            f"Simulated LTV: {ltv.ltv_percentage}% using a property value "
            f"assumption of €{ltv.property_value_used:,.2f}."
        )

        summary_parts.append(ltv.interpretation)

    if maturity is not None:
        summary_parts.append(
            f"Simulated age at the end of the loan: "
            f"{maturity.age_at_end_of_loan}."
        )

        summary_parts.append(maturity.interpretation)

    if warning_count > 0:
        summary_parts.append(
            f"The validation layer identified {warning_count} warning(s). "
            "These warnings should be reviewed as part of prudent financial "
            "simulation, but they are not lending decisions."
        )
    else:
        summary_parts.append(
            "No non-blocking validation warnings were identified in this "
            "simulation."
        )

    return " ".join(summary_parts)


def run_affordability_scenario(
    scenario_name: str,
    income_sources: list[float],
    existing_monthly_commitments: float,
    proposed_monthly_instalment: float,
    stressed_monthly_instalment: float,
    configured_dsti_threshold_percentage: float,
    use_conservative_income: bool = False,
    conservative_factor: float = 0.90,
    loan_amount: float | None = None,
    acquisition_value: float | None = None,
    valuation_value: float | None = None,
    configured_ltv_threshold_percentage: float | None = None,
    use_lower_property_value: bool = True,
    loan_maturity_years: float | None = None,
    current_age: float | None = None,
    configured_maximum_age_at_end: float = 75,
) -> ScenarioResult:
    """
    Run a complete educational affordability scenario.

    This function:

    - calculates income assumptions;
    - validates input data;
    - calculates DSTI outputs;
    - optionally calculates LTV outputs;
    - optionally calculates maturity outputs;
    - generates an educational scenario summary.

    Args:
        scenario_name:
            Name of the simulated scenario.

        income_sources:
            List of fictional, simulated or anonymised monthly income sources.

        existing_monthly_commitments:
            Existing monthly credit commitments.

        proposed_monthly_instalment:
            Proposed monthly instalment.

        stressed_monthly_instalment:
            Stressed monthly instalment.

        configured_dsti_threshold_percentage:
            Configured DSTI threshold used for the simulation.

        use_conservative_income:
            Whether to use the conservative income assumption.

        conservative_factor:
            Conservative factor applied to income.

        loan_amount:
            Optional simulated loan amount for LTV calculation.

        acquisition_value:
            Optional simulated acquisition value.

        valuation_value:
            Optional simulated valuation value.

        configured_ltv_threshold_percentage:
            Optional configured LTV threshold.

        use_lower_property_value:
            Whether to use the lower of acquisition and valuation value.

        loan_maturity_years:
            Optional simulated loan maturity.

        current_age:
            Optional fictional or anonymised age.

        configured_maximum_age_at_end:
            Configured maximum age assumption for maturity simulation.

    Returns:
        ScenarioResult object.
    """

    income = run_income_simulation(
        income_sources=income_sources,
        use_conservative_income=use_conservative_income,
        conservative_factor=conservative_factor,
    )

    property_value_for_validation = None

    if acquisition_value is not None and valuation_value is not None:
        property_value_for_validation = (
            min(acquisition_value, valuation_value)
            if use_lower_property_value
            else valuation_value
        )
    elif acquisition_value is not None:
        property_value_for_validation = acquisition_value
    elif valuation_value is not None:
        property_value_for_validation = valuation_value

    validation = validate_affordability_inputs(
        monthly_net_income=income.monthly_net_income,
        existing_monthly_commitments=existing_monthly_commitments,
        proposed_monthly_instalment=proposed_monthly_instalment,
        stressed_monthly_instalment=stressed_monthly_instalment,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
        loan_amount=loan_amount,
        property_value=property_value_for_validation,
        loan_maturity_years=loan_maturity_years,
        current_age=current_age,
    )

    if not validation.is_valid:
        summary = generate_scenario_summary(
            scenario_name=scenario_name,
            validation=validation,
        )

        return ScenarioResult(
            scenario_name=scenario_name,
            validation=validation,
            income=income,
            dsti=None,
            ltv=None,
            maturity=None,
            summary=summary,
        )

    dsti = run_dsti_simulation(
        monthly_net_income=income.monthly_net_income,
        existing_monthly_commitments=existing_monthly_commitments,
        proposed_monthly_instalment=proposed_monthly_instalment,
        stressed_monthly_instalment=stressed_monthly_instalment,
        configured_dsti_threshold_percentage=configured_dsti_threshold_percentage,
    )

    ltv = None
    if loan_amount is not None and (
        acquisition_value is not None or valuation_value is not None
    ):
        ltv = run_ltv_simulation(
            loan_amount=loan_amount,
            acquisition_value=acquisition_value,
            valuation_value=valuation_value,
            configured_ltv_threshold_percentage=configured_ltv_threshold_percentage,
            use_lower_value=use_lower_property_value,
        )

    maturity = None
    if loan_maturity_years is not None and current_age is not None:
        maturity = run_maturity_simulation(
            current_age=current_age,
            loan_maturity_years=loan_maturity_years,
            configured_maximum_age_at_end=configured_maximum_age_at_end,
        )

    validation.warnings.extend(
        []
    )

    summary = generate_scenario_summary(
        scenario_name=scenario_name,
        validation=validation,
        dsti=dsti,
        ltv=ltv,
        maturity=maturity,
    )

    return ScenarioResult(
        scenario_name=scenario_name,
        validation=validation,
        income=income,
        dsti=dsti,
        ltv=ltv,
        maturity=maturity,
        summary=summary,
    )


def compare_scenarios(scenarios: list[ScenarioResult]) -> list[dict]:
    """
    Convert multiple scenario results into a simple comparison table structure.

    Args:
        scenarios:
            List of ScenarioResult objects.

    Returns:
        List of dictionaries suitable for pandas DataFrame creation.
    """

    comparison_rows = []

    for scenario in scenarios:
        comparison_rows.append(
            {
                "scenario_name": scenario.scenario_name,
                "validation_status": "valid"
                if scenario.validation.is_valid
                else "invalid",
                "warning_count": len(scenario.validation.warnings),
                "base_dsti_percentage": scenario.dsti.base_dsti_percentage
                if scenario.dsti
                else None,
                "stressed_dsti_percentage": scenario.dsti.stressed_dsti_percentage
                if scenario.dsti
                else None,
                "remaining_repayment_capacity": (
                    scenario.dsti.remaining_repayment_capacity
                    if scenario.dsti
                    else None
                ),
                "margin_against_stressed_instalment": (
                    scenario.dsti.margin_against_stressed_instalment
                    if scenario.dsti
                    else None
                ),
                "ltv_percentage": scenario.ltv.ltv_percentage
                if scenario.ltv
                else None,
                "age_at_end_of_loan": scenario.maturity.age_at_end_of_loan
                if scenario.maturity
                else None,
            }
        )

    return comparison_rows


if __name__ == "__main__":
    base_scenario = run_affordability_scenario(
        scenario_name="Base scenario",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=False,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    prudent_scenario = run_affordability_scenario(
        scenario_name="Prudent income scenario",
        income_sources=[1500, 1000],
        existing_monthly_commitments=300,
        proposed_monthly_instalment=650,
        stressed_monthly_instalment=780,
        configured_dsti_threshold_percentage=40,
        use_conservative_income=True,
        conservative_factor=0.90,
        loan_amount=180000,
        acquisition_value=220000,
        valuation_value=215000,
        configured_ltv_threshold_percentage=90,
        loan_maturity_years=30,
        current_age=35,
    )

    print(base_scenario.summary)
    print(prudent_scenario.summary)
    print(compare_scenarios([base_scenario, prudent_scenario]))
