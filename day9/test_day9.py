from . import day9

def test_basic():
    assert day9.high_score(9, 25) == 32
    assert day9.high_score(10, 1618) == 8317
    assert day9.high_score(13, 7999) == 146373
    assert day9.high_score(17, 1104) == 2764
    assert day9.high_score(21, 6111) == 54718
    assert day9.high_score(30, 5807) == 37305
