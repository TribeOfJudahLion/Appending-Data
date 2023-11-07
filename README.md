<br/>
<p align="center">
  <a href="https://github.com/TribeOfJudahLion/Appending-Data">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Streamlined Data Consolidation: Automating Marketing Analytics with Python</h3>

  <p align="center">
    Discover how our Python solution transforms complex marketing campaign data into a simplified, unified dataset for insightful analytics, empowering data analysts with efficient processes and error logging for optimal data integrity.
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Appending-Data"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/TribeOfJudahLion/Appending-Data">View Demo</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Appending-Data/issues">Report Bug</a>
    .
    <a href="https://github.com/TribeOfJudahLion/Appending-Data/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/TribeOfJudahLion/Appending-Data/total) ![Contributors](https://img.shields.io/github/contributors/TribeOfJudahLion/Appending-Data?color=dark-green) ![Stargazers](https://img.shields.io/github/stars/TribeOfJudahLion/Appending-Data?style=social) ![Issues](https://img.shields.io/github/issues/TribeOfJudahLion/Appending-Data) ![License](https://img.shields.io/github/license/TribeOfJudahLion/Appending-Data) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

**Problem:**

A data analyst at a marketing firm needs to consolidate information from two separate marketing campaign datasets into a single comprehensive dataset. The individual datasets are updated regularly and contain many columns, of which only a specific subset is relevant for analysis. The analyst requires an automated way to:

1. Load the data from each campaign CSV file,
2. Select and keep only the columns relevant to the analysis,
3. Log the shape and preview the data to ensure correct loading and selection,
4. Combine the two datasets into one for a complete view of the data,
5. Log any issues that occur during the process for troubleshooting purposes.

**Challenges:**

- Ensuring the correct files are loaded without errors,
- Handling missing files or incorrect paths,
- Dealing with potential missing columns in the datasets,
- Efficiently combining the datasets while ensuring data integrity,
- Providing clear logs for the process to facilitate monitoring and debugging.

**Solution:**

The provided Python script solves the stated problem through the following steps:

1. **Configuration:**
   - A logging configuration is set up to document the process and any issues encountered, which is crucial for both debugging and record-keeping.

2. **Function Definitions:**
   - `load_dataset()`: Loads a dataset from a given CSV file path while selecting only the specified columns. It logs success or errors regarding file existence and column presence.
   - `inspect_data()`: Logs the shape and prints the first few rows of a DataFrame to allow for a quick manual inspection.
   - `append_datasets()`: Combines two DataFrames into one, facilitating a consolidated view for analysis.

3. **Process Execution in `main()`:**
   - File paths for the datasets are defined using `Path` objects for OS-independent file path handling.
   - A list of relevant columns is defined, ensuring that only necessary data is kept.
   - Datasets are loaded from the files using `load_dataset()` and inspected via `inspect_data()`.
   - The two datasets are combined with `append_datasets()` and the resulting DataFrame is inspected again.

4. **Logging:**
   - The script logs important milestones and errors, such as successful data load, missing files, missing columns, and the data shape after each operation. This information is timestamped and categorized by severity level (INFO, ERROR).

**Outcome:**

When executed, the script automates the data preparation process for the analyst, providing a single, cleaned, and consolidated dataset ready for analysis. The analyst can quickly identify any issues through the logs and ensure the data is in the correct format for further work. The modular design of the script also allows for easy updates or changes to the data loading and processing steps in the future.

The script provided is a Python program designed to load, process, and combine data from two separate CSV files into a single DataFrame. Below is an explanation of each part of the script and its functionality:

1. **Import Statements**:
    - `import numpy as np`: Imports the NumPy library, typically used for numerical operations, although it is not explicitly used in this script.
    - `import pandas as pd`: Imports the pandas library, a powerful tool for data manipulation and analysis.
    - `import logging`: Imports the logging module, which allows for tracking events that happen when the software runs.
    - `from pathlib import Path`: Imports the `Path` class from the `pathlib` module, which provides an object-oriented filesystem paths interface.
    - `from typing import List`: Imports the `List` type from the `typing` module, which is used for type hinting (specifying the expected data types of variables).

2. **Logging Configuration**:
    - `logging.basicConfig(...)`: Configures the logging to output messages with a specific format including the timestamp, the level of importance (INFO, ERROR, etc.), and the actual message.

3. **Function Definitions**:
    - `load_dataset(file_path: Path, columns_to_keep: List[str]) -> pd.DataFrame`: This function is responsible for loading the data from a CSV file into a pandas DataFrame. It only keeps the columns listed in `columns_to_keep`. If the file is not found or the specified columns are not present, an error is logged and the exception is raised.
    - `inspect_data(data: pd.DataFrame, data_name: str)`: It logs the shape (number of rows and columns) and the first five rows of the DataFrame. This is useful for getting a quick overview of the data.
    - `append_datasets(dataset1: pd.DataFrame, dataset2: pd.DataFrame) -> pd.DataFrame`: This function concatenates two DataFrames vertically (one on top of the other), assuming they have the same columns.

