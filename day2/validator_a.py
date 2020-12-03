with open("input.txt") as file:
    lines = file.read().split("\n")
    print(lines)

valid_count = 0
for line in lines:
    num_range, char, password = line.split()
    s, e = num_range.split("-")
    start = int(s)
    end = int(e)
    target = char[0]
    frequency = 0
    for character in password:
        if character == target:
            frequency += 1
    if start <= frequency <= end:
        valid_count += 1
print(valid_count)

