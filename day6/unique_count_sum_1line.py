print(sum([len(set(g.replace("\n", ""))) for g in open("input.txt").read().split("\n\n")]))
# Note: This was a terrible idea
