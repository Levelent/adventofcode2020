with open("input.txt") as file:
    lines = file.read().split("\n")

hor_pos = 0
trees = 0
threshold = len(lines[0])

for line in lines:
    if line[hor_pos] == '#':
        trees += 1
    hor_pos = (hor_pos + 3) % threshold
print(trees)

