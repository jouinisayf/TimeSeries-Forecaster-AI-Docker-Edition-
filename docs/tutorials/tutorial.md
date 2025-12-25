# TimeSeries-Forecaster-AI — Quick Tutorial

This short tutorial guides you through the main steps to use the TimeSeries-Forecaster-AI project.  
It explains how to install dependencies, run the forecasting pipeline, and understand the results.

## 1. Introduction

TimeSeries-Forecaster-AI is a lightweight time-series forecasting pipeline that combines:

- **ARIMA** models (to capture temporal structure)
- **GARCH** models (to model volatility)
- **Poetry** for dependency management
- **Logging**, **unit tests**, and **documentation**

This tutorial explains how to execute the project from end to end.

## 2. Requirements

Before running the project, you need:

- Python 3.10 or above  
- Poetry installed:

```
pip install poetry
```
## 3. Install Dependencies

From the project root directory:
```
poetry install
```

This installs all dependencies specified in the pyproject.toml file:

pandas
numpy
matplotlib
statsmodels
arch
logging tools
pytest (dev)
ruff (dev)
pdoc (dev)

## 4. Run the Forecasting Pipeline

The main script is located here:
src/main.py
To run the full ARIMA + GARCH pipeline:
```
poetry run python src/main.py
```

The pipeline performs the following steps:

-Loads the dataset data/gld_price_data.csv
-Cleans missing values
-Fits an ARIMA(2,0,3) model
-Fits a GARCH(1,1) model on ARIMA residuals
-Forecasts the next 20 values
-Displays:
  *ARIMA summary
  *GARCH summary
  *Forecast plot (Matplotlib)

## 5. Example Output

You should see something like:
```
ARIMA Summary:
SARIMAX Results
...

GARCH Summary:
Volatility Model: GARCH(1,1)
...
```
A Matplotlib graph will also appear showing the historical series and the forecast.

## 6. Understanding the Plot

The generated plot contains:

Blue line → original historical GLD values
Red line → ARIMA forecast for the next 20 steps
This helps visualize trend continuation and volatility influence.

## 7. Running Tests

To run unit tests:
```
poetry run pytest -v
```

Expected output:
```
test_preprocess.py .... PASSED
test_models.py .... PASSED
```

## 8. Generate Documentation

Documentation can be generated using pdoc:
```
poetry run pdoc src -o docs
```

Generated HTML files will appear inside:
docs/

## 9. Conclusion

You are now ready to explore, modify, or extend the ARIMA + GARCH forecasting tool.
Feel free to adapt the models, test different parameters, or analyze new datasets.

For more details, check:

preprocess.py : Data loading
models.py : ARIMA and GARCH functions
visualize.py : Plotting
main.py : Full pipeline

Happy forecasting!