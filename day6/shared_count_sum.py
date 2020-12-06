with open("input.txt") as file:
    groups = file.read().split("\n\n")

total = 0
for group in groups:
    forms = group.split("\n")
    intersect = set(forms[0])
    for form in forms[1:]:
        intersect &= set(form)
    total += len(intersect)
print(total)
