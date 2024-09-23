from mylib.lib import (
    load_dataset,
    process_mean,
    process_median,
    process_std,
    plot_summary_statistics,
)


def general_describe(df):
    return df.describe()


def summary_statistics(df):
    columns = [
        "beer_servings",
        "spirit_servings",
        "wine_servings",
        "total_litres_of_pure_alcohol",
    ]
    stats = {}
    for col in columns:
        mean = process_mean(df, col)
        median = process_median(df, col)
        std_dev = process_std(df, col)
        print(f"Column: {col}")
        print(f"Mean: {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        print()
        stats[col] = {"Mean": mean, "Median": median, "Standard Deviation": std_dev}
    return stats


def save_to_md(df, filename="summary.md", image_filename="figure.png"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(df.describe().to_markdown() + "\n\n")

        columns = [
            "beer_servings",
            "spirit_servings",
            "wine_servings",
            "total_litres_of_pure_alcohol",
        ]
        for col in columns:
            mean = process_mean(df, col)
            median = process_median(df, col)
            std_dev = process_std(df, col)
            file.write(f"## Column: {col}\n")
            file.write(f"- Mean: {mean:.2f}\n")
            file.write(f"- Median: {median:.2f}\n")
            file.write(f"- Standard Deviation: {std_dev:.2f}\n\n")

        file.write(f"![Summary Statistics Chart]({image_filename})\n")


if __name__ == "__main__":
    df = load_dataset()
    print(general_describe(df).to_markdown())
    summary_statistics(df)
    plot_summary_statistics(df)
    save_to_md(df)
