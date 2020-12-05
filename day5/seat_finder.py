with open("input.txt") as file:
    lines = file.read().split("\n")


def binary_search(moves, l_char):
    start = 0
    end = pow(2, len(moves)) - 1
    for char in moves:
        if char == l_char:
            end = (start + end) // 2
        else:
            start = ((start + end) // 2) + 1
    return start


def get_seat_id(r: int, c: int):
    return r * 8 + c


min_id = 1031  # 128 * 8 + 7
max_id = -1
ids = set()
for line in lines:
    row = binary_search(line[:7], "F")
    column = binary_search(line[7:], "L")
    s_id = get_seat_id(row, column)
    ids.add(s_id)
    if s_id > max_id:
        max_id = s_id
    if s_id < min_id:
        min_id = s_id
print(min_id, max_id)
print(set(range(min_id, max_id+1)) - ids)




