#!/usr/bin/env python3

from itertools import count

with open('input', 'r') as fd:
    data = fd.readlines()

buses = data[1].split(',')
timestamp = int(data[0])

# tuple bus id, offset
buses_with_offsets = [(int(b[1]), b[0]) for b in enumerate(buses) if b[1] != 'x']
fixed_buses = [int(b) for b in buses if b != 'x']

wait_times = list(map(lambda x: (min(x - (timestamp % x), x), x), fixed_buses))
time, id = min(wait_times, key=lambda e: e[0])
print('Part 1 -> ', time * id)


# Part 2
temp = 0
step = 1
for bus, off in buses_with_offsets:
    for cur in count(temp, step):
        if (cur + off) % bus == 0:
            temp = cur
            step *= bus
            break

print('Part 2 ->', temp)
