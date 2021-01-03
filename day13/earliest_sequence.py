from math import gcd

with open("input.txt") as file:
    _ = file.readline()
    line = file.readline()

timetable = line.split(",")
bus_ids = [int(t) for t in line.replace("x,", "").split(",")]


mins_between = []
for i in range(len(timetable)):
    if timetable[i] != "x":
        mins_between.append(i)

print(mins_between)
print(bus_ids)
# When does

# Chinese remainder theorem time
# Note that all inputs are prime
# Want to do this with all possible remainders


def lcm(a, b):
    return (a * b) // gcd(a, b)


total = 1
for num in bus_ids:
    total = lcm(total, num)
print(total)


# Finds multiplicative inverse of a number under modulo arithmetic, noting that m is prime
def fermat_inverse(num: int, mod: int):
    return pow(num, mod - 2, mod)




