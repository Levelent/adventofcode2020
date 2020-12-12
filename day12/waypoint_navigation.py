with open("input.txt") as file:
    directions = file.read().split("\n")

s_east, s_north = 0, 0
w_east, w_north = 10, 1

for direct in directions:
    command = direct[0]
    value = int(direct[1:])

    if command == "N":
        w_north += value
    elif command == "S":
        w_north -= value
    elif command == "E":
        w_east += value
    elif command == "W":
        w_east -= value
    elif command == "L":
        for i in range(value // 90):
            w_east, w_north = -w_north, w_east
    elif command == "R":
        for i in range(value // 90):
            w_east, w_north = w_north, -w_east
    elif command == "F":
        s_east += (w_east * value)
        s_north += (w_north * value)

print(abs(s_north) + abs(s_east))
# 1225 too low

