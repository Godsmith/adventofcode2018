from . import day8

list_ = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def test_sum_of_metadata_entries():
    assert day8.sum_of_metadata_entries(list_) == 138

def test_value():
    assert day8.value(list_) == 66

