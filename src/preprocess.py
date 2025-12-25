import pandas as pd
import os
import logging

logger = logging.getLogger("TimeSeriesForecaster")


def load_time_series(path, column="GLD", output_dir="shared/processed"):
    """
    Load and clean a financial time series from a CSV file.

    The function:
    - loads a CSV file containing a date column and financial indicators
    - converts the selected column to numeric
    - sets the "Date" column as index
    - removes invalid or missing values
    - logs detailed steps for debugging and traceability
    - saves the cleaned series to disk (Docker-friendly)

    Parameters
    ----------
    path : str
        Path to the CSV dataset.
    column : str, optional
        Name of the column to extract as a time series (default is "GLD").
    output_dir : str, optional
        Directory where the cleaned time series will be saved
        (default is "shared/processed").

    Returns
    -------
    pandas.Series
        A cleaned time series indexed by date.

    Raises
    ------
    FileNotFoundError
        If the provided file path does not exist.
    ValueError
        If the column does not exist in the dataset.

    Notes
    -----
    Logging Levels used:
        - INFO: loading steps and final dataset size
        - DEBUG: head of raw DataFrame before cleaning
        - WARNING: number of removed missing values
        - CRITICAL: missing file error before raising exception
    """
    logger.info(f"Loading dataset from {path}")

    # Check dataset existence
    if not os.path.exists(path):
        logger.critical(f"Dataset not found at path: {path}")
        raise FileNotFoundError(path)

    # Load CSV file
    df = pd.read_csv(path, sep=",", parse_dates=["Date"], dayfirst=False)
    logger.debug(f"Raw DataFrame head: {df.head()}")

    # Set date as index
    df.set_index("Date", inplace=True)

    # Convert selected column to numeric and clean missing values
    before_drop = df[column].isna().sum()
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=[column])
    after_drop = df[column].isna().sum()

    if before_drop != after_drop:
        logger.warning(
            f"{before_drop - after_drop} missing values removed in column {column}"
        )

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save cleaned time series to disk
    cleaned_path = os.path.join(output_dir, "cleaned_series.csv")
    df[[column]].to_csv(cleaned_path)

    logger.info(f"Cleaned dataset saved to {cleaned_path}")
    logger.info(f"Dataset loaded successfully: {len(df)} rows")

    return df[column]


# --------------------------------------------------
# Entry point for Docker multi-container execution
# --------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logger.info("Starting preprocessing step")

    # Default dataset path used in Docker
    load_time_series("data/gld_price_data.csv")

    logger.info("Preprocessing completed successfully")
