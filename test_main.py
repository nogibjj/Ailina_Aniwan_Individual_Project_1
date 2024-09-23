from main import (
    general_describe,
    summary_statistics,
    save_to_md,
)


def test_describe():
    test_describe = general_describe()


def test_two_describles():
    test_describe = general_describe()
    test_summary_statistics = summary_statistics()


def test_save_to_md():
    save_to_md()


if __name__ == "__main__":
    test_describe()
    test_two_describles()
    test_save_to_md()
