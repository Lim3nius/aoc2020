#!/usr/bin/env python3

with open('input', 'r') as fd:
    z = 0
    cells = set()
    for y, line in enumerate(fd):
        for x, c in enumerate(line.strip()):
            if c == '#':
                cells.add((z, y, x))

origin = cells.copy()


def recursive_index_change(pos):
    if len(pos) == 1:
        return [(pos[0] - 1,), (pos[0] + 0,), (pos[0] + 1,)]

    res = []
    changes = recursive_index_change(pos[1:])
    for i in [-1, 0, 1]:
        for c in changes:
            res.append((pos[0] + i, *c))

    return res


def neighbors(pos):
    res = []
    for z in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if x == 0 and y == 0 and z == 0:
                    continue
                res.append(tuple((pos[0] + z, pos[1] + y, pos[2] + x)))
    return res


def convay_cube_step(alive):
    new_cells = {}
    for a in alive:
        neigh = recursive_index_change(a)
        del neigh[len(neigh) // 2]  # remove indentic element (always in middle)
        for n in neigh:
            if n in new_cells:
                new_cells[n] += 1
            else:
                new_cells[n] = 1

    new_alive = set()
    for c in new_cells.keys():
        if c in alive:
            if new_cells[c] in [2, 3]:
                new_alive.add(c)
        else:
            if new_cells[c] == 3:
                new_alive.add(c)
    return new_alive


for _ in range(6):
    cells = convay_cube_step(cells)

print('Part 1 -> ', len(cells))

# transform to 4th dimension
origin = [(0,) + c for c in origin]
cells = origin

for _ in range(6):
    cells = convay_cube_step(cells)

print('Part 2 -> ', len(cells))
