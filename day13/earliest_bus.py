with open("input.txt") as file:
    earliest_timestamp = int(file.readline())
    timetable = file.readline().replace("x,", "")

bus_ids = [int(t) for t in timetable.split(",")]

# Smallest distance from current remainder to frequency
best_id = 0
best_wait = max(bus_ids)
for id_num in bus_ids:
    mod = earliest_timestamp % id_num
    to_wait = id_num - mod
    if to_wait < best_wait:
        best_wait = to_wait
        best_id = id_num

print(best_wait * best_id)
