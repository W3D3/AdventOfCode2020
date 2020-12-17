from aocd import data
from aocd import submit

from parse import parse


def part_a(data):
    conditions, _, nearby_tickets = parse_data(data)

    total = 0
    for ticket in nearby_tickets:
        total += sum(get_invalid_nums(conditions, ticket))
    return total


def part_b(data):
    conditions, myticket, nearby_tickets = parse_data(data)

    valid_tickets = []
    for ticket in nearby_tickets:
        if is_valid(conditions, ticket):
            valid_tickets.append(ticket)

    matching = match_condition(conditions, valid_tickets)

    total = 1
    for index, condition in matching.items():
        if condition["title"].startswith("departure"):
            total *= myticket[index]

    return total


def match_condition(conditions, tickets, valid_field_mapping=None):
    size = len(tickets[0])
    i = 0
    if valid_field_mapping is None:
        valid_field_mapping = {}
    while i < size:
        if i in valid_field_mapping.keys():
            i += 1
            continue
        values_for_index = [ticket[i] for ticket in tickets]

        valid_conditions = []
        conditions_to_check = set(conditions).difference(valid_field_mapping.values())

        for condition in conditions_to_check:
            possibility = all([valid_for(condition, num) for num in values_for_index])  # has to only fit once for all
            if possibility:
                valid_conditions.append(condition)
        if len(valid_conditions) == 1:  # found valid connection, possibly reloop?
            valid_field_mapping[i] = valid_conditions[0]
            i = 0
        else:
            i += 1
            if i == size and len(valid_field_mapping) < size:
                raise Exception("Impossible input!")

    return valid_field_mapping


def get_invalid_nums(conditions, ticket):
    invalid_nums = []
    for num in ticket:
        validity = [valid_for(condition, num) for condition in conditions]
        invalid = not any(validity)
        if invalid:
            invalid_nums.append(num)
    return invalid_nums


def is_valid(conditions, ticket):
    for num in ticket:
        validity = [valid_for(condition, num) for condition in conditions]
        invalid = not any(validity)
        if invalid:
            return False
    return True


def valid_for(condition, num):
    if num < condition["low1"] or (condition["hi1"] < num < condition["low2"]) or num > condition["hi2"]:
        return False
    return True


def parse_data(data):
    conditions_text, myticket_text, nearby_tickets_text = data.strip().split("\n\n")
    conditions = [parse("{title}: {low1:d}-{hi1:d} or {low2:d}-{hi2:d}", line) for line in conditions_text.split("\n")]
    myticket = list(map(int, myticket_text.split("\n")[1].split(",")))
    nearby_tickets = [list(map(int, line.split(","))) for line in nearby_tickets_text.split("\n")[1:]]

    return conditions, myticket, nearby_tickets


test_data = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

test_data_b = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""

if __name__ == "__main__":
    assert part_a(test_data) == 71
    solution_a = part_a(data)
    # submit(solution_a, part="a", day=16, year=2020)

    # part_b(test_data_b)
    solution_b = part_b(data)
    # submit(solution_b, part="b", day=16, year=2020)
