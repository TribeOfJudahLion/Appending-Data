import numpy as np
import pandas as pd
import logging
from pathlib import Path
from typing import List  # This import was missing

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_dataset(file_path: Path, columns_to_keep: List[str]) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Dataset loaded successfully from {file_path}")
        return data[columns_to_keep]
    except FileNotFoundError:
        logging.error(f"File {file_path} not found.")
        raise
    except KeyError as e:
        logging.error(f"Columns not found in the dataset: {e}")
        raise


def inspect_data(data: pd.DataFrame, data_name: str):
    logging.info(f"Shape of {data_name}: {data.shape}")
    logging.info(f"First 5 rows of {data_name}:\n{data.head()}")


def append_datasets(dataset1: pd.DataFrame, dataset2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([dataset1, dataset2])


def main():
    # Define the paths to the datasets
    file_path1 = Path("marketing_campaign_append1.csv")
    file_path2 = Path("marketing_campaign_append2.csv")

    # Define the columns to keep
    columns_to_keep = ['ID', 'Year_Birth', 'Education', 'Marital_Status',
                       'Income', 'Kidhome', 'Teenhome', 'Dt_Customer',
                       'Recency', 'NumStorePurchases', 'NumWebVisitsMonth']

    # Load and process the datasets
    marketing_sample1 = load_dataset(file_path1, columns_to_keep)
    marketing_sample2 = load_dataset(file_path2, columns_to_keep)

    # Inspect the datasets
    inspect_data(marketing_sample1, "marketing_sample1")
    inspect_data(marketing_sample2, "marketing_sample2")

    # Append the datasets
    appended_data = append_datasets(marketing_sample1, marketing_sample2)

    # Inspect the appended data
    inspect_data(appended_data, "appended_data")


if __name__ == "__main__":
    main()
