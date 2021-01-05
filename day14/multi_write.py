def gen_locations(float_mask):
    if "X" not in float_mask:
        return [float_mask]

    left = float_mask.replace("X", "0", 1)
    right = float_mask.replace("X", "1", 1)
    return gen_locations(left) + gen_locations(right)


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
    to_write = int(line[r_bracket + 4:])
    address = int(line[4:r_bracket])

    before_mask = format(address, "b").zfill(36)

    after_mask = ""
    # Apply mask
    for i in range(36):
        if mask[i] == "0":
            after_mask += before_mask[i]
        else:
            after_mask += mask[i]
    # Generate all memory locations from mask
    locations = gen_locations(after_mask)
    for location in locations:
        memory[int(location, 2)] = to_write

print(sum(memory.values()))
