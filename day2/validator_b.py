with open("input.txt") as file:
    lines = file.read().split("\n")
    print(lines)

valid_count = 0
for line in lines:
    num_range, char, password = line.split()
    s, e = num_range.split("-")
    start = int(s) - 1
    end = int(e) - 1
    target = char[0]
    valid_count += bool(password[start] == target) ^ bool(password[end] == target)
print(valid_count)

