from aocd import data
from aocd import submit


def part_a(data):
    lines = list(data.strip().split("\n"))
    trees = check_slope(lines, 3, 1)

    return str(trees)


def part_b(data):
    offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    lines = list(data.strip().split("\n"))

    mul = 1
    for offset in offsets:
        right, down = offset
        mul *= check_slope(lines, right, down)
    return str(mul)


def check_slope(lines, right_offset, down_offset):
    width = len(lines[0])
    trees = 0
    x = 0
    y = 0

    while y < len(lines):
        trees += lines[y][x] == '#'
        x = (x + right_offset) % width
        y += down_offset

    return trees


test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

if __name__ == "__main__":
    assert part_a(test_data) == "7"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=3, year=2020)

    assert part_b(test_data) == "336"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=3, year=2020)
