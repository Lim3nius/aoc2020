#!/usr/bin/env python3

import time

with open('input', 'r') as fd:
    first_time = {n: i for i, n in
                  enumerate(map(int, fd.readline().split(',')), start=1)}

visited = {}
current_num = list(first_time.keys())[-1]
idx = len(first_time)
part1 = 0

t0 = time.time()
while True:
    if current_num in first_time:
        idx0 = first_time[current_num]
        if idx == idx0:
            new_num = 0
        else:
            diff = idx - idx0
            new_num = diff
            first_time.pop(current_num)
            visited[current_num] = idx
    elif current_num in visited:
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
        break

print('Part1 -> ', part1)
print('Part2 -> ', current_num)
