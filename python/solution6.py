#!/usr/bin/env python3

count = 795


def solution6(filename: str) -> tuple[int, int]:
    part1 = None
    part2 = None
    with open(filename) as file:
        for line in file:
            line = line.rstrip()

    for i in range(len(line)-3):
        if len(set(line[i:i+4])) == 4 and not part1:
            part1 = i + 4
        if len(set(line[i:i + 14])) == 14:
            part2 = i + 14
            break

    return part1, part2


if __name__ == '__main__':
    print(solution6("../input/6.txt"))
