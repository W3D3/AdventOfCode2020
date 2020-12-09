import itertools

from aocd import data
from aocd import submit


def part_a(data, preamble=25):
    nums = parse_data(data)
    valid, violated_num = check_validity(nums, preamble)
    return violated_num


def part_b(data, preamble=25):
    nums = parse_data(data)
    _, goal_sum = check_validity(nums, preamble)
    sum_set = get_contiguous_set_to_sum(nums, goal_sum)
    return min(sum_set) + max(sum_set)


def parse_data(data):
    return list(map(int, data.strip().split("\n")))


def check_validity(nums, preamble, lookback=None):
    if lookback is None:
        lookback = preamble

    for n in range(preamble, len(nums) - 2):
        to_check = nums[n]

        valid = False
        for n1, n2 in itertools.combinations(nums[n - lookback:n], 2):
            if n1 + n2 == to_check:
                valid = True
                break
        if not valid:
            return False, to_check
    return True


def get_contiguous_set_to_sum(list, goal_sum):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if sum(list[i:j]) > goal_sum:
                break
            elif sum(list[i:j]) == goal_sum:
                return list[i:j]


test_data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

if __name__ == "__main__":
    assert part_a(test_data, 5) == 127
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=9, year=2020)

    assert part_b(test_data, 5) == 62
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=9, year=2020)
