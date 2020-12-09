with open("input.txt") as file:
    lines = file.read().split("\n")

nums = [int(line) for line in lines]
del lines
sum_to = 1721308972
# Largest possible length is index of sum_to - 1
idx = nums.index(sum_to)
for length in range(2, idx):
    for i in range(idx - length + 1):
        sublist = nums[i:i+length]
        if sum(sublist) == sum_to:
            print(min(sublist) + max(sublist))
