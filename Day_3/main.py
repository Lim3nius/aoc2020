#!/usr/bin/env python3

import math

INPUT = 'input'


def main():
    with open(INPUT, 'r') as fd:
        area_map = [line.strip() for line in fd]

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    res = []
    # part2
    for s in slopes:
        # part 1
        pos = [0, 0]
        tree_hits = 0
        while True:
            x = pos[0]
            if x >= len(area_map[pos[1]]):
                x = x % len(area_map[pos[1]])

            if area_map[pos[1]][x] == '#':
                tree_hits += 1

            pos[0] += s[0]
            pos[1] += s[1]

            if pos[1] >= len(area_map):
                res.append(tree_hits)
                break

    print('part1 -> ', res[1])
    print('Part2 -> ', math.prod(res))


if __name__ == '__main__':
    main()
