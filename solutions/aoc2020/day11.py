import copy
import itertools

from aocd import data
from aocd import submit


def part_a(data):
    seats = parse_data(data)
    stable = False

    occupied = count_occupied(seats)

    while not stable:
        # pretty_print_seats(seats)
        old_occupied = occupied
        new_seats = copy.deepcopy(seats)
        for row in range(0, len(seats)):
            for col in range(0, len(seats[0])):
                if seats[row][col] == "L" and count_adjacent_occupied(row, col, seats) == 0:
                    new_seats[row][col] = "#"
                if seats[row][col] == "#" and count_adjacent_occupied(row, col, seats) >= 4:
                    new_seats[row][col] = "L"
        occupied = count_occupied(new_seats)
        stable = old_occupied == occupied

        seats = new_seats

    return occupied


def part_b(data):
    seats = parse_data(data)
    stable = False

    occupied = count_occupied(seats)

    while not stable:
        # pretty_print_seats(seats)
        old_occupied = occupied
        new_seats = copy.deepcopy(seats)
        for row in range(0, len(seats)):
            for col in range(0, len(seats[0])):
                if seats[row][col] == "L" and count_visible_occupied(row, col, seats) == 0:
                    new_seats[row][col] = "#"
                if seats[row][col] == "#" and count_visible_occupied(row, col, seats) >= 5:
                    new_seats[row][col] = "L"
        occupied = count_occupied(new_seats)
        stable = old_occupied == occupied
        seats = new_seats

    return occupied


def count_adjacent_occupied(row, col, seats):
    sum_adjacent = 0
    for i in range(row - 1, row + 2):
        if i < 0 or i >= len(seats):
            continue
        selected_row = seats[i]
        for j in range(col - 1, col + 2):
            if j < 0 or j >= len(selected_row):
                continue
            if not (i == row and j == col):
                sum_adjacent += seats[i][j] == "#"
    return sum_adjacent


def count_visible_occupied(row, col, seats):
    sum_visible = 0
    directions = list(itertools.product([-1, 1, 0], repeat=2))
    directions.remove((0, 0))

    for direction in directions:
        i = row
        j = col
        y_step, x_step = direction
        i += y_step
        j += x_step
        while not (i < 0 or i >= len(seats) or j < 0 or j >= len(seats[0])):
            if seats[i][j] == "#":
                sum_visible += 1
                break
            elif seats[i][j] == "L":
                break
            i += y_step
            j += x_step

    return sum_visible


def pretty_print_seats(seats):
    for row in seats:
        for seat in row:
            print(seat, end='')
        print()
    print()


def count_occupied(seats):
    sum_occupied = 0
    for row in seats:
        for seat in row:
            sum_occupied += seat == "#"
    return sum_occupied


def parse_data(data):
    return list(map(list, data.strip().split("\n")))


test_data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

small_test = """
L##
.##
"""

no_visible = """
.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
"""

if __name__ == "__main__":
    assert part_a(test_data) == 37
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=11, year=2020)

    assert count_visible_occupied(3, 3, parse_data(no_visible)) == 0
    assert part_b(test_data) == 26
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=11, year=2020)