4. **The `main()` Function**:
    - Paths to the CSV files are defined using `Path` objects. This is where the script expects to find the CSV files to load.
    - `columns_to_keep` is a list of column names to retain in the DataFrame after loading the data.
    - `marketing_sample1` and `marketing_sample2` are DataFrames created by loading data from the specified CSV files using the `load_dataset` function.
    - The `inspect_data` function is called to log information about each of these DataFrames.
    - The `append_datasets` function is then used to combine `marketing_sample1` and `marketing_sample2` into a single DataFrame called `appended_data`.
    - Finally, `inspect_data` is called again to log the shape and the first five rows of the combined DataFrame.

5. **Execution Check**:
    - The `if __name__ == "__main__":` block makes sure that the `main()` function is called only when the script is executed as a standalone file, not when imported as a module in another script.

When the script is run, it will process the specified CSV files and print out logs to the console, detailing the steps it has taken and any issues encountered. The final output will be a combined dataset from both files, which can then be used for further analysis or processing.

## Built With

This project leverages several technologies and tools listed below:

- [**Python**](https://www.python.org/) - The core programming language used for the development of this project.
- [**Pandas**](https://pandas.pydata.org/) - A library providing high-performance, easy-to-use data structures, and data analysis tools.
- [**NumPy**](https://numpy.org/) - An essential library for scientific computing with Python, providing support for arrays and matrices.
- [**Pathlib**](https://docs.python.org/3/library/pathlib.html) - Used for file system path manipulation, providing an object-oriented interface.
- [**Logging**](https://docs.python.org/3/library/logging.html) - Utilized for tracking events that occur when the program runs, aiding in debugging and understanding the program's operational flow.
- [**Visual Studio Code**](https://code.visualstudio.com/) - The preferred Integrated Development Environment (IDE) for writing and editing code.
- [**Git**](https://git-scm.com/) - The version control system used for tracking changes, coordinating work, and backing up the code.
- [**GitHub**](https://github.com/) - The platform for hosting the version-controlled code and facilitating collaboration.

## Prerequisites

Make sure you have Python 3.x installed on your system. The following Python packages are also required:

```bash
pandas
numpy
```

These can be installed via `pip` using the following command:

```bash
pip install pandas numpy
```

## Installation

Clone this repository to get started with the project on your local machine:

```sh
git clone https://github.com/your_username_/Project-Name.git
```

After cloning the repository, navigate to the project directory and install the required packages:

```sh
pip install -r requirements.txt
```





## Getting Started

This section will guide you through the setup process to get the project running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- **Python**: The project is developed with Python. You will need Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: The Python package installer, which usually comes with Python.

To check if you have Python and pip installed, you can run the following commands:

```bash
python --version
pip --version

This section guides you through using the Python script to consolidate your marketing campaign datasets. Follow these steps to prepare your data for analysis.

### Preparing Your Data

Ensure that your CSV files are in the correct directory and named appropriately:

- `marketing_campaign_append1.csv`
- `marketing_campaign_append2.csv`

These files should be in the same folder as your script or in a subdirectory that your script references.

### Running the Script

To run the script, you'll need Python installed on your system. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

Open your terminal (or command prompt), navigate to the directory containing your script, and run the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of your Python script.

### Understanding the Output

When you run the script, it will perform the following actions:

1. Load the data from each specified CSV file.
2. Select and keep only the specified columns.
3. Log the shape of each dataset and display the first 5 rows to ensure correct loading and selection.
4. Combine the datasets into one for a complete view of the data.
5. Log any issues encountered during the process to a log file.

The logs will look something like this:

```log
2023-11-07 10:00:00 - INFO - Dataset loaded successfully from marketing_campaign_append1.csv
2023-11-07 10:00:00 - INFO - Shape of marketing_sample1: (1000, 11)
...
2023-11-07 10:00:01 - ERROR - File marketing_campaign_append3.csv not found.
```

### Post-Processing

After the script has run, you will have a single DataFrame in memory that contains your consolidated data. If you want to export this DataFrame to a CSV file, you can add the following line to the end of the `main()` function in the script:

```python
appended_data.to_csv('consolidated_marketing_data.csv', index=False)
```

### Troubleshooting

If you encounter any issues while running the script, refer to the log messages. These messages can help you identify if files are missing, if there are issues with the data itself, or if the wrong columns are being accessed.

For any errors related to missing columns, ensure that the columns listed in `columns_to_keep` are present in both CSV files.

### Modifying the Script

If you need to work with different columns or additional datasets, you can modify the `columns_to_keep` list or the `append_datasets()` function accordingly. Ensure that any new columns added to `columns_to_keep` are present in all CSV files to avoid `KeyError`s.


## Usage

To run this script, execute it within your Python environment. Ensure the CSV data files are located in the specified directories as per the script's `Path` objects.

Refer to the [Documentation](#documentation) section for detailed usage instructions.

## Documentation

The full documentation for this project, including additional setup details, use cases, and examples, is available in the project's wiki:

* [Project Wiki](https://github.com/your_username_/Project-Name/wiki)
```

Be sure to replace `your_username_` and `Project-Name` with your GitHub username and your project's repository name. Additionally, adjust the technology and tool links as per your project's actual tech stack.



## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Appending-Data/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Appending-Data/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Appending-Data/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
