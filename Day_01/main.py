#!/usr/bin/env python3

from typing import Dict

FILE = 'input'
TARGET = 2020


def findNumbersSummingTo(dct: Dict[int, bool], target: int) -> (int, int):
    for l1 in dct.keys():
        l2 = target - l1
        if dct.get(l2, False):
            return (l1, l2)
    return (0, 0)


def main():
    with open(FILE, 'r') as fd:
        lines = fd.readlines()
    dct = {int(x): True for x in lines}

    # Part 1
    n1, n2 = findNumbersSummingTo(dct, TARGET)
    print('Part1 -> ', n1 * n2)

    # Part2
    for l1 in dct.keys():
        l2, l3 = findNumbersSummingTo(dct, TARGET - l1)
        if l2 != 0 and l3 != 0:
            print('Part2 -> ', l1 * l2 * l3)
            break


if __name__ == '__main__':
    main()
