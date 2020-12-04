import re

with open("input.txt") as file:
    passports = file.read().split("\n\n")

passports_pairs = []
for passport in passports:
    split_passport = re.split("[ \n]", passport)
    pairs = {}
    for pair in split_passport:
        key, value = pair.split(":")
        pairs[key] = value
    passports_pairs.append(pairs)
del passports
print(passports_pairs)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def fields_present(pp_dict, fs):
    for f in fs:
        if f not in pp_dict:
            return False
    return True


def four_digit_yr_range(s, a, b):
    return len(s) == 4 and s.isdigit() and a <= int(s) <= b


def measure_range(s, units, a, b):
    u_len = len(units)
    return s[-u_len:] == units and s[:-u_len].isdigit() and a <= int(s[:-u_len]) <= b


def fields_valid(pp_dict):
    if not four_digit_yr_range(pp_dict["byr"], 1920, 2002):
        return False
    elif not four_digit_yr_range(pp_dict["iyr"], 2010, 2020):
        return False
    elif not four_digit_yr_range(pp_dict["eyr"], 2020, 2030):
        return False
    elif not (measure_range(pp_dict["hgt"], "cm", 150, 193) or measure_range(pp_dict["hgt"], "in", 59, 76)):
        return False
    elif not re.match("#[0-9a-f]{6}", pp_dict["hcl"]):
        return False
    elif pp_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    elif not (pp_dict["pid"].isdigit() and len(pp_dict["pid"]) == 9):
        return False
    return True


count = 0
for passport in passports_pairs:
    if fields_present(passport, fields) and fields_valid(passport):
        count += 1
print(count)

