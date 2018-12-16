from . import day11

def test_power_level():
    assert day11.power_level(3, 5, 8) == 4
    assert day11.power_level(122, 79, 57) == -5
    assert day11.power_level(217, 196, 39) == 0
    assert day11.power_level(101, 153, 71) == 4

def test_largest_power_coordinate():
    assert day11.largest_power_coordinate(18) == (33,45)

def test_largest_power_square():
    assert day11.largest_power_square(18) == (90, 269, 16)

def test_power_diff_from_one_step_left():
    assert day11.power_diff_from_one_step_left({
        (1,1): 1,
        (1,2): 2,
        (2,1): 3,
        (2,2): 4,
        (3,1): 5,
        (3,2): 6}, 2, 1, 2) == 8

def test_power_diff_from_one_step_up():
    assert day11.power_diff_from_one_step_up({
        (1,1): 1,
        (1,2): 2,
        (1,3): 3,
        (2,1): 4,
        (2,2): 5,
        (2,3): 6}, 1, 2, 2) == 4
