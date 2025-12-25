import pandas as pd
import logging
from src.models import forecast_combined

# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("TimeSeriesForecaster")


def main():
    """
    Training step of the time series forecasting pipeline.

    This script:
    1. Loads the cleaned time series produced by the preprocess step;
    2. Trains ARIMA and GARCH models;
    3. Generates forecasts;
    4. Saves model summaries and forecast values to disk.

    The outputs are written to shared volumes so they can be reused
    by subsequent pipeline steps (visualization).
    """
    logger.info("Starting training step")

    # --------------------------------------------------
    # Load cleaned time series from shared volume
    # --------------------------------------------------
    series_path = "shared/processed/cleaned_series.csv"
    logger.info(f"Loading cleaned series from {series_path}")

    series = pd.read_csv(
        series_path,
        index_col=0,
        parse_dates=True
    ).iloc[:, 0]

    logger.info(f"Cleaned series loaded: {len(series)} points")

    # --------------------------------------------------
    # Train models and generate forecasts
    # --------------------------------------------------
    logger.info("Training ARIMA + GARCH models")

    forecast_combined(
        series=series,
        arima_order=(2, 0, 3),
        garch_order=(1, 1),
        horizon=20
    )

    logger.info("Training step completed successfully")


# --------------------------------------------------
# Entry point for Docker multi-container execution
# --------------------------------------------------
if __name__ == "__main__":
    main()
