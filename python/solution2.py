#!/usr/bin/env python3

# A = opponent chooses rock
# B = opponent chooses paper
# C = opponent chooses scissors

# loss = 0 score
# draw = 3 score
# win  = 6 score

# Part 1
# X = you choose rock
# Y = you choose paper
# Z = you choose scissors

def solution2(filename):
    part_1_scores = {
        'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
        'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
        'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3,
    }
    part_2_scores = {
        #      Lose          Draw          Win
        'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
        'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
        'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6,

    }
    with open(filename) as file:
        part_1_score = 0
        part_2_score = 0
        for line in file:
            line = line.rstrip()
            part_1_score += part_1_scores[line]
            part_2_score += part_2_scores[line]

        return part_1_score, part_2_score


if __name__ == '__main__':
    print(solution2("../input/2.txt"))
