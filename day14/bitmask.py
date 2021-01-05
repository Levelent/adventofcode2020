with open("input.txt") as file:
    lines = file.read().split("\n")

memory = {}
mask = ""
for line in lines:
    if "mask" in line:
        mask = line[7:]
        continue
    # If mem instead
    r_bracket = line.find("]")
    mem_location = int(line[4:r_bracket])
    before_mask = format(int(line[r_bracket + 4:]), "b").zfill(36)

    after_mask = ""
    # Compare binary strings to apply mask
    for i in range(36):
        if mask[i] == "X":
            after_mask += before_mask[i]
        else:
            after_mask += mask[i]
    memory[mem_location] = int(after_mask, 2)

print(sum(memory.values()))

