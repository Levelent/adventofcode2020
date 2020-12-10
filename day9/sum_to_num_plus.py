with open("input.txt") as file:
    lines = file.read().split("\n")

nums = [int(line) for line in lines]
del lines

# Takes O(n) to compute prefix sum
prefix_sums = []
running_total = 0
for n in nums:
    running_total += n
    prefix_sums.append(running_total)

sum_to = 1721308972

# Takes O(n^2) to check combinations of prefix sum
for gap in range(2, len(nums) - 1):
    for i in range(len(nums) - gap):
        val = prefix_sums[i+gap] - prefix_sums[i]
        if val == sum_to:
            # Takes O(n), but only when found
            sublist = nums[i+1:i+gap+1]
            print(min(sublist) + max(sublist))
            break
