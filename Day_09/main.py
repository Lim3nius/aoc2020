#!/usr/bin/env python3

from collections import deque
from itertools import count
from typing import List

with open('input', 'r') as fd:
    data = list(map(int, fd.readlines()))


NUMS=25

usable_numbers = deque(data[:NUMS])
idx = NUMS
invalid = 0


def combine_from(us: List[int], num: int) -> (int, int):
    for i, n0 in enumerate(us):
        n1 = num - n0
        a = us.copy()
        a.remove(n0)
        if (n1 in a):
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
# for l in count(2, 1):
#     for idx in range(len(data) - l):
#         s = data[idx:idx+l]
#         if sum(s) == invalid:
#             print('Part2 -> ', min(s) + max(s))
#             raise StopIteration()

deq = deque([data[0], data[1]])
current_sum = data[0] + data[1]

for d in data[2:]:
    print(deq)
    if current_sum + d == invalid:
        l = list(deq)
        print('Part2 -> ', min(l) + max(l))
        break
    elif current_sum + d < invalid:
        current_sum += d
        deq.append(d)
    else:
        while current_sum + d > invalid:
            current_sum -= deq.popleft()

            if current_sum + d == invalid:
                deq.append(d)
                l = list(deq)
                print('Part2 ->', min(l) + max(l))
                raise StopIteration()
        else:
            deq.append(d)
            current_sum += d
