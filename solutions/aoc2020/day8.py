import networkx as nx
from aocd import data
from aocd import submit
import matplotlib.pyplot as plt

def part_a(data):
    instructions = list(data.strip().split("\n"))
    return execute(instructions)

def execute(instructions):
    pc = 0
    acc = 0
    visited = set()
    while True:
        if pc in visited:
            # loop detected
            return acc
        visited.add(pc)
        if pc >= len(instructions):
            return acc
        inst, par = parse_program_line(instructions[pc])
        if inst == "acc":
            acc += par
            pc += 1
            continue
        elif inst == "jmp":
            pc += par
            continue
        pc += 1


def parse_program_line(line):
    inst, par = line.split();
    return str(inst), int(par)


def part_b(data):
    instructions = list(data.strip().split("\n"))

    graph = nx.DiGraph()
    graph.add_nodes_from(range(0, len(instructions)))

    for pc in range(0, len(instructions)):
        inst, par = parse_program_line(instructions[pc])

        if inst == "acc":
            graph.add_edge(pc, pc + 1, weight=0)
            continue
        if inst == "nop":
            graph.add_edge(pc, pc + 1, weight=0)
            graph.add_edge(pc, pc + par, weight=1)
        elif inst == "jmp":
            graph.add_edge(pc, pc + 1, weight=1)
            graph.add_edge(pc, pc + par, weight=0)

    # for ugly visualization
    # print_graph(graph)

    # find path to the end of the program
    shortest_path = nx.dijkstra_path(graph, 0, len(instructions) - 1)

    for first, second in zip(shortest_path, shortest_path[1:]):
        if graph.get_edge_data(first, second)["weight"]:
            # found edge that is not in our original program, swap it
            original, param = parse_program_line(instructions[first])
            if original == "jmp":
                instructions[first] = "nop " + str(param)
            elif original == "nop":
                instructions[first] = "jmp " + str(param)

    return execute(instructions)

def print_graph(graph):
    options = {
        "font_size": 12,
        "node_size": 500,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
    }
    nx.draw_networkx(graph, None, **options)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("off")
    plt.show()

test_data = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

if __name__ == "__main__":
    assert part_a(test_data) == 5
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=8, year=2020)

    assert part_b(test_data) == 8
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=8, year=2020)
