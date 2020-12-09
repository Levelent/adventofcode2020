with open("input.txt") as file:
    lines = file.read().split("\n")

last_25 = [int(line) for line in lines[:25]]
last_sums = [[last_25[i] + last_25[j] for j in range(i+1, 25)] for i in range(24)]


def is_sum(num):
    for rows in last_sums:
        for elem in rows:
            if num == elem:
                return True
    return False


def update_sums(num):
    last_25.pop(0)
    last_25.append(num)
    last_sums.append([])
    last_sums.pop(0)
    for i in range(24):
        last_sums[i].append(num + last_25[i])


for line in lines[25:]:
    n = int(line)
    if not is_sum(n):
        print(n)
        break
    update_sums(n)
