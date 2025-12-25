import pandas as pd
from src.models import fit_arima, fit_garch


def test_fit_arima():
    series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
    model = fit_arima(series, order=(1, 0, 1))
    assert model is not None


def test_fit_garch():
    residuals = pd.Series([0.1, -0.2, 0.05, -0.1, 0.2])
    model = fit_garch(residuals, order=(1, 1))
    assert model is not None
