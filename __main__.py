"""adventofcode2018."""
import importlib
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Solutions for the puzzles at http://adventofcode.com',
        usage='python -m adventofcode2018 [-h] day_number')
    parser.add_argument('day_number',
                        help="An integer between 1 and 25")
    args = parser.parse_args()

    try:
        importlib.import_module('adventofcode2018.day{i}.day{i}'.format(
            i=args.day_number))
    except ModuleNotFoundError:
        print(('Error: could not find solution for day %s. Did you run python '
              'with the -m flag?') % args.day_number)


if __name__ == '__main__':
    main()
