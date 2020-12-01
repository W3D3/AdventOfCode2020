from aocd import data
from aocd import submit

def part_a(data):
    nums = list(map(int, data.strip().split("\n")))
    for i in range(0, len(nums)):
        if nums[i] < 2020:
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == 2020:
                    return str(nums[i] * nums[j])
    return None


def part_b(data):
    nums = list(map(int, data.strip().split("\n")))
    for i in range(0, len(nums)):
        if nums[i] < 2020:
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < 2020:
                    for k in range(j+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == 2020:
                            return str(nums[i] * nums[j] * nums[k])
    return None


test_data = """\
1721
979
366
299
675
1456
"""


if __name__ == "__main__":
    assert part_a(test_data) == "514579"
    assert part_b(test_data) == "241861950"
    solution_a = part_a(data)
    print(solution_a)
    submit(solution_a, part="a", day=1, year=2020)
    solution_b = part_b(data)
    print(solution_b)
    submit(solution_b, part="b", day=1, year=2020)

