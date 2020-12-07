from aocd import data
from aocd import submit
import re
from parse import *
import networkx as nx


def part_a(data):
    lines = list(data.strip().split("\n"))
    G = nx.DiGraph()

    for line in lines:
        left, right = line.split("contain")
        upper_bag = parse("{color} bags", left.strip())
        if right.strip() != "no other bags.":
            lower_bags = right.split(",")
            for lower in lower_bags:
                lower = re.sub('s?\.?$', '', lower)
                # print(lower)
                lower_bag = parse("{num:d} {color} bag", lower.strip())
                G.add_edge(upper_bag.named["color"], lower_bag.named["color"], weight=1)
                # print(upper_bag, "->", lower_bag)
        else:
            # print(upper_bag)
            G.add_node(upper_bag.named["color"])

    candidates = rec_predecessors(set(), G.predecessors("shiny gold"), G)

    print(len(candidates))
    return str(len(candidates))


def part_b(data):
    lines = list(data.strip().split("\n\n"))

    # todo
    return str(0)


def rec_predecessors(candidates, nodes, G):
    for node in nodes:
        candidates.add(node)
        for rec_node in rec_predecessors(candidates, G.predecessors(node), G):
            candidates.add(rec_node)
    return candidates


test_data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

if __name__ == "__main__":
    assert part_a(test_data) == "4"
    solution_a = part_a(data)
    print(solution_a)
    submit(solution_a, part="a", day=7, year=2020)

    # assert part_b(test_data) == "6"
    # solution_b = part_b(data)
    # print(solution_b)
    # submit(solution_b, part="b", day=7, year=2020)
