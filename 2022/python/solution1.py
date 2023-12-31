#!/usr/bin/env python3

count = 5780


def solution1(filename: str) -> tuple[int, int]:
    maxsum = 0
    sums = []
    with open(filename) as file:
        s = 0
        for line in file:
            line = line.rstrip()
            if line == '':
                sums.append(s)
                if s > maxsum: maxsum = s
                s = 0
                continue
            s += int(line)
    return maxsum, sum(sorted(sums, reverse=True)[:3])


if __name__ == '__main__':
    print(solution1("../input/1.txt"))
