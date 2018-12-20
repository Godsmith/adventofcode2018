from .. import util


class Cart:
    turns = 'LSR'
    delta_from_direction = {'>': (1, 0),
                            'v': (0, 1),
                            '<': (-1, 0),
                            '^': (0, -1)}
    turn_changes = {'/': {'>': '^',
                          'v': '<',
                          '<': 'v',
                          '^': '>'},
                    '\\': {'>': 'v',
                           '^': '<',
                           '<': '^',
                           'v': '>'}}
    intersection_changes = {'L': {'>': '^',
                                  '^': '<',
                                  '<': 'v',
                                  'v': '>'},
                            'R': {'>': 'v',
                                  '^': '>',
                                  '<': '^',
                                  'v': '<'},
                            'S': {'>': '>',
                                  '^': '^',
                                  '<': '<',
                                  'v': 'v'}}

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn_index = 0

    def __repr__(self):
        return f'Cart({self.x}, {self.y}, "{self.direction}", ' \
               f'"{self.turns[self.turn_index]}")'

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y == other.y:
            return self.x < other.x

    def move(self):
        dx, dy = self.delta_from_direction[self.direction]
        self.x += dx
        self.y += dy

    def turn(self, terrain):
        if terrain in ('/', '\\'):
            self.direction = self.turn_changes[terrain][self.direction]
        elif terrain == '+':
            self.direction = self.intersection_changes[self.turns[
                self.turn_index]][self.direction]
            self.turn_index += 1
            self.turn_index %= 3

        elif terrain == ' ':
            raise ValueError('Cart off track')


class Track:

    def __init__(self, state):
        self.latest_crash_location = None
        self._terrain = [list(s) for s in state]
        self.carts = []
        for y, line in enumerate(state):
            for x, char in enumerate(line):
                if char in ('>', 'v', '<', '^'):
                    self.carts.append(Cart(x, y, char))
                    self._terrain[y][x] = self.terrain_from_surroundings(x, y)

    def __str__(self):
        terrain = [list(_list) for _list in self._terrain]
        for cart in self.carts:
            terrain[cart.y][cart.x] = cart.direction
        return '\n'.join([''.join(_list) for _list in terrain])

    def terrain_from_surroundings(self, x, y):
        return '|' if self.terrain(x, y - 1) in ('+', '|') or \
                      self.terrain(x, y+1) in ('+', '|') else '-'

    def terrain(self, x, y):
        if x < 0 or y < 0 or x >= len(self._terrain[0]) or y >= len(
                self._terrain):
            return ' '
        return self._terrain[y][x]

    def tick(self):
        self.carts.sort()
        moved = set()
        while len(moved) < len(self.carts):
            cart = [cart for cart in self.carts if cart not in moved][0]
            other_from_coordinate = {(other.x, other.y): other for other in
                                      self.carts if other != cart}
            if (cart.x, cart.y) in other_from_coordinate:
                other = other_from_coordinate[(cart.x, cart.y)]
                self.latest_crash_location = (cart.x, cart.y)
                self.carts.remove(cart)
                self.carts.remove(other)
                if cart in moved:
                    moved.remove(cart)
                if other in moved:
                    moved.remove(other)
                continue
            cart.move()
            cart.turn(self.terrain(cart.x, cart.y))
            moved.add(cart)
        print(self)
        print(len(self.carts))

    def first_crash(self):
        while not self.latest_crash_location:
            self.tick()
        return self.latest_crash_location

    def last_cart_location(self):
        while len(self.carts) > 1:
            self.tick()
        return self.carts[0].x, self.carts[0].y


lines = util.input_lines(13)

track = Track(lines)
print(track.first_crash())
track = Track(lines)
print(track.last_cart_location())
