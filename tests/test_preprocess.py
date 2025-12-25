import pandas as pd
from src.preprocess import load_time_series
import pytest


def test_load_time_series_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_time_series("data/no_file.csv")


def test_load_time_series_valid_file(tmp_path):
    p = tmp_path / "test.csv"
    df = pd.DataFrame({"Date": ["2020-01-01", "2020-01-02"], "GLD": [1500, 1510]})
    df.to_csv(p, index=False)

    series = load_time_series(str(p))
    assert len(series) == 2
    assert series.iloc[0] == 1500
