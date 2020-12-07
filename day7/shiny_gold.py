with open("input.txt") as file:
    text = file.read().split("\n")

bag_structure = {}

for line in text:
    contains = []
    words = line.split()
    bag_name = " ".join(words[:2])
    if "no other bags" not in line:
        i = 4
        for i in range(4, len(words), 4):
            name = f"{words[i + 1]} {words[i + 2]}"
            num = int(words[i])
            contains.append((name, num))
    bag_structure[bag_name] = contains


def has_gold_bag(b_name):
    bs = bag_structure[b_name]
    if len(bs) == 0:
        return False
    for b in bs:
        if b[0] == "shiny gold":
            return True
    for b in bs:
        if has_gold_bag(b[0]):
            return True
    return False


def bags_in_bag(b_name: str):
    bs = bag_structure[b_name]
    if len(bs) == 0:
        return 0
    b_total = 0
    for b in bs:
        b_total += b[1] + b[1] * bags_in_bag(b[0])
    return b_total


num_containing_gold = 0
for bag in bag_structure.keys():
    num_containing_gold += has_gold_bag(bag)
print(num_containing_gold)

print(bags_in_bag("shiny gold"))
