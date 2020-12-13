#!/usr/bin/env python3

from typing import List, Tuple


with open('input', 'r') as fd:
    grid = [list(line.strip()) for line in fd]


def print_grid(grid):
    for line in grid:
        print(''.join(line))


def new_far_adj_point_state(xo: int, yo: int, grid: List[List[str]]) -> str:
    if grid[yo][xo] == '.':
        return '.'

    directions = [-1, 0, 1]
    occupied, empty = 0, 0
    # x, y = xo, yo
    for i, j in ((i, j) for i in directions for j in directions):
        if i == 0 and j == 0:
            continue
        x, y = xo+i, yo+j
        while ((0 <= y < len(grid)) and (0 <= x < len(grid[0]))):
            if grid[y][x] == 'L':
                empty += 1
                break
            elif grid[y][x] == '#':
                occupied += 1
                break
            x, y = x+i, y+j

    if grid[yo][xo] == 'L' and occupied == 0:
        return '#'
    elif grid[yo][xo] == '#' and occupied >= 5:
        return 'L'
    else:
        return grid[yo][xo]


def new_adjacent_point_state(xo: int, yo: int, grid: List[List[str]]) -> str:
    if grid[yo][xo] == '.':
        return '.'

    directions = [-1, 0, 1]
    occupied, empty = 0, 0
    for i, j in ((i, j) for i in directions for j in directions):
        if i == 0 and j == 0:
            continue
        x, y = xo+i, yo+j
        if ((0 <= y < len(grid)) and (0 <= x < len(grid[0]))):
            if grid[y][x] == 'L':
                empty += 1
            elif grid[y][x] == '#':
                occupied += 1

    if grid[yo][xo] == 'L' and occupied == 0:
        return '#'
    elif grid[yo][xo] == '#' and occupied >= 4:
        return 'L'
    else:
        return grid[yo][xo]


def grid_iteration(grid: List[List[str]], state_gen) -> Tuple[List[List[str]], int]:
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    changes = 0

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s = state_gen(x, y, grid)
            new_grid[y][x] = s

            if s != grid[y][x]:
                changes += 1

    return new_grid, changes


changes = 1
in_grid = grid[:]

for part, gen in [[1, new_adjacent_point_state], [2, new_far_adj_point_state]]:
    changes = 1
    grid = in_grid[:]
    while changes > 0:
        grid, changes = grid_iteration(grid, gen)
        print('Changes :', changes)

    occupied = sum([len(list(filter(lambda x: x == '#', line))) for line in grid])
    print(f'Part {part} -> {occupied}')
