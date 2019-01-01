from .game import Elf, Goblin

def test_targets():
    elf = Elf(1,2)
    elves = [Elf(3, 2), Elf(0,0)]
    goblins = [Goblin(1,1), Goblin(1,1)]
    units = elves + goblins
    assert elf.targets(units) == goblins

def test_adjacent_positions():
    elf = Elf(1,2)
    assert elf.adjacent_positions() == {(0,2), (2, 2), (1,1), (1, 3)}
