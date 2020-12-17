import math
from functools import reduce

from aocd import data, submit


def part_a(data):
    time, ids = parse_data(data)
    min_diff = math.inf
    best_bus = -1
    for id in ids:
        diff = id - (time % id)
        if diff < min_diff:
            min_diff = diff
            best_bus = id

    return best_bus * min_diff


def part_b(data):
    _, ids = parse_data_with_x(data)
    n = []
    a = []
    for idx, id in enumerate(ids):
        if id != "x":
            a.append(int(id) - idx)
            n.append(int(id))

    return chinese_remainder(n, a)


def parse_data(data):
    leave_time, busses = data.strip().split("\n")
    busses = busses.split(",")
    busses = [int(bus) for bus in busses if bus != "x"]
    return int(leave_time), busses


def parse_data_with_x(data):
    leave_time, busses = data.strip().split("\n")
    busses = busses.split(",")
    return int(leave_time), busses


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


test_data = """
939
7,13,x,x,59,x,31,19
"""

test_data_small = """
1
17,x,13,19
"""

if __name__ == "__main__":
    assert part_a(test_data) == 295
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=13, year=2020)

    assert part_b(test_data_small) == 3417
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=13, year=2020)
