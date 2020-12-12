with open("input.txt") as file:
    directions = file.read().split("\n")

east, north = 0, 0
rotation = 90

for direct in directions:
    command = direct[0]
    value = int(direct[1:])

    if command == "N":
        north += value
    elif command == "S":
        north -= value
    elif command == "E":
        east += value
    elif command == "W":
        east -= value
    elif command == "L":
        rotation = (rotation - value) % 360
    elif command == "R":
        rotation = (rotation + value) % 360
    elif command == "F":
        if rotation == 0:
            north += value
        elif rotation == 90:
            east += value
        elif rotation == 180:
            north -= value
        else:
            east -= value

print(abs(north) + abs(east))
