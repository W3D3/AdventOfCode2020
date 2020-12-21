import re

from aocd import data
from aocd import submit
from lark import Lark


def part_a(data):
    grammar, lines = parse_data(data)

    return count_valid(grammar, lines)


def part_b(data):

    grammar, lines = parse_data(data)

    grammar = grammar\
        .replace("8: 42", "8: 42 | 42 8")\
        .replace("11: 42 31", "11: 42 31 | 42 11 31")
    return count_valid(grammar, lines)

def count_valid(grammar, lines):
    sum_valid = 0
    rules = "?start: r0\n" + re.sub(r'([0-9]+)', r'r\1', grammar)
    calc_parser = Lark(rules, parser='earley')
    check = calc_parser.parse
    for line in lines:
        try:
            check(line)
            sum_valid += 1
        except Exception:
            pass

    return sum_valid

def parse_data(data):
    grammar, lines = data.strip().split("\n\n")
    lines = lines.split("\n")
    return grammar, lines


test_data = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

test_data_complex = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""


if __name__ == "__main__":
    assert part_a(test_data) == 2
    solution_a = part_a(data)
    submit(solution_a, part="a", day=19, year=2020)

    assert part_a(test_data_complex) == 3
    assert part_b(test_data_complex) == 12
    solution_b = part_b(data)
    submit(solution_b, part="b", day=19, year=2020)
