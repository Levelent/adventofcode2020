with open("input.txt") as file:
    lines = file.read().split("\n")

mapping = {"F": "0", "B": "1", "L": "0", "R": "1"}

known_ids = set()
for line in lines:
    bin_int = "".join([mapping[c] for c in line])
    known_ids.add(int(bin_int, 2))
print(max(known_ids))
all_ids = set(range(min(known_ids), max(known_ids) + 1))
print(all_ids - known_ids)




