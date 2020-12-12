import math

import numpy as np
from aocd import data, submit


def part_a(data):
    pos = np.array([0, 0])
    directions = {
        'N': np.array([0, 1]),
        'E': np.array([1, 0]),
        'S': np.array([0, -1]),
        'W': np.array([-1, 0]),
        'F': np.array([1, 0])  # forward is east on the beginning
    }

    lines = parse_data(data)
    for line in lines:
        action, value = line[:1], int(line[1:])
        if action == 'R':
            directions['F'] = rotate(directions['F'], value, clockwise=True)
        elif action == 'L':
            directions['F'] = rotate(directions['F'], value, clockwise=False)
        else:
            pos = pos + directions[action] * value
    x, y = pos
    return int(abs(x) + abs(y))


def part_b(data):
    pos = np.array([0, 0])
    directions = {
        'N': np.array([0, 1]),
        'E': np.array([1, 0]),
        'S': np.array([0, -1]),
        'W': np.array([-1, 0]),
        'F': np.array([10, 1])  # waypoints starts at 10, 1
    }

    lines = parse_data(data)
    for line in lines:
        action, value = line[:1], int(line[1:])
        if action == 'R':
            directions['F'] = rotate(directions['F'], value, clockwise=True)
        elif action == 'L':
            directions['F'] = rotate(directions['F'], value, clockwise=False)
        elif action == 'F':
            # move the ship towards the waypoint
            pos = pos + directions[action] * value
        else:
            directions['F'] = directions['F'] + directions[action] * value
    x, y = pos
    return int(abs(x) + abs(y))


def rotate(vector, angle, clockwise=False):
    """ Rotate a point around the origin (0, 0)"""
    if clockwise:
        angle = 360 - angle
    angle = math.radians(angle)
    x, y = vector
    x2 = x * math.cos(angle) - y * math.sin(angle)
    y2 = x * math.sin(angle) + y * math.cos(angle)
    return np.array([round(x2, 0), round(y2, 0)])


def parse_data(data):
    return list(data.strip().split("\n"))


test_data = """
F10
N3
F7
R90
F11
"""

if __name__ == "__main__":
    assert part_a(test_data) == 25
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=12, year=2020)

    assert part_b(test_data) == 286
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=12, year=2020)
