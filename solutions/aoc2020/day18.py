from aocd import data
from aocd import submit

from lark import Lark, Transformer, v_args

calc_grammar_left_to_right = """
    ?start: anyop         -> calc
    ?anyop: atom
        | anyop "*" atom   -> mul
        | anyop "+" atom      -> add
    ?atom: NUMBER           -> number
         | "(" anyop ")"
    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

calc_grammar_inversed = """
    ?start: product         -> calc
    ?product: sum
        | sum "*" product   -> mul
    ?sum: atom
        | sum "+" atom      -> add
    ?atom: NUMBER           -> number
         | "(" product ")"
    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""

def part_a(data):
    sum_results = 0
    calc_parser = Lark(calc_grammar_left_to_right, parser='lalr', transformer=CalculateTree())
    calc = calc_parser.parse
    for line in parse_data(data):
        result = calc(line)
        sum_results += result.children[0]
    return int(sum_results)


def part_b(data):
    sum_results = 0
    calc_parser = Lark(calc_grammar_inversed, parser='lalr', transformer=CalculateTree())
    calc = calc_parser.parse

    for line in parse_data(data):
        result = calc(line)
        sum_results += result.children[0]
    return int(sum_results)


# noinspection PyUnresolvedReferences
@v_args(inline=True)  # Affects the signatures of the methods, taking args instead of lists
class CalculateTree(Transformer):
    from operator import add, mul
    number = int

    def __init__(self):
        return

    def add(self, val1, val2):
        return val1 + val2

    def mul(self, val1, val2):
        return val1 * val2


def parse_data(data):
    return data.strip().split("\n")


test_data = """
1 + 2 * 3 + 4 * 5 + 6
"""

test_data_brackets = """
1 + (2 * 3) + (4 * (5 + 6))
"""

test_data_b = """
2 * 3 + (4 * 5)
"""

if __name__ == "__main__":
    assert part_a(test_data) == 71
    assert part_a(test_data_brackets) == 51
    solution_a = part_a(data)
    submit(solution_a, part="a", day=18, year=2020)

    assert part_b(test_data_brackets) == 51
    assert part_b(test_data_b) == 46
    solution_b = part_b(data)
    submit(solution_b, part="b", day=18, year=2020)
