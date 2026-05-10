"""
Unit tests for the sample scenario loader.

These tests validate loading and structural validation of the fictional sample
scenario dataset used by the DSTI Affordability Calculator.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
bank pricing model, financial advisory tool or replacement for formal human
credit analysis.
"""

import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))

from sample_scenario_loader import (
    REQUIRED_SAMPLE_SCENARIO_COLUMNS,
    get_default_sample_scenarios_path,
    load_and_validate_sample_scenarios,
    load_sample_scenarios,
    validate_sample_scenarios_columns,
)


def build_valid_sample_scenarios_dataframe() -> pd.DataFrame:
    """
    Build a minimal valid sample scenarios DataFrame for testing.
    """

    return pd.DataFrame(
        [
            {
                "scenario_name": "Base educational simulation",
                "income_source_1": 1500,
                "income_source_2": 1000,
                "use_conservative_income": False,
                "conservative_factor": 0.90,
                "existing_monthly_commitments": 300,
                "loan_amount": 180000,
                "loan_maturity_years": 30,
                "euribor_tenor": "6M",
                "simulated_euribor_percentage": 3.00,
                "simulated_spread_percentage": 0.90,
                "stress_buffer_percentage": 1.50,
                "acquisition_value": 220000,
                "valuation_value": 215000,
                "configured_dsti_threshold_percentage": 40,
                "configured_ltv_threshold_percentage": 90,
                "current_age": 35,
                "configured_maximum_age_at_end": 75,
                "scenario_note": (
                    "Standard fictional scenario used to demonstrate DSTI, "
                    "LTV, maturity and interest rate stress."
                ),
            }
        ]
    )


def test_required_sample_scenario_columns_contains_expected_fields():
    assert "scenario_name" in REQUIRED_SAMPLE_SCENARIO_COLUMNS
    assert "simulated_euribor_percentage" in REQUIRED_SAMPLE_SCENARIO_COLUMNS
    assert "simulated_spread_percentage" in REQUIRED_SAMPLE_SCENARIO_COLUMNS
    assert "stress_buffer_percentage" in REQUIRED_SAMPLE_SCENARIO_COLUMNS
    assert "scenario_note" in REQUIRED_SAMPLE_SCENARIO_COLUMNS


def test_get_default_sample_scenarios_path_points_to_examples_folder():
    result = get_default_sample_scenarios_path()

    assert result.name == "sample_scenarios.csv"
    assert result.parent.name == "examples"


def test_load_sample_scenarios_from_custom_path(tmp_path):
    sample_dataframe = build_valid_sample_scenarios_dataframe()
    sample_path = tmp_path / "sample_scenarios.csv"

    sample_dataframe.to_csv(sample_path, index=False)

    result = load_sample_scenarios(file_path=sample_path)

    assert len(result) == 1
    assert result.loc[0, "scenario_name"] == "Base educational simulation"
    assert result.loc[0, "euribor_tenor"] == "6M"


def test_load_sample_scenarios_raises_error_for_missing_file(tmp_path):
    missing_path = tmp_path / "missing_sample_scenarios.csv"

    with pytest.raises(FileNotFoundError):
        load_sample_scenarios(file_path=missing_path)


def test_validate_sample_scenarios_columns_returns_valid_result():
    sample_dataframe = build_valid_sample_scenarios_dataframe()

    result = validate_sample_scenarios_columns(sample_dataframe)

    assert result.is_valid is True
    assert result.missing_columns == []
    assert result.row_count == 1
    assert "required columns" in result.interpretation
    assert "fictional" in result.interpretation


def test_validate_sample_scenarios_columns_detects_missing_columns():
    sample_dataframe = build_valid_sample_scenarios_dataframe()
    sample_dataframe = sample_dataframe.drop(columns=["scenario_name"])

    result = validate_sample_scenarios_columns(sample_dataframe)

    assert result.is_valid is False
    assert result.missing_columns == ["scenario_name"]
    assert result.row_count == 1
    assert "missing required columns" in result.interpretation


def test_validate_sample_scenarios_columns_detects_empty_dataset():
    sample_dataframe = pd.DataFrame(columns=list(REQUIRED_SAMPLE_SCENARIO_COLUMNS))

    result = validate_sample_scenarios_columns(sample_dataframe)

    assert result.is_valid is False
    assert result.missing_columns == []
    assert result.row_count == 0
    assert "has no rows" in result.interpretation


def test_load_and_validate_sample_scenarios_from_custom_path(tmp_path):
    sample_dataframe = build_valid_sample_scenarios_dataframe()
    sample_path = tmp_path / "sample_scenarios.csv"

    sample_dataframe.to_csv(sample_path, index=False)

    loaded_dataframe, validation_result = load_and_validate_sample_scenarios(
        file_path=sample_path
    )

    assert len(loaded_dataframe) == 1
    assert validation_result.is_valid is True
    assert validation_result.row_count == 1
