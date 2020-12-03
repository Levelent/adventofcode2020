with open("input.txt") as file:
    lines = file.read().split("\n")


def trees_encountered(slope, right: int, down: int):
    hor_pos = 0
    trees = 0
    threshold = len(slope[0])
    for line in slope[::down]:
        if line[hor_pos] == '#':
            trees += 1
        hor_pos = (hor_pos + right) % threshold
    return trees


a = trees_encountered(lines, 1, 1)
b = trees_encountered(lines, 3, 1)
c = trees_encountered(lines, 5, 1)
d = trees_encountered(lines, 7, 1)
e = trees_encountered(lines, 1, 2)
print(a * b * c * d * e)
