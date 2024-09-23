from mylib.lib import (
    load_dataset,
    process_mean,
    process_median,
    process_std,
    plot_summary_statistics,
)


def general_describe():
    df = load_dataset()
    return df.describe()


def summary_statistics():
    df = load_dataset()
    columns = [
        "beer_servings",
        "spirit_servings",
        "wine_servings",
        "total_litres_of_pure_alcohol",
    ]

    for col in columns:
        print(f"Column: {col}")
        print(f"Mean: {process_mean(df, col):.2f}")
        print(f"Median: {process_median(df, col):.2f}")
        print(f"Standard Deviation: {process_std(df, col):.2f}")
        print()

    return {
        "Mean": process_mean,
        "Median": process_median,
        "Standard Deviation": process_std,
    }


def save_to_md():
    with open("test.md", "w", encoding="utf-8") as file:
        file.write("test")


if __name__ == "__main__":
    df = load_dataset()
    print(general_describe())
    summary_statistics()
    plot_summary_statistics(df)
