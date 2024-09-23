from main import (
    general_describe,
    summary_statistics,
    save_to_md,
    load_dataset,
)


def test_describe():
    df = load_dataset()
    desc = general_describe(df)
    assert "beer_servings" in desc.columns


def test_summary_statistics():
    df = load_dataset()
    stats = summary_statistics(df)
    assert "beer_servings" in stats
    assert isinstance(stats["beer_servings"]["Mean"], float)
    assert isinstance(stats["beer_servings"]["Median"], float)
    assert isinstance(stats["beer_servings"]["Standard Deviation"], float)


def test_save_to_md():
    df = load_dataset()
    filename = "summary.md"
    save_to_md(df, filename)
    with open(filename, "r") as file:
        content = file.read()
    assert "beer_servings" in content


if __name__ == "__main__":
    test_describe()
    test_summary_statistics()
    test_save_to_md()
