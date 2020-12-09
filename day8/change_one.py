with open("input.txt") as file:
    lines = file.read().split("\n")

instructions = []
for line in lines:
    operation, value = line.replace("+", "").split()
    instructions.append([operation, int(value)])


def visited_before_loop(instructs):
    i = 0
    visits = set()
    while True:
        if i in visits:
            return visits
        visits.add(i)
        op, val = instructs[i]
        if op == "jmp":
            i += val
        else:
            i += 1


def run(instructs):
    acc = 0
    i = 0
    visits = set()
    while i < len(instructs):
        if i in visits:
            return False, acc
        visits.add(i)
        op, val = instructions[i]
        if op == "jmp":
            i += val
            continue
        elif op == "acc":
            acc += val
        i += 1
    return True, acc


def flip_code(code):
    if code == "jmp":
        return "nop"
    else:
        return "jmp"


visited = visited_before_loop(instructions)
print(visited)
terminated = True
acc_val = 0
for v in visited:
    if instructions[v][0] == "acc":
        continue
    instructions[v][0] = flip_code(instructions[v][0])
    terminated, acc_val = run(instructions)
    if terminated:
        print(terminated, acc_val)
        break
    instructions[v][0] = flip_code(instructions[v][0])
