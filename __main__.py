"""adventofcode2018."""
import importlib
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Solutions for the puzzles at http://adventofcode.com')
    parser.add_argument('day_number',
                        help="An integer between 1 and 25")
    args = parser.parse_args()

    try:
        importlib.import_module('day{i}.day{i}'.format(i=args.day_number))
    except ModuleNotFoundError:
        print('Error: could not find solution for day %s.' % args.day_number)


if __name__ == '__main__':
    main()
