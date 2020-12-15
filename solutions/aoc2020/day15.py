from aocd import data
from aocd import submit

def part_a(data):
    return get_number_spoken_at(parse_data(data), 2020)


def part_b(data):
    return get_number_spoken_at(parse_data(data), 30_000_000)


def find_last(list, element):
    for r_idx, elt in enumerate(reversed(list)):
        if elt == element:
            return len(list) - 1 - r_idx
    return -1


def get_number_spoken_at(starting_nums, index):
    dict = {}
    last_spoken = None

    for idx, num in enumerate(starting_nums):
        dict[num] = (idx + 1, None)  # Hold the two last indices who said this number

    last_spoken = starting_nums[-1]
    for i in range(len(starting_nums) + 1, index + 1):
        first_idx, second_idx = dict[last_spoken]  # get last spoken idx
        if second_idx is None:
            # this was the first occurence!
            spoken = 0
            update_tuple(dict, spoken, i)
        else:
            diff = second_idx - first_idx
            spoken = diff
            update_tuple(dict, spoken, i)
        last_spoken = spoken

    return last_spoken


def update_tuple(dict, spoken, new_idx):
    if spoken not in dict:
        dict[spoken] = (new_idx, None)

    first, second = dict[spoken]
    if second is None:
        dict[spoken] = (first, new_idx)
    else:
        dict[spoken] = (second, new_idx)


def parse_data(data):
    return list(map(int, data.strip().split(",")))


test_data = """
0,3,6
"""

if __name__ == "__main__":
    assert part_a(test_data) == 436
    # solution_a = part_a(data)
    # submit(solution_a, part="a", day=15, year=2020)

    assert part_b(test_data) == 175594
    # solution_b = part_b(data)
    # submit(solution_b, part="b", day=15, year=2020)
