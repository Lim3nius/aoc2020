#!/usr/bin/env python3

import math
from itertools import count

INPUT = 'input'


def main():
    with open(INPUT, 'r') as fd:
        area_map = [line.strip() for line in fd]

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    res = []
    # part2
    for s in slopes:
        # part 1
        tree_hits = 0
        for (x, y) in zip(count(0, s[0]), count(0, s[1])):
            if y >= len(area_map):
                res.append(tree_hits)
                break

            if x >= len(area_map[y]):
                x = x % len(area_map[y])

            if area_map[y][x] == '#':
                tree_hits += 1

    print('part1 -> ', res[1])
    print('Part2 -> ', math.prod(res))


if __name__ == '__main__':
    main()
