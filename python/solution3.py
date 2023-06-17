#!/usr/bin/env python3

count = 1824


def prio(c):
    if c.isupper():
        return ord(c) - ord('A') + 1 + 26
    else:
        return ord(c) - ord('a') + 1


def solution3(filename):
    part1 = 0
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            lines.append(line)

    for line in lines:
        length = len(line)
        one = set(line[:int(length / 2)])
        two = set(line[int(length / 2):])

        common = next(iter(one.intersection(two)))
        part1 += prio(common)

    part2 = 0
    for a in zip(*[iter(lines)] * 3):
        part2 += prio(next(iter(set(a[0]).intersection(set(a[1])).intersection(set(a[2])))))

    return part1, part2


if __name__ == '__main__':
    print(solution3("../input/3.txt"))
