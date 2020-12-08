with open("input.txt") as file:
    lines = file.read().split("\n")

instructions = []
for line in lines:
    op, val = line.replace("+", "").split()
    instructions.append((op, int(val)))

acc = 0
i = 0
visited = set()
while True:
    if i in visited:
        break
    visited.add(i)
    op, val = instructions[i]
    if op == "jmp":
        i += val
        continue
    elif op == "acc":
        acc += val
    i += 1
print(visited)
print(acc)
