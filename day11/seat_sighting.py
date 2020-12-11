def sighted_seats(prev_rs, next_rs, s_r, s_c):
    to_change = prev_rs[s_r][s_c]
    if to_change == ".":
        return False

    occupied = 0
    for r_dir in range(-1, 2):
        for c_dir in range(-1, 2):
            if r_dir == c_dir == 0:
                continue
            r_dist = 0
            c_dist = 0
            while True:
                r_dist += r_dir
                c_dist += c_dir
                if not 0 <= s_r + r_dist < len(prev_rs) or not 0 <= s_c + c_dist < len(prev_rs[0]):
                    break
                to_check = prev_rs[s_r + r_dist][s_c + c_dist]
                if to_check != ".":
                    if to_check == "#":
                        occupied += 1
                    break

    if occupied == 0 and to_change == "L":
        next_rs[s_r][s_c] = "#"
        return True
    elif occupied >= 5 and to_change == "#":
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
            swaps += sighted_seats(rows, next_rows, i, j)
    rows = next_rows

total = 0
for row in rows:
    for seat in row:
        total += seat == "#"
print(total)
