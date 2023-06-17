#!/usr/bin/env python3

def solution3(filename):
    sumprio = 0
    prio = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            length = len(line)
            one = set(line[:int(length / 2)])
            two = set(line[int(length / 2):])

            common = next(iter(one.intersection(two)))
            if common.isupper():
                prio = ord(common) - ord('A') + 1 + 26
            else:
                prio = ord(common) - ord('a') + 1
            sumprio += prio
    return sumprio,


if __name__ == '__main__':
    print(solution3("../input/3.txt"))
