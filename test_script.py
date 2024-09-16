import os
import pytest
import pandas as pd 
from mylib.lib import load_dataset, calculate_statistics, create_histogram
from main import general_describe, summary, generate_visualizations, generate_md_report

# Define the path to the test dataset
file_path = "rdu-weather-history.csv"


@pytest.fixture
def data():
    """Fixture to load data for use in multiple tests."""
    return load_dataset(file_path)


def test_general_describe(data):
    """Test the general_describe function."""
    desc = general_describe(file_path)  # Call the function
    assert isinstance(desc, pd.DataFrame), "Description should be a DataFrame"
    
    # Adjust expected columns to exclude non-numeric columns like 'Date'
    numeric_columns = data.select_dtypes(include=['number']).columns  # Only numeric columns
    for column in numeric_columns:
        assert column in desc.columns, f"Expected column '{column}' not found in the description"

def test_summary(data):
    """Test the summary function."""
    stats = summary(file_path)
    expected_columns = ["Temperature Minimum", "Temperature Maximum", "Precipitation"]
    for column in expected_columns:
        assert (
            column in stats.columns
        ), f"Expected column {column} not found in summary statistics"


def test_generate_visualizations(data):
    """Test the generate_visualizations function."""
    image_paths = generate_visualizations(file_path)
    for path in image_paths:
        assert os.path.isfile(path), f"Visualization file {path} should be created"
        os.remove(path)  # Cleanup after test


def test_generate_md_report(data):
    """Test the generate_md_report function."""
    stats = summary(file_path)
    image_paths = generate_visualizations(file_path)
    report_path = "summary_report.md"
    generate_md_report(stats, image_paths, report_path)
    assert os.path.isfile(report_path), "Markdown report should be created"

    # Clean up after test
    os.remove(report_path)
    for path in image_paths:
        os.remove(path)



if __name__ == "__main__":
    test_general_describe(load_dataset(file_path))
    test_summary(load_dataset(file_path))
    test_generate_visualizations(load_dataset(file_path))
    test_generate_md_report(load_dataset(file_path))
    print("All tests passed.")
