"""day1"""
import itertools
import os
from .. import util

def first_duplicate_frequency(ints):
    freq = 0
    freqs = set()
    for i in itertools.cycle(ints):
        freq += i
        if freq in freqs:
            return freq
        freqs.add(freq)


dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/input.txt') as f:
    ints = [int(i) for i in util.input_lines(1)]
    print(sum(ints))
    print(first_duplicate_frequency(ints))

# Test
# print(first_duplicate_frequency([1, -2, 3, 1]))
