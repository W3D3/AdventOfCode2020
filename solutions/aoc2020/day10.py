import networkx as nx

from aocd import data
from aocd import submit


def part_a(data):
    adapters = parse_data(data)
    adapters.append(0)  # outlet
    adapters.append(max(adapters) + 3)  # my phone
    adapters = sorted(adapters)

    cnt_3diff = 0
    cnt_1diff = 0
    for current, next in zip(adapters, adapters[1:]):
        if next - current == 3:
            cnt_3diff += 1
        elif next - current == 1:
            cnt_1diff += 1

    return cnt_3diff * cnt_1diff


def part_b(data):
    adapters = parse_data(data)
    adapters.append(0)  # outlet
    my_device = max(adapters) + 3
    adapters.append(my_device)  # my phone
    adapters = sorted(adapters, reverse=True)

    possibilities = [0] * len(adapters)
    # only 1 possibility for last
    possibilities[0] = 1

    for i in range(1, len(adapters)):
        current_possibilities = 0
        for j in range(1, 4):
            if i - j >= 0 and adapters[i - j] - adapters[i] <= 3:
                current_possibilities += possibilities[i - j]
        possibilities[i] = current_possibilities;

    return possibilities[-1]


def part_b_rec(data):
    adapters = parse_data(data)
    adapters.append(0)  # outlet
    my_device = max(adapters) + 3
    adapters.append(my_device)  # my phone
    adapters = sorted(adapters)

    sum_paths = cnt_possibilities_rec(0, adapters)

    return sum_paths


def cnt_possibilities_rec(index, adapters):
    selected = adapters[index]
    sum = 0
    for j in range(1, 4):
        if index + j < len(adapters):
            if adapters[index + j] - selected <= 3:
                sum += cnt_possibilities_rec(index + j, adapters)
        else:
            return 1
    return sum


def part_b_graph(data):
    adapters = parse_data(data)
    adapters.append(0)  # outlet
    my_device = max(adapters) + 3
    adapters.append(my_device)  # my phone
    adapters = sorted(adapters)

    graph = nx.DiGraph()
    graph.add_nodes_from(adapters)

    for i in range(0, len(adapters)):
        current = adapters[i]
        for j in range(1, 4):
            if i + j < len(adapters) and adapters[i + j] - current <= 3:
                graph.add_edge(current, adapters[i + j])

    paths = nx.all_simple_paths(graph, source=0, target=my_device)
    sum_paths = sum(1 for _ in list(paths))
    return sum_paths


def parse_data(data):
    return list(map(int, data.strip().split("\n")))


small_test = """
1
4
5
6
7
10
"""

test_data = """
16
10
15
5
1
11
7
19
6
12
4
"""

test_data_large = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

if __name__ == "__main__":
    assert part_a(test_data) == 35
    assert part_a(test_data_large) == 220
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=10, year=2020)

    assert part_b(small_test) == 4
    assert part_b(test_data) == 8
    assert part_b(test_data_large) == 19208
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=10, year=2020)
