def adjacent_seats(prev_rs, next_rs, s_r, s_c):
    to_change = prev_rs[s_r][s_c]
    if to_change == ".":
        return False

    r_lower = max(0, s_r - 1)
    r_upper = min(len(prev_rs), s_r + 2)
    c_lower = max(0, s_c - 1)
    c_upper = min(len(prev_rs[0]), s_c + 2)

    occupied = 0
    for r in range(r_lower, r_upper):
        for c in range(c_lower, c_upper):
            if r == s_r and c == s_c:
                continue
            if prev_rs[r][c] == "#":
                occupied += 1

    if occupied == 0 and to_change == "L":
        next_rs[s_r][s_c] = "#"
        return True
    elif occupied >= 4 and to_change == "#":
        next_rs[s_r][s_c] = "L"
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
            swaps += adjacent_seats(rows, next_rows, i, j)
    rows = next_rows

total = 0
for row in rows:
    for seat in row:
        total += seat == "#"
print(total)
