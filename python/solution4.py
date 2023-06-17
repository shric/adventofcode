#!/usr/bin/env python3

count = 1886


def solution4(filename: str) -> tuple[int, int]:
    part1 = part2 = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            left, right = line.split(",")

            lefts = [int(x) for x in left.split('-')]
            rights = [int(x) for x in right.split('-')]

            if lefts[0] >= rights[0] and lefts[1] <= rights[1]:
                part1 += 1
                part2 += 1
                continue
            elif rights[0] >= lefts[0] and rights[1] <= lefts[1]:
                part1 += 1
                part2 += 1
                continue
            if rights[0] <= lefts[0] <= rights[1]:
                part2 += 1
                continue
            if lefts[0] <= rights[0] <= lefts[1]:
                part2 += 1
                continue

    return part1, part2


if __name__ == '__main__':
    print(solution4("../input/4.txt"))
