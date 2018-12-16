"""This is an ugly brute-force solution since I did not know about
   https://en.wikipedia.org/wiki/Summed-area_table"""


def power_level(x, y, serial_number):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    hundred_digit = int(str(power)[-3])
    return hundred_digit - 5


def square_power(power_levels, x, y, side=3):
    power = 0
    for x1 in range(x, x + side):
        for y1 in range(y, y + side):
            power += power_levels[(x1, y1)]
    return power


def all_sides(x, y):
    return range(1, 302 - max(x, y))


def power_diff_from_one_step_left(power_levels, x, y, side):
    power = 0
    for y1 in range(y, y + side):
        power -= power_levels[(x - 1, y1)]
        power += power_levels[(x + side - 1, y1)]
    return power


def power_diff_from_one_step_up(power_levels, x, y, side):
    power = 0
    for x1 in range(x, x + side):
        power -= power_levels[(x1, y - 1)]
        power += power_levels[(x1, y + side - 1)]
    return power


def largest_power_coordinate(serial_number, any_size=False):
    power_levels = {}
    for x in range(1, 301):
        for y in range(1, 301):
            power_levels[(x, y)] = power_level(x, y, serial_number)

    powers = {}

    sides = range(300, 0, -1) if any_size else [3]
    for side in sides:
        print(side)
        for x in range(1, 301 - side):
            for y in range(1, 301 - side):
                if (x - 1, y, side) in powers:
                    powers[(x, y, side)] = powers[(x - 1, y, side)] + \
                                           power_diff_from_one_step_left(
                                               power_levels, x, y,
                                               side)
                elif (x, y - 1, side) in powers:
                    powers[(x, y, side)] = powers[(x, y - 1, side)] + \
                                           power_diff_from_one_step_up(
                                               power_levels, x, y, side)
                else:
                    powers[(x, y, side)] = square_power(power_levels, x, y,
                                                        side)
    max_val = max(powers.values())
    return [key for key in powers.keys() if powers[key] == max_val]


    # record_power = 0
    # record_power_coordinate = None
    # record_size = 0
    # sides = all_sides if any_size else lambda x, y: [3]
    # for x in range(1, 299):
    #     for y in range(1, 299):
    #         print(x,y, sides(x,y))
    #         for side in sides(x, y):
    #             power = square_power(power_levels, x, y, side)
    #             if power > record_power:
    #                 record_power = power
    #                 record_power_coordinate = (x, y)
    #                 record_size = side
    # return record_power_coordinate + ((record_size,) if any_size else ())


def largest_power_square(serial_number):
    return largest_power_coordinate(serial_number, True)


def main():
    pass
    # print(largest_power_square(8199))


if __name__ == '__main__':
    main()

print(largest_power_coordinate(8199))
print(largest_power_square(8199))
