from time import sleep


class SpokenNumber:
    def __init__(self, first_turn):
        self.earlier = first_turn
        self.later = 0

    def spoken_again(self, turn_num):
        self.earlier = self.later
        self.later = turn_num

    def difference(self):
        return self.later - self.earlier


spoken_numbers = {}
# stored as 2 element array (most recent, second most recent) [ , ]

with open("input.txt") as file:
    s_nums = [int(n) for n in file.read().split(",")]

# Setup numbers
for i, num in enumerate(s_nums):
    spoken_numbers[num] = SpokenNumber(i + 1)
    print(i + 1, num)

prev = s_nums[-1]


for turn in range(len(s_nums) + 1, 2021):
    if spoken_numbers[prev].later == 0:
        prev = 0
        spoken_numbers[prev].spoken_again(turn)
        print(turn, prev)
        sleep(0.5)
        continue

    prev = spoken_numbers[prev].difference()

    if prev not in spoken_numbers:
        spoken_numbers[prev] = SpokenNumber(turn)
    else:
        spoken_numbers[prev].spoken_again(turn)
    print(turn, prev)
    sleep(0.5)
