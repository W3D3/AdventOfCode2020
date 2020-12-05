import math

from aocd import data
from aocd import submit


def part_a(data):
    lines = list(data.strip().split("\n"))
    ids = get_boarding_ids(lines)
    return str(max(ids))


def part_b(data):
    lines = list(data.strip().split("\n"))
    ids = sorted(get_boarding_ids(lines))

    for current, next in zip(ids, ids[1:]):
        if not (next - current == 1):
            return str(current + 1)

    return None


def get_boarding_ids(lines):
    ids = []
    for line in lines:
        row = find_row(line)
        col = find_col(line)
        ids.append(row * 8 + col)
    return ids


def find_row(info):
    min = 0
    max = 127
    for i in info[:7]:
        if i == 'F':
            # take lower half
            max = math.floor((min + max) / 2)
        if i == 'B':
            # take upper half
            min = math.ceil((min + max) / 2)
    assert min == max
    return min


def find_col(info):
    min = 0
    max = 7
    for i in info[7:10]:
        if i == 'L':
            # take lower half
            max = math.floor((min + max) / 2)
        if i == 'R':
            # take upper half
            min = math.ceil((min + max) / 2)
    assert min == max
    return min


test_pass = "FBFBBFFRLR"

test_data = """\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

if __name__ == "__main__":
    assert find_row(test_pass) == 44
    assert find_col(test_pass) == 5
    assert part_a(test_data) == "820"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=5, year=2020)

    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=5, year=2020)
