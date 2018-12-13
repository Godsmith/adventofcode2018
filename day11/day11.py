def power_level(x, y, serial_number):
    rack_id = x + 10
    power = rack_id * y
    power += serial_number
    power *= rack_id
    hundred_digit = int(str(power)[-3])
    return hundred_digit - 5


def square_power(power_levels, x, y):
    power = 0
    for x1 in range(x, x+3):
        for y1 in range(y, y+3):
            power += power_levels[(x1, y1)]
    return power


def largest_power_coordinate(serial_number):
    power_levels = {}
    for x in range(1, 301):
        for y in range(1, 301):
            power_levels[(x, y)] = power_level(x, y, serial_number)

    record_power = 0
    record_power_coordinate = None
    for x in range(1, 299):
        for y in range(1, 299):
            power = square_power(power_levels, x, y)
            if power > record_power:
                record_power = power
                record_power_coordinate = (x,y)
    return record_power_coordinate

print(largest_power_coordinate(8199))
