from aocd import data
from aocd import submit
import timeit

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

def part_a_set(data):
    nums = set(map(int, data.strip().split("\n")))
    for num in nums:
        diff = 2020 - num
        if diff in nums:
            return str(num * diff)
    return None

def part_b_set(data):
    nums = set(map(int, data.strip().split("\n")))
    for num in nums:
        for num2 in nums:
            diff = 2020 - num - num2
            if diff in nums:
                return str(num * num2 * diff)
    return None


test_data = """\
1721
979
366
299
675
1456
"""

def timing_differences():
    loops = 10000
    print('part_a_set', timeit.timeit('part_a_set(data)', number=loops, globals=globals()))
    print('part_a', timeit.timeit('part_a(data)', number=loops, globals=globals()))

    print('part_b_set', timeit.timeit('part_b_set(data)', number=loops, globals=globals()))
    print('part_b', timeit.timeit('part_b(data)', number=loops, globals=globals()))

if __name__ == "__main__":
    # timing_differences()

    assert part_a_set(test_data) == "514579"
    assert part_b_set(test_data) == "241861950"
    solution_a = part_a_set(data)
    print(solution_a)
    # submit(solution_a, part="a", day=1, year=2020)
    solution_b = part_b_set(data)
    print(solution_b)
    # submit(solution_b, part="b", day=1, year=2020)

