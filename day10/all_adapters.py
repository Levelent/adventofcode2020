with open("input.txt") as file:
    lines = file.read().split("\n")

nums = [0] + sorted([int(line) for line in lines])
del lines
print(nums)

one_jumps = 0
three_jumps = 0

for i in range(len(nums) - 1):
    diff = nums[i+1] - nums[i]
    if diff == 1:
        one_jumps += 1
    elif diff == 3:
        three_jumps += 1
    i += 1

print(one_jumps * (three_jumps + 1))
# Note: There are no 2-jumps
