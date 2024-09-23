import pandas as pd
from mylib.lib import (
    process_mean,
    process_median,
    process_std,
)


def test_statistics():
    data = {
        "beer_servings": [50, 60, 70],
        "spirit_servings": [80, 90, 100],
        "wine_servings": [20, 30, 40],
    }
    df = pd.DataFrame(data)

    print("Testing 'beer_servings' statistics...")
    expected_mean_beer = 60
    expected_median_beer = 60
    expected_std_beer = 10
    print(
        f"Expected mean: {expected_mean_beer:.2f}, "
        f"Calculated mean: {process_mean(df, 'beer_servings'):.2f}"
    )
    print(
        f"Expected median: {expected_median_beer:.2f}, "
        f"Calculated median: {process_median(df, 'beer_servings'):.2f}"
    )
    print(
        f"Expected standard deviation: {expected_std_beer:.2f}, "
        f"Calculated standard deviation: {process_std(df, 'beer_servings'):.2f}"
    )
    print()


if __name__ == "__main__":
    test_statistics()
