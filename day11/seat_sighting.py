def can_see_occupied(prev_rs, r_source, c_source, r_dir, c_dir):
    r_dist = 0
    c_dist = 0
    while True:
        r_dist += r_dir
        c_dist += c_dir
        if not 0 <= r_source + r_dist < len(prev_rs) or not 0 <= c_source + c_dist < len(prev_rs[0]):
            return False
        to_check = prev_rs[r_source + r_dist][c_source + c_dist]
        if to_check != ".":
            return to_check == "#"


def count_occupied(prev_rs, r_source, c_source):
    occupied = 0
    for r_dir in range(-1, 2):
        for c_dir in range(-1, 2):
            if r_dir == c_dir == 0:
                continue
            occupied += can_see_occupied(prev_rs, r_source, c_source, r_dir, c_dir)
    return occupied


def change_seat(prev_rs, next_rs, r_source, c_source):
    to_change = prev_rs[r_source][c_source]
    if to_change == ".":
        return False

    occupied = count_occupied(prev_rs, r_source, c_source)

    if occupied == 0 and to_change == "L":
        next_rs[r_source][c_source] = "#"
        return True
    elif occupied >= 5 and to_change == "#":
        next_rs[r_source][c_source] = "L"
        return True
    return False


with open("input.txt") as file:
    rows = [list(row) for row in file.read().split("\n")]

swaps = 1
while swaps > 0:
    next_rows = [r[:] for r in rows]
    swaps = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            swaps += change_seat(rows, next_rows, i, j)
    rows = next_rows

total = 0
for row in rows:
    for seat in row:
        total += seat == "#"
print(total)
