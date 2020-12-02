from aocd import data
from aocd import submit


def part_a(data):
    lines = list(data.strip().split("\n"))
    valid = 0
    for line in lines:
        pw_policy, pw = line.split(": ")
        min_max, policy_char = pw_policy.split(" ")
        min, max = min_max.split("-")
        if int(max) >= pw.count(policy_char) >= int(min):
            valid += 1

    return str(valid)


def part_b(data):
    lines = list(data.strip().split("\n"))
    valid = 0
    for line in lines:
        pw_policy, pw = line.split(": ")
        i_j, policy_char = pw_policy.split(" ")
        i, j = i_j.split("-")
        i = int(i) - 1
        j = int(j) - 1
        valid += ((pw[int(i)] == policy_char) ^ (pw[int(j)] == policy_char))
    return str(valid)


test_data = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

if __name__ == "__main__":
    assert part_a(test_data) == "2"
    solution_a = part_a(data)
    print(solution_a)
    submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data) == "1"
    solution_b = part_b(data)
    print(solution_b)
    submit(solution_b, part="b", day=2, year=2020)
