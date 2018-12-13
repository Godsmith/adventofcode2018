from . import day11

def test_power_level():
    assert day11.power_level(3, 5, 8) == 4
    assert day11.power_level(122, 79, 57) == -5
    assert day11.power_level(217, 196, 39) == 0
    assert day11.power_level(101, 153, 71) == 4

def test_largest_power_coordinate():
    assert day11.largest_power_coordinate(18) == (33,45)