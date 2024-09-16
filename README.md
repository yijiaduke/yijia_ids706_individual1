 yijia_ids706_individual1

## Python Template

This project is for generating descriptive statistics and visualizations from datasets using Python. It integrates CI/CD capabilities through GitHub Actions, which automate the process of generating, testing, and pushing summary reports in Markdown format.

## CI/CD Badge
[![CI](https://github.com/nogibjj/yijia_ids706_miniProj2/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/yijia_ids706_miniProj2/actions/workflows/hello.yml)

## File Structure

- **`.devcontainer/`**: Contains the development container configuration (`devcontainer.json` and a Dockerfile) to ensure a consistent development environment.
- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository.
- **`rdu-weather-history.csv`**: The dataset used for analysis, containing historical weather data for the Durham region.
- **`summary_report.md`**: Automatically generated report that includes descriptive statistics (mean, median, standard deviation) and visualizations.
- **`script.py`**: Implements core functionality such as `generate_describe`,`generate_visualizations` and `generate_md_report`.
- **`lib.py`**: Contains reusable utility functions like `load_dataset`, `calculate_statistics`, and `create_histogram`, which are shared between the script and the Jupyter notebook.
- **`test_script.py`**: Contains tests for functions implemented in `script.py`.
- **`test_lib.py`**: Contains tests for functions in `lib.py`.
- **`main.ipynb`**: A Jupyter Notebook for data analysis and testing, integrating with the shared functions in `lib.py`.


## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:nogibjj/yijia_ids706_miniProj2.git
```

### 2. Open the Repository in CodeSpace

- Open the repository in GitHub Codespaces
- Wait for the container setup to complete to ensure a consistent environment.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Ruff.
- make test: Runs all tests in test_lib.py and test_script.py using pytest and checks Jupyter Notebook cells with the nbval plugin.
- make clean: Removes pytest cache.
- make generate_report: Generates and commits a profiling report in Markdown format during the CI/CD process.

## CI/CD Setup
- Location: .github/workflows/
- Actions: Automatically runs setup, lint, format, and test actions, ensuring continuous integration and code quality.

## Summary Report Generation
The CI/CD pipeline automatically generates a Markdown report. The report includes descriptive statistics (mean, median, standard deviation) and visualizations generated from the dataset. The report is then committed and pushed back to the repository.