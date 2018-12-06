from collections import Counter
from .. import util


def coordinates_from_claim(claim: str):
    offset_x, offset_y = map(int, claim.replace(':', '').split(' ')[2].split(
        ','))
    width, height = map(int, claim.split(' ')[3].split('x'))

    for x in range(offset_x, offset_x + width):
        for y in range(offset_y, offset_y + height):
            yield (x, y)

def id(claim: str):
    return claim.split(' ')[0]

claims = Counter()
lines = util.input_lines(3)
for line in lines:
    for coordinate in coordinates_from_claim(line):
        claims[coordinate] += 1

print(len([value for value in claims.values() if value > 1]))

for line in lines:
    for coordinate in coordinates_from_claim(line):
        if claims[coordinate] > 1:
            break
    else:
        print(id(line))
        break
