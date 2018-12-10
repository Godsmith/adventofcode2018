from . import day8


def test_basic():
    list_ = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    assert day8.sum_of_metadata_entries(list_) == 138
