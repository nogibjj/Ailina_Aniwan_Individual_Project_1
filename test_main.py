from main import (
    general_describe,
    summary_statistics,
    save_to_md,
)


def test_describe():
    desc = general_describe()
    assert "beer_servings" in desc.columns


def test_summary_statistics():
    stats = summary_statistics()
    # Ensure returned dictionary has proper structure
    assert "Mean" in stats and callable(stats["Mean"])
    assert "Median" in stats and callable(stats["Median"])
    assert "Standard Deviation" in stats and callable(stats["Standard Deviation"])


def test_save_to_md():
    save_to_md()


if __name__ == "__main__":
    test_describe()
    test_summary_statistics()
    test_save_to_md()
