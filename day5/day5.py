from collections import Counter
from .. import util

def react(unit1, unit2):
    return unit1 != unit2 and unit1.lower() == unit2.lower()

def trigger(polymer: str):
    out = [polymer[0]]
    for char in polymer[1:]:
        if len(out) == 0 or not react(char, out[-1]):
            out.append(char)
        else:
            out.pop()
    return ''.join(out)

def improved_polymer_lengths(polymer):
    unit_types = Counter(polymer).keys()

    for unit_type in unit_types:
        new_polymer = polymer.replace(unit_type.lower(), '').replace(
            unit_type.upper(), '')
        yield len(trigger(new_polymer))


polymer = util.input_lines(5)[0]

print(len(trigger(polymer)))

print(min(improved_polymer_lengths(polymer)))

