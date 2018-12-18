from . import day12

INPUT = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""".splitlines()

def test_sum_of_pot_numbers():
    assert day12.sum_of_pot_numbers(INPUT, generations=20) == 325

def test_produce():
    cave = day12.Cave(state='.....', rules={'.....': '#'})
    cave.step()
    assert str(cave) == '-2, #########'
