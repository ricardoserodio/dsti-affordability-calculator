"""
Smoke tests for application-level imports.

These tests help ensure that the main project modules can be imported
successfully in a clean environment.

The project is educational, demonstrative and portfolio-oriented.
It must not be interpreted as a credit approval system, underwriting engine,
bank pricing model, financial advisory tool or replacement for formal human
credit analysis.
"""

import importlib
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.append(str(SRC_PATH))


def test_core_modules_import_successfully():
    modules = [
        "dsti_calculator",
        "income_calculator",
        "ltv_calculator",
        "maturity_validator",
        "validation_checks",
        "scenario_engine",
        "loan_payment_calculator",
        "interest_rate_builder",
        "interest_rate_stress",
        "euribor_provider",
    ]

    for module_name in modules:
        imported_module = importlib.import_module(module_name)
        assert imported_module is not None


def test_streamlit_app_file_exists():
    app_path = PROJECT_ROOT / "app" / "streamlit_app.py"

    assert app_path.exists()
    assert app_path.is_file()


def test_requirements_file_exists():
    requirements_path = PROJECT_ROOT / "requirements.txt"

    assert requirements_path.exists()
    assert requirements_path.is_file()


def test_github_actions_workflow_exists():
    workflow_path = PROJECT_ROOT / ".github" / "workflows" / "python-tests.yml"

    assert workflow_path.exists()
    assert workflow_path.is_file()
