#!/usr/bin/env python3

from typing import List
from math import prod

with open('input', 'r') as fd:
    data = [int(n) for n in fd]

data = sorted(data)
differences = [0, 0, 0, 0]
data = [0] + data

for i0 in range(0, len(data)-1):
    d = data[i0+1] - data[i0]
    differences[d] += 1

differences[3] += 1

print('Part1 -> ', differences[1] * differences[3])


def valid_combinations(lt: int, ut: int, nums: List[int]) -> int:
    if len(nums) == 0:
        return 1

    valid = list(filter(lambda x: True if (x[1] - lt) in [1, 2, 3] else False, enumerate(nums)))
    if len(valid) == 0:
        return 1

    cnt = 0
    for (idx, v) in valid:
        nn = nums[:]
        del nn[idx]
        cnt += valid_combinations(v, ut, nn)

    if ut - lt <= 3:
        cnt += 1

    return cnt

# Part 2
changeable_indexes = []
for i in range(1, len(data)-1):
    if ((0 < data[i+1] - data[i] < 3) and
            (0 < data[i] - data[i-1] < 3)):
        changeable_indexes.append(i)

# edge cases
if changeable_indexes[0] == 0:
    changeable_indexes = changeable_indexes[1:]

if changeable_indexes[-1] == len(data)-1:
    changeable_indexes = changeable_indexes[:-1]

sequences = []
tl = []
last_val = 0

for i in range(len(changeable_indexes)):
    if changeable_indexes[i] - last_val == 1:
        tl.append(changeable_indexes[i])
    else:
        sequences.append(tl)
        tl = [changeable_indexes[i]]
    last_val = changeable_indexes[i]

sequences.append(tl)

counts = []
for s in sequences:
    if len(s) == 0:
        continue
    lt = data[s[0]-1]
    ut = data[s[-1]+1]
    counts.append(valid_combinations(lt, ut, [data[i] for i in s]))

print('Part2 -> ', prod(counts))
