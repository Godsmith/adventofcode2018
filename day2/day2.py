from collections import Counter
import itertools

from .. import util

lines = util.input_lines(2)

# Part 1
twos = 0
threes = 0
for line in lines:
    c = Counter(line)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1
print(twos * threes)

# Part 2
for id1, id2 in itertools.combinations(lines, 2):
    diffcount = 0
    same = ''
    for char1, char2 in zip(id1, id2):
        if char1 == char2:
            same += char1
        else:
            diffcount += 1
        if diffcount == 2:
            break
    if diffcount == 1:
        print(same)
        break


