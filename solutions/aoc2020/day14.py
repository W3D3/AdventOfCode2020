import itertools

from aocd import data
from aocd import submit
from parse import parse


def part_a(data):
    expressions = parse_data(data)
    positive_mask = 0
    negative_mask = 0
    memory = {}

    for cmd, value in expressions:
        if cmd == "mask":
            positive_mask = int(value.replace("X", "0"), 2)
            negative_mask = int(value.replace("X", "1"), 2)
        else:
            mem_loc = parse("mem[{:d}]", cmd.strip()).fixed[0]
            memory[mem_loc] = (int(value) | positive_mask) & negative_mask

    return sum(memory.values())


def part_b(data):
    expressions = parse_data(data)
    memory = {}
    preprocessing_mask = None
    masks = []

    for cmd, value in expressions:
        if cmd == "mask":
            # generate all substitutions for X
            masks = generate_masks(value, "X")
            # create a mask to 0 out every bit in the original memory location where the mask is X
            preprocessing_mask = int(value.replace("0", "1").replace("X", "0"), 2)
        else:
            mem_loc = int(parse("mem[{:d}]", cmd.strip()).fixed[0])
            for mask in masks:
                new_loc = mem_loc & preprocessing_mask | mask
                memory[new_loc] = int(value)

    return sum(memory.values())


# Return all valid combinations of bitmasks as Int
def generate_masks(mask, floating_char):
    options = [(c,) if c != floating_char else ("0", "1") for c in mask]
    return list(int(''.join(o), 2) for o in itertools.product(*options))


def parse_data(data):
    expr = []
    lines = data.strip().split("\n")
    for line in lines:
        expr.append(line.split(" = "))

    return expr


test_data = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

test_data_b = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

if __name__ == "__main__":
    part_a(test_data)
    assert part_a(test_data) == 165
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=14, year=2020)

    assert part_b(test_data_b) == 208
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=14, year=2020)
