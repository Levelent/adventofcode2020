import timeit

with open("input.txt") as file:
    text = file.read().split("\n")

bag_structure = {}

for line in text:
    contains = []
    words = line.split()
    bag_name = " ".join(words[:2])
    if "no other" not in line:
        i = 4
        for i in range(4, len(words), 4):
            name = f"{words[i + 1]} {words[i + 2]}"
            num = int(words[i])
            contains.append((name, num))
    bag_structure[bag_name] = contains

has_gold_mem = {}
bags_in_bag_mem = {}


def has_gold_bag(b_name):
    if b_name in has_gold_mem:
        return has_gold_mem[b_name]
    bs = bag_structure[b_name]
    if len(bs) == 0:
        return False
    for b in bs:
        if b[0] == "shiny gold":
            return True
    for b in bs:
        if b[0] not in has_gold_mem:
            check = has_gold_bag(b[0])
        else:
            check = has_gold_mem[b[0]]
        if check:
            return True
    return False


def bags_in_bag(b_name: str):
    if b_name in bags_in_bag_mem:
        return bags_in_bag_mem[b_name]
    bs = bag_structure[b_name]
    if len(bs) == 0:
        return 0
    b_total = 0
    for b in bs:
        if b[0] not in bags_in_bag_mem:
            n_in_bag = bags_in_bag(b[0])
        else:
            n_in_bag = bags_in_bag_mem[b[0]]
        b_total += b[1] + b[1] * n_in_bag
    return b_total


num_containing_gold = 0
for bag in bag_structure.keys():
    num_containing_gold += has_gold_bag(bag)
print(num_containing_gold)

print(bags_in_bag("shiny gold"))
