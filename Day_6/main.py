#!/usr/bin/env python3

trans = str.maketrans('\n', ' ')

with open('input', 'r') as fd:
    data = [line for line in fd]

data = ''.join(data).split('\n\n')
data = [g.translate(trans).strip().split() for g in data]


def group_choices(d, operation):
    sets = []
    for g in data:
        s = set(g[0])
        for p in g:
            s = operation(s, set(p))

        sets.append(s)
    return sets


sets = group_choices(data, lambda s1, s2: s1.union(s2))
print('Part1 -> ', sum([len(s) for s in sets]))

sets = group_choices(data, lambda s1, s2: s1.intersection(s2))
print('Part 2 -> ', sum([len(s) for s in sets]))
