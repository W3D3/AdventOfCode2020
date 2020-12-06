from aocd import data
from aocd import submit
import re


def part_a(data):
    groups = list(data.strip().split("\n\n"))

    cnt = 0
    for group in groups:
        answers = group.split("\n")
        cnt += count_group_answers_anyone(answers)

    return str(cnt)

def part_b(data):
    groups = list(data.strip().split("\n\n"))

    cnt = 0
    for group in groups:
        answers = group.split("\n")
        cnt += count_group_answers_everyone(answers)

    return str(cnt)

def count_group_answers_anyone(answers):
    group_answers = set()
    for answer in answers:
        for char in answer:
            group_answers.add(char)
    return len(group_answers)

def count_group_answers_everyone(answers):
    group_answers = set.intersection(*map(set, answers))
    return len(group_answers)

test_data = """
abc

a
b
c

ab
ac

a
a
a
a

b
"""

if __name__ == "__main__":
    assert part_a(test_data) == "11"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=6, year=2020)

    assert part_b(test_data) == "6"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=6, year=2020)
