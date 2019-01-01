def turn_order_key(unit):
    return (unit.y, unit.x)


class Game():
    def __init__(self, strings):
        self.walls = {}
        self.units = []
        for row, string in strings:
            for column, character in string:
                if character == '#':
                    self.walls[(column, row)] = True
                elif character == 'G':
                    self.units.append(Goblin(column, row))
                elif character == 'E':
                    self.units.append(Elf(column, row))

    def do_round(self):
        self.units.sort(key=turn_order_key)
        for unit in self.units:
            targets = unit.targets(self.units)
            


class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def targets(self, units):
        return [unit for unit in units if isinstance(unit, self.enemy)]

    def adjacent_positions(self):
        return {(self.x -1, self.y),
                (self.x + 1, self.y),
                (self.x, self.y - 1),
                (self.x, self.y + 1)}


class Elf(Unit):
    pass


class Goblin(Unit):
    pass


Elf.enemy = Goblin
Goblin.enemy = Elf
