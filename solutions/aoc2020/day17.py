import itertools
import operator

from aocd import data
from aocd import submit

from parse import parse
import numpy as np


def part_a(data):
    active_coords = parse_data(data)
    print_3d_coords(active_coords)

    for i in range(0, 6):
        active_coords = simulate_step(active_coords)
        # print_3d_coords(active_coords)

    return len(active_coords)


def part_b(data):
    active_coords = parse_data_b(data)

    for i in range(0, 6):
        active_coords = simulate_step(active_coords)

    return len(active_coords)


def simulate_step(active_coords):
    next_coords = set()
    inactive_coords = set()
    for coord in active_coords:
        # add the inactive neighbors to our neighborhood of inactive plas
        inactive_coords = inactive_coords.union(get_neighbors(coord).difference(active_coords))
        coord_neighbor_count = count_neighbors(coord, active_coords)
        # let active coords with neighbor count 2 and 3 survive
        if coord_neighbor_count == 2 or coord_neighbor_count == 3:
            next_coords.add(coord)

    # check all currently inactive that are part of our neighborhood
    for inactive in inactive_coords:
        # let inactive coords with neighbor count 3 be alive
        if count_neighbors(inactive, active_coords) == 3:
            next_coords.add(inactive)

    return next_coords

def print_3d_coords(coords):
    min_z, max_z = get_limits(coords, 2)
    min_y, max_y = get_limits(coords, 1)
    min_x, max_x = get_limits(coords, 0)
    for z in range(min_z, max_z + 1):
        print("z = ", z)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y, z) in coords:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()


def count_neighbors(coord, active_coords):
    count = 0
    for neighbor in get_neighbors(coord):
        count += neighbor in active_coords
    return count


def get_limits(coords, tuple_index):
    all_index_vals = [coord[tuple_index] for coord in coords]
    return min(all_index_vals), max(all_index_vals)


def get_neighbors(coord):
    dimension = len(coord)
    directions = list(itertools.product([-1, 1, 0], repeat=dimension))
    directions.remove((0,) * dimension)
    return set([add_tuples(coord, direction) for direction in directions])


def add_tuples(a, b):
    return tuple(map(operator.add, a, b))


def parse_data(data):
    lines = data.strip().split("\n")
    initial_coords = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                initial_coords.add((x, y, 0))

    return initial_coords


def parse_data_b(data):
    lines = data.strip().split("\n")
    initial_coords = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                initial_coords.add((x, y, 0, 0))

    return initial_coords


test_data = """
.#.
..#
###
"""

if __name__ == "__main__":
    assert part_a(test_data) == 112
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=17, year=2020)

    assert part_b(test_data) == 848
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=17, year=2020)
