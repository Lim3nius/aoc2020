#!/usr/bin/env python3

from collections import deque
from itertools import count

with open('input', 'r') as fd:
    data = list(map(int, fd.readlines()))


NUMS=25

usable_numbers = deque(data[:NUMS])
idx = NUMS
invalid = 0


def combine_from(us, num) -> (int, int):
    for n0 in us:
        n1 = num - n0
        if (n1 in us) and (n1 != n0):
            return n0, n1

    return -1, -1


# Part 1
while idx < len(data):
    curr = data[idx]
    n0, n1 = combine_from(usable_numbers, curr)
    if n0 == -1:
        print('Part1 -> ', curr)
        invalid = curr
        break
    usable_numbers.popleft()
    usable_numbers.append(curr)
    idx += 1


# Part 2
for l in count(2, 1):
    for idx in range(len(data) - l):
        s = data[idx:idx+l]
        if sum(s) == invalid:
            s = sorted(s)
            print('Part2 -> ', s)
            print(s[0] + s[-1])
            raise StopIteration()
