import os
import pytest
import pandas as pd 
from mylib.lib import load_dataset, calculate_statistics
from script import generate_describe, generate_visualizations, generate_md_report

file_path = "rdu-weather-history.csv"


@pytest.fixture
def data():
    """Fixture to load data for use in multiple tests."""
    return load_dataset(file_path)


def test_general_describe():
    """Test the general_describe function."""
    data = load_dataset(file_path)
    desc = generate_describe(file_path)  
    assert isinstance(desc, pd.DataFrame), "Description should be a DataFrame"
    
    # Check that all numeric columns are present in the description
    numeric_columns = data.select_dtypes(include=['number']).columns  
    for column in numeric_columns:
        assert column in desc.columns, f"Expected column '{column}' not found"


def test_generate_visualizations():
    """Test the generate_visualizations function."""
    image_paths = generate_visualizations(file_path)
    for path in image_paths:
        assert os.path.isfile(path), f"Visualization file {path} should be created"
        os.remove(path)  # Cleanup after test

def test_generate_md_report():
    """Test the generate_md_report function."""
    data = load_dataset(file_path)
    stats = calculate_statistics(data)
    image_paths = generate_visualizations(file_path)
    report_path = "summary_report.md"
    generate_md_report(stats, image_paths, report_path)
    assert os.path.isfile(report_path), "Markdown report should be created"

    # Clean up after test
    os.remove(report_path)
    for path in image_paths:
        os.remove(path)

if __name__ == "__main__":
    # Run tests manually if needed
    test_general_describe()
    test_generate_visualizations()
    test_generate_md_report()
    print("All tests passed.")