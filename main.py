from mylib.lib import *

# filepath = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"
file_path = "rdu-weather-history.csv"


def general_describe(filepath):
    """General describe function to perform data loading and statistics calculation for numeric columns."""
    data = load_dataset(filepath)
    # Select only numeric columns for description
    numeric_data = data.select_dtypes(include=['number'])  
    return numeric_data.describe()


def summary(filepath):
    """Summary of each numeric column's mean, median, and standard deviation."""
    data = load_dataset(filepath)
    return calculate_statistics(data)


def generate_visualizations(filepath):
    """Generate visualizations for specific columns and save them as PNG files."""
    # Load data
    data = load_dataset(filepath)

    # Create and save histograms for selected columns
    columns = ["Temperature Maximum", "Temperature Minimum", "Precipitation"]
    image_paths = []
    for column in columns:
        image_path = f"{column.lower().replace(' ', '_')}_distribution.png"
        create_histogram(data, column, image_path)
        image_paths.append(image_path)

    return image_paths


def generate_md_report(stats, image_paths, output_path_md):
    """Generate a markdown report with the descriptive statistics and images."""
    with open(output_path_md, "w") as file:
        file.write("# Summary Report\n\n")
        file.write("## Descriptive Statistics\n\n")
        file.write(stats.to_markdown())
        file.write("\n\n")
        for image_path in image_paths:
            file.write(f"![{image_path}]({image_path})\n")
