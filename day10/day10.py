from .. import util


class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def step(self):
        self.x += self.dx
        self.y += self.dy

    def step_backwards(self):
        self.x -= self.dx
        self.y -= self.dy

    def __repr__(self):
        return 'Point(%s, %s, %s, %s)' % (self.x, self.y, self.dx, self.dy)


def width_and_height(points):
    xs = [point.x for point in points]
    ys = [point.y for point in points]
    width = max(xs) - min(xs) + 1
    height = max(ys) - min(ys) + 1
    return width, height


def translate_to_0(points):
    xs = [point.x for point in points]
    ys = [point.y for point in points]
    min_x = min(xs)
    min_y = min(ys)

    for point in points:
        point.x -= min_x
        point.y -= min_y


def print_array(points):
    array = []
    width, height = width_and_height(points)
    for y in range(height):
        array.append(['.'] * width)
    for point in points:
        array[point.y][point.x] = 'X'
    for line in array:
        for char in line:
            print(char, end='')
        print()


def print_at_smallest_height_and_width(points):
    width_plus_height = 100000000000
    time = 0
    while True:
        time += 1
        for point in points:
            point.step()
        new_width_plus_height = sum(width_and_height(points))
        if new_width_plus_height > width_plus_height:
            for point in points:
                point.step_backwards()
            translate_to_0(points)
            print_array(points)
            print(time - 1)
            break
        width_plus_height = new_width_plus_height


# load points from list
# points = [Point(2, 0, -1, 0), Point(-3, 1, 1, 0)]
points = []

for line in util.input_lines(10):
    x = int(line.split('<')[1].split(',')[0])
    y = int(line.split(',')[1].split('>')[0])
    dx = int(line.split('<')[2].split(',')[0])
    dy = int(line.split(',')[2].split('>')[0])
    points.append(Point(x, y, dx, dy))

print_at_smallest_height_and_width(points)
