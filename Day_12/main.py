#!/usr/bin/env python3


with open('input', 'r') as fd:
    instructions = [(line[0], int(line.strip()[1:])) for line in fd]


class Ship:
    Orientation = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }
    OrientationOrder = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.orientation = Ship.Orientation['E']
        self.orientation_name = 'E'
        self.pos = [0, 0]
        self.waypoint = [10, 1]

    def move(self, instruction):
        direction, distance = instruction
        if Ship.Orientation.get(direction):
            self.pos = [p + c * distance
                        for p, c in zip(self.pos, Ship.Orientation[direction])]
        elif direction == 'F':
            self.pos = [p + c * distance
                        for p, c in zip(self.pos, self.orientation)]
        elif direction == 'R':
            self.change_orientation(self.orientation_name, distance // 90)
        elif direction == 'L':
            self.change_orientation(self.orientation_name, -(distance // 90))

    def change_orientation(self, orientation, idx_change):
        idx = Ship.OrientationOrder.index(orientation)
        idx += idx_change
        self.orientation_name = Ship.OrientationOrder[idx % len(Ship.OrientationOrder)]
        self.orientation = Ship.Orientation[self.orientation_name]

    def waypoint_move(self, instruction):
        direction, distance = instruction
        if Ship.Orientation.get(direction):
            self.waypoint = [p + c * distance
                             for p, c in zip(self.waypoint, Ship.Orientation[direction])]
        elif direction == 'F':
            self.pos = [p + c * distance
                        for p, c in zip(self.pos, self.waypoint)]
        elif direction == 'R':
            self.rotate_waypoint(distance)
        elif direction == 'L':
            self.rotate_waypoint(-distance)

    def rotate_waypoint(self, change):
        if change < 0:
            change += 360

        x, y = self.waypoint

        if change == 0:
            self.waypoint = [x, y]
        elif change == 90:
            self.waypoint = [y, -x]
        elif change == 180:
            self.waypoint = [-x, -y]
        elif change == 270:
            self.waypoint = [-y, x]
        elif change == 360:
            self.waypoint = [x, y]


for part, move in [[1, Ship.move], [2, Ship.waypoint_move]]:
    sh = Ship()
    for inst in instructions:
        move(sh, inst)

    print('Part {} -> {}'.format(part, sum(map(abs, sh.pos))))
