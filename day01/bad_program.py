with open("input.txt") as file:
    nums = [int(n) for n in file.read().split("\n")]

# Terrible solution, but the input size is too small to warrant a better one
for idx1, elem1 in enumerate(nums):
    for idx2, elem2 in enumerate(nums):
        if elem1 + elem2 == 2020 and idx1 != idx2:
            print(elem1 * elem2)
            exit(0)
