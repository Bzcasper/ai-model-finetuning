"""
Test configuration and utilities for the modal-deployments project.
"""

import os
import sys
from pathlib import Path

# Add src directory to Python path for testing
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Test configuration
TEST_CONFIG = {
    "timeout": 30,
    "mock_modal": True,
    "test_data_dir": PROJECT_ROOT / "tests" / "data",
    "temp_dir": PROJECT_ROOT / "tests" / "temp",
}

# Create test directories if they don't exist
TEST_CONFIG["test_data_dir"].mkdir(exist_ok=True)
TEST_CONFIG["temp_dir"].mkdir(exist_ok=True)
