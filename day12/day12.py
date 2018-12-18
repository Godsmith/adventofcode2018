from collections import defaultdict
from .. import util

class Cave:
    def __init__(self, state, rules):
        self.state = defaultdict(lambda: '.')
        for i, c in enumerate(state):
            self.state[i] = c
        self.rules = defaultdict(lambda: '.')
        for key in rules:
            self.rules[key] = rules[key]

    def step(self):
        new_state = defaultdict(lambda: '.')
        indices = range(min(self.state.keys()) - 2, max(self.state.keys()) + 3)
        for i in indices:
            previous = (self.state[i-2] + self.state[i-1] + self.state[i] +
                        self.state[i+1] + self.state[i+2])
            new_state[i] = self.rules[previous]
        self.state = new_state

    def __str__(self):
        out = ''
        for key, value in sorted(self.state.items()):
            out += value
        return f'{min(self.state.keys())}, {out}'


def sum_of_pot_numbers(input_lines, generations):
    state = input_lines[0].split()[-1]
    rules = {}
    for line in input_lines[2:]:
        key, _, value = line.split()
        rules[key] = value
    cave = Cave(state, rules)
    for _ in range(generations):
        cave.step()

    pot_sum = 0
    for key, value in cave.state.items():
        if value == '#':
            pot_sum += key
    return pot_sum



lines = util.input_lines(12)

print(sum_of_pot_numbers(lines, 20))
