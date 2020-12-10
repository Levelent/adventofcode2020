with open("input.txt") as file:
    lines = file.read().split("\n")

nums = sorted([int(line) for line in lines])
# Memoisation time
calcs = [0] * len(nums)


def recursive_ways(pos):
    if calcs[pos] == 0:
        total = 0
        if nums[pos] <= 3:
            total += 1
        back_idx = pos - 1
        while back_idx >= 0 and nums[pos] - nums[back_idx] <= 3:
            total += recursive_ways(back_idx)
            back_idx -= 1
        calcs[pos] = total
    return calcs[pos]


print(recursive_ways(len(nums) - 1))
