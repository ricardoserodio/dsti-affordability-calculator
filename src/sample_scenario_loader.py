"""
Sample scenario loader for the DSTI Affordability Calculator.

This module loads fictional sample scenarios from examples/sample_scenarios.csv.

The purpose is educational, demonstrative and portfolio-oriented.
It does not load real client data, personal financial information or bank
confidential information.

All sample scenarios should remain fictional, simulated or anonymised.
"""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


REQUIRED_SAMPLE_SCENARIO_COLUMNS = {
    "scenario_name",
    "income_source_1",
    "income_source_2",
    "use_conservative_income",
    "conservative_factor",
    "housing_commitment",
    "auto_loan_commitment",
    "personal_loan_commitment",
    "credit_card_commitment",
    "other_credit_commitments",
    "existing_monthly_commitments",
    "loan_amount",
    "loan_maturity_years",
    "euribor_tenor",
    "simulated_euribor_percentage",
    "simulated_spread_percentage",
    "stress_buffer_percentage",
    "acquisition_value",
    "valuation_value",
    "configured_dsti_threshold_percentage",
    "configured_ltv_threshold_percentage",
    "current_age",
    "configured_maximum_age_at_end",
    "scenario_note",
}


STRUCTURED_COMMITMENT_COLUMNS = {
    "housing_commitment",
    "auto_loan_commitment",
    "personal_loan_commitment",
    "credit_card_commitment",
    "other_credit_commitments",
}


@dataclass
class SampleScenarioValidationResult:
    """
    Stores validation results for the sample scenario dataset.

    Attributes:
        is_valid:
            Indicates whether the sample scenario dataset passed validation.

        missing_columns:
            Required columns missing from the dataset.

        row_count:
            Number of rows in the dataset.

        interpretation:
            Educational interpretation of the validation result.
    """

    is_valid: bool
    missing_columns: list[str]
    row_count: int
    interpretation: str


def get_default_sample_scenarios_path() -> Path:
    """
    Return the default path for the sample scenarios CSV file.
    """

    project_root = Path(__file__).resolve().parents[1]
    return project_root / "examples" / "sample_scenarios.csv"


def load_sample_scenarios(file_path: str | Path | None = None) -> pd.DataFrame:
    """
    Load the sample scenarios CSV file.

    Args:
        file_path:
            Optional custom CSV path. If not provided, the default examples
            folder path is used.

    Returns:
        pandas DataFrame containing sample scenarios.

    Raises:
        FileNotFoundError:
            If the sample scenario file does not exist.
    """

    scenario_path = (
        Path(file_path)
        if file_path is not None
        else get_default_sample_scenarios_path()
    )

    if not scenario_path.exists():
        raise FileNotFoundError(f"Sample scenarios file not found: {scenario_path}")

    return pd.read_csv(scenario_path)


def validate_sample_scenarios_columns(
    sample_scenarios: pd.DataFrame,
) -> SampleScenarioValidationResult:
    """
    Validate whether the sample scenarios dataset contains the required columns.

    Args:
        sample_scenarios:
            DataFrame containing sample scenario rows.

    Returns:
        SampleScenarioValidationResult object.
    """

    available_columns = set(sample_scenarios.columns)
    missing_columns = sorted(REQUIRED_SAMPLE_SCENARIO_COLUMNS - available_columns)

    is_valid = len(missing_columns) == 0
    row_count = len(sample_scenarios)

    if not is_valid:
        interpretation = (
            "Data quality warning: the sample scenario dataset is missing "
            "required columns. Review the CSV structure before using it in the "
            "application or documentation."
        )
    elif row_count == 0:
        interpretation = (
            "Data quality warning: the sample scenario dataset contains the "
            "required columns but has no rows."
        )
        is_valid = False
    else:
        interpretation = (
            "The sample scenario dataset contains the required columns, including "
            "structured commitments fields, and can be used for educational "
            "scenario demonstration. Values should remain fictional, simulated "
            "or anonymised."
        )

    return SampleScenarioValidationResult(
        is_valid=is_valid,
        missing_columns=missing_columns,
        row_count=row_count,
        interpretation=interpretation,
    )


def validate_structured_commitments_consistency(
    sample_scenarios: pd.DataFrame,
) -> SampleScenarioValidationResult:
    """
    Validate consistency between structured commitment columns and total
    existing monthly commitments.

    Args:
        sample_scenarios:
            DataFrame containing sample scenario rows.

    Returns:
        SampleScenarioValidationResult object.
    """

    column_validation = validate_sample_scenarios_columns(sample_scenarios)

    if not column_validation.is_valid:
        return column_validation

    inconsistent_rows = []

    for index, row in sample_scenarios.iterrows():
        structured_total = (
            row["housing_commitment"]
            + row["auto_loan_commitment"]
            + row["personal_loan_commitment"]
            + row["credit_card_commitment"]
            + row["other_credit_commitments"]
        )

        declared_total = row["existing_monthly_commitments"]

        if round(float(structured_total), 2) != round(float(declared_total), 2):
            inconsistent_rows.append(index)

    if inconsistent_rows:
        return SampleScenarioValidationResult(
            is_valid=False,
            missing_columns=[],
            row_count=len(sample_scenarios),
            interpretation=(
                "Data quality warning: one or more sample scenarios have "
                "inconsistent structured commitments totals. The sum of the "
                "commitment categories should equal existing_monthly_commitments."
            ),
        )

    return SampleScenarioValidationResult(
        is_valid=True,
        missing_columns=[],
        row_count=len(sample_scenarios),
        interpretation=(
            "Structured commitments are consistent across the sample scenario "
            "dataset. The sum of commitment categories matches "
            "existing_monthly_commitments for all rows."
        ),
    )


def load_and_validate_sample_scenarios(
    file_path: str | Path | None = None,
) -> tuple[pd.DataFrame, SampleScenarioValidationResult]:
    """
    Load and validate the sample scenarios dataset.

    Args:
        file_path:
            Optional custom CSV path.

    Returns:
        Tuple containing:
            - sample scenarios DataFrame
            - validation result
    """

    sample_scenarios = load_sample_scenarios(file_path=file_path)
    validation_result = validate_sample_scenarios_columns(sample_scenarios)

    return sample_scenarios, validation_result


if __name__ == "__main__":
    scenarios, validation = load_and_validate_sample_scenarios()
    commitments_validation = validate_structured_commitments_consistency(scenarios)

    print(scenarios.head())
    print(validation)
    print(commitments_validation)
