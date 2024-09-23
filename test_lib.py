import pandas as pd
from mylib.lib import (
    load_dataset,
    process_mean,
    process_median,
    process_std,
)


def test_load_dataset():
    df = load_dataset()
    assert df is not None
    assert df.shape == (193, 5)


def test_statistics():
    data = {
        "beer_servings": [50, 60, 70],
        "spirit_servings": [80, 90, 100],
        "wine_servings": [20, 30, 40],
    }
    df = pd.DataFrame(data)

    assert process_mean(df, "beer_servings") == 60, "Mean of beer_servings should be 60"
    assert (
        process_mean(df, "spirit_servings") == 90
    ), "Mean of spirit_servings should be 90"
    assert process_mean(df, "wine_servings") == 30, "Mean of wine_servings should be 30"

    assert (
        process_median(df, "beer_servings") == 60
    ), "Median of beer_servings should be 60"
    assert (
        process_median(df, "spirit_servings") == 90
    ), "Median of spirit_servings should be 90"
    assert (
        process_median(df, "wine_servings") == 30
    ), "Median of wine_servings should be 30"

    assert (
        round(process_std(df, "beer_servings"), 2) == 10
    ), "Std deviation of beer_servings should be 10.00"
    assert (
        round(process_std(df, "spirit_servings"), 2) == 10
    ), "Std deviation of spirit_servings should be 10.00"
    assert (
        round(process_std(df, "wine_servings"), 2) == 10
    ), "Std deviation of wine_servings should be 10.00"


if __name__ == "__main__":
    test_load_dataset()
    test_statistics()
