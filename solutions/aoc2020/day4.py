from aocd import data
from aocd import submit
import re


def part_a(data):
    lines = list(data.strip().split("\n\n"))

    valid_cnt = 0
    for line in lines:
        passport = dict((key.strip(), val.strip())
                        for key, val in (element.split(':')
                                         for element in re.split('\n| ', line)))

        valid_cnt += valid(passport)

    return str(valid_cnt)


def part_b(data):
    lines = list(data.strip().split("\n\n"))

    valid_cnt = 0
    for line in lines:
        passport = dict((key.strip(), val.strip())
                        for key, val in (element.split(':')
                                         for element in re.split('\n| ', line)))

        valid_cnt += valid_data(passport)

    return str(valid_cnt)


def valid(passport):
    req_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # we skip cid
    return req_keys.intersection(passport.keys()) == req_keys


def valid_data(passport):
    req_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # we skip cid

    if req_keys.intersection(passport.keys()) != req_keys:
        return False

    if not (2002 >= int(passport["byr"]) >= 1920):
        return False

    if not (2020 >= int(passport["iyr"]) >= 2010):
        return False

    if not (2030 >= int(passport["eyr"]) >= 2020):
        return False

    defined_height = re.match("(\d*)(cm|in)", passport['hgt'])
    if not defined_height:
        return False

    height, unit = defined_height.groups()
    if unit == "cm":
        if not (193 >= int(height) >= 150):
            return False
    elif unit == "in":
        if not (76 >= int(height) >= 59):
            return False
    else:
        return False

    valid_hair = re.match("^#(\d|[a-f]){6}$", passport['hcl'])

    if not valid_hair:
        return False

    valid_eye = re.match("^amb|blu|brn|gry|grn|hzl|oth$", passport['ecl'])
    if not valid_eye:
        return False

    valid_pid = re.match("^[\d]{9}$", passport['pid'])
    if not valid_pid:
        return False

    return True


test_data = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

all_invalid = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

all_valid = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

if __name__ == "__main__":
    assert part_a(test_data) == "2"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=4, year=2020)

    assert part_b(all_invalid) == "0"
    assert part_b(all_valid) == "4"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=4, year=2020)
