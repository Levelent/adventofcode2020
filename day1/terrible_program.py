with open("input.txt") as file:
    nums = [int(n) for n in file.read().split("\n")]

# For anyone who has the displeasure of laying their eyes upon this, I am sorry.
for idx1, elem1 in enumerate(nums):
    for idx2, elem2 in enumerate(nums):
        for idx3, elem3 in enumerate(nums):
            if elem1 + elem2 + elem3 == 2020 and idx1 != idx2 != idx3:
                print(elem1 * elem2 * elem3)
