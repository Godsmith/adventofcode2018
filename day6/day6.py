from collections import Counter
from .. import util


def neighbor_coordinates(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


lines = util.input_lines(6)

# lines = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9""".splitlines()

coordinates = [tuple(map(int, line.split(','))) for line
               in lines]

id_from_coordinate = {coordinate: i for i, coordinate in enumerate(coordinates)}

min_x = min(c[0] for c in coordinates)
max_x = max(c[0] for c in coordinates)
min_y = min(c[1] for c in coordinates)
max_y = max(c[1] for c in coordinates)


def is_on_border(x, y):
    return x in (min_x, max_x) or y in (min_y, max_y)


def distance(coordinate, x, y):
    return abs(coordinate[0] - x) + abs(coordinate[1] - y)


def smallest_value_is_unique(dict_):
    return list(dict_.values()).count(min(dict_.values())) == 1


def key_for_largest_value(dict_):
    return [key for key, value in dict_.items()
            if value == max(dict_.values())][0]


def key_for_smallest_value(dict_):
    return [key for key, value in dict_.items()
            if value == min(dict_.values())][0]


locations = {}
disqualified_coordinates = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distance_from_coordinate = {coordinate: distance(coordinate, x, y) for
                                    coordinate in coordinates}
        coordinate = key_for_smallest_value(distance_from_coordinate)
        if smallest_value_is_unique(distance_from_coordinate):
            locations[(x, y)] = coordinate
        else:
            locations[(x, y)] = '.'

        if is_on_border(x, y):
            disqualified_coordinates.add(coordinate)

# letter_from_coordinate = {(1, 1): 'A', (1, 6): 'B', (8, 3): 'C',
#                           (3, 4): 'D', (5, 5): 'E', (8, 9): 'F',
#                           '.': '.'}

# for y in range(min_y, max_y + 1):
#     for x in range(min_x, max_x + 1):
#
#         #print(letter_from_coordinate[locations[(x, y)]], end='')
#         print(locations[(x, y)], end='')
#     print()

coordinate_counter = Counter(locations.values())
for coordinate in disqualified_coordinates:
    del coordinate_counter[coordinate]

print(max(coordinate_counter.values()))

safe_location_count = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        total_distance = sum(distance(coordinate, x, y) for
                             coordinate in coordinates)
        if total_distance < 10000:
            safe_location_count += 1
print(safe_location_count)

