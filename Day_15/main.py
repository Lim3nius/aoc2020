#!/usr/bin/env python3

import time

first_time = [-1 for _ in range(30_000_000)]
loaded = 0
last = 0

with open('input', 'r') as fd:
    for i, n in enumerate(map(int, fd.readline().split(',')), start=1):
        first_time[n] = i
        loaded += 1
        last = n

visited = [-1 for _ in range(30_000_000)]

idx = loaded
current_num = last
t0 = time.time()
while True:
    if first_time[current_num] != -1:
        idx0 = first_time[current_num]
        if idx == idx0:
            new_num = 0
        else:
            diff = idx - idx0
            new_num = diff
            first_time[current_num] = -1
            visited[current_num] = idx
    elif visited[current_num] != -1:
        diff = idx - visited[current_num]
        new_num = diff
        visited[current_num] = idx
    else:
        first_time[current_num] = idx
        new_num = 0
    current_num = new_num
    idx += 1

    if idx == 2020:
        part1 = new_num
        print('Part1 in ', time.time() - t0, ' s')
    if idx == 30_000_000:
        print('Part2 in ', time.time() - t0, ' s')
        part2 = new_num
        break

# part1, part2 = foo()
print('Part1 -> ', part1)
print('Part2 -> ', part2)
