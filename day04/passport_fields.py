with open("input.txt") as file:
    passports = file.read().split("\n\n")

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0
for passport in passports:
    flag = False
    for field in fields:
        if f"{field}:" not in passport:
            flag = True
            break
    if flag:
        continue
    count += 1
print(count)
