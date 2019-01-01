from .game import turn_order_key, Goblin, Elf

def test_turn_order_key():
    units = [Goblin(2, 1), Elf(4, 1), Goblin(1, 2), Goblin(3,2)]
    assert sorted(units, key=turn_order_key) == units
