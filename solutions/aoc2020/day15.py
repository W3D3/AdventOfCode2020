import itertools

from aocd import data
from aocd import submit
from parse import parse


def part_a(data):
    starting_nums = parse_data(data)
    history = []

    for num in starting_nums:
        history.append(num)

    for i in range(len(starting_nums)+1, 2021):
        print(history)
        last_spoken_index = find_last(history[:-1], history[-1])
        if last_spoken_index >= 0:
            diff = (i - 1) - (last_spoken_index + 1) # -1 as we are analyzing the last turn, +1 as we are 1 indexed in turns
            # print(last_spoken_index+1, i - 1, "=", diff)
            history.append(diff)
            print(i, "speaks", diff)
        else:
            history.append(0)

    return history[-1]


def find_last(list, element):
    for r_idx, elt in enumerate(reversed(list)):
        if elt == element:
            return len(list) - 1 - r_idx
    return -1

def part_b(data):
    return None

def parse_data(data):
    return list(map(int, data.strip().split(",")))


test_data = """
0,3,6
"""

if __name__ == "__main__":
    part_a(test_data)
    assert part_a(test_data) == 436
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=15, year=2020)

    # assert part_b(test_data) == 0
    # solution_b = part_b(data)
    # submit(solution_b, part="b", day=15, year=2020)
