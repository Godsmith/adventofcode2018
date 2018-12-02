import os


def input_lines(day):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_path = f'{dir_path}/day{day}/input.txt'

    with open(input_path) as f:
        return f.readlines()
