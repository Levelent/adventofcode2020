import re

with open("input.txt") as file:
    passports = file.read().split("\n\n")

split_passports = [re.split("[ \n:]", p) for p in passports]

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def fields_present(pp, fs):
    for f in fs:
        if f not in pp:
            return False
    return True


def four_digit_yr_range(s, a, b):
    return len(s) == 4 and value.isdigit() and a <= int(s) <= b


def measure_range(s, units, a, b):
    u_len = len(units)
    return s[-u_len:] == units and s[:-u_len].isdigit() and a <= int(s[:-u_len]) <= b


count = 0
for passport in split_passports:
    if not fields_present(passport, fields):
        continue
    flag = False
    for i in range(len(passport) // 2):
        name = passport[i*2]
        value = passport[(i*2)+1]
        if name == "byr" and four_digit_yr_range(value, 1920, 2002):
            continue
        elif name == "iyr" and four_digit_yr_range(value, 2010, 2020):
            continue
        elif name == "eyr" and four_digit_yr_range(value, 2020, 2030):
            continue
        elif name == "hgt" and (measure_range(value, "cm", 150, 193) or measure_range(value, "in", 59, 76)):
            continue
        elif name == "hcl" and re.match("#[0-9a-f]{6}", value):
            continue
        elif name == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        elif name == "pid" and value.isdigit() and len(value) == 9:
            continue
        elif name == "cid":
            continue
        else:
            flag = True
            break
    if flag:
        continue
    count += 1
print(count)

