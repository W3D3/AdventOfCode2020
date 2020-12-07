from aocd import data
from aocd import submit
import re
from parse import *
import networkx as nx


def part_a(data):
    lines = list(data.strip().split("\n"))
    G = get_graph(lines)

    candidates = rec_predecessors(set(), G.predecessors("shiny gold"), G)

    return str(len(candidates))


def part_b(data):
    lines = list(data.strip().split("\n"))
    G = get_graph(lines)

    size = count_bags("shiny gold", G)

    return str(size)


def get_graph(lines):
    G = nx.DiGraph()

    for line in lines:
        left, right = line.split("contain")
        upper_bag = parse("{color} bags", left.strip())
        if right.strip() != "no other bags.":
            lower_bags = right.split(",")
            for lower in lower_bags:
                lower = re.sub('s?\.?$', '', lower) # dirty af regex hax for plurals
                lower_bag = parse("{num:d} {color} bag", lower.strip())
                G.add_edge(upper_bag.named["color"], lower_bag.named["color"], weight=lower_bag.named["num"])
        else:
            G.add_node(upper_bag.named["color"])

    return G


def rec_predecessors(candidates, nodes, G):
    for node in nodes:
        candidates.add(node)
        for rec_node in rec_predecessors(candidates, G.predecessors(node), G):
            candidates.add(rec_node)
    return candidates


def count_bags(node, G):
    count = 0
    if len(G.out_edges(node)) == 0:
        # leafs contain no bags
        return 0
    for edge in G.out_edges(node):
        weight = G.get_edge_data(*edge)["weight"]
        _, inner_bag = edge
        count += weight + weight * count_bags(inner_bag, G)
    return count


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

test_data_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

if __name__ == "__main__":
    assert part_a(test_data) == "4"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=7, year=2020)

    assert part_b(test_data) == "32"
    assert part_b(test_data_2) == "126"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=7, year=2020)
