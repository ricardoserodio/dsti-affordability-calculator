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


@dataclass
class SampleScenarioValidationResult:
    """
    Stores validation results for the sample scenario dataset.
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

    scenario_path = Path(file_path) if file_path is not None else (
        get_default_sample_scenarios_path()
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
    missing_columns = sorted(
        REQUIRED_SAMPLE_SCENARIO_COLUMNS - available_columns
    )

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
            "The sample scenario dataset contains the required columns and can "
            "be used for educational scenario demonstration. Values should "
            "remain fictional, simulated or anonymised."
        )

    return SampleScenarioValidationResult(
        is_valid=is_valid,
        missing_columns=missing_columns,
        row_count=row_count,
        interpretation=interpretation,
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

    print(scenarios.head())
    print(validation)
