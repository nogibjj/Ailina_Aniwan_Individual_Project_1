from mylib.lib import (
    load_dataset,
    process_mean,
    process_median,
    process_std,
    plot_summary_statistics,
)


def general_describe():
    general = load_dataset()
    return general.describe()


def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")


if __name__ == "__main__":
    save_to_md()
