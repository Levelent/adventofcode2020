with open("input.txt") as file:
    groups = file.read().split("\n\n")

total = 0
for group in groups:
    g = group.replace("\n", "")
    total += len(set(g))
print(total)
