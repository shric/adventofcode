#!/usr/bin/env python3

from itertools import zip_longest

count = 2597


def solution5(filename):
    part1 = part2 = 0
    stack_lines = []
    inst_lines = []
    push_list = stack_lines
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line == "":
                push_list = inst_lines
                continue
            push_list.append(line)
    lol = []
    for line in stack_lines:
        lol.append([line[i:i + 4] for i in range(0, len(line), 4)])

    transposed = []
    for i in list(map(list, zip_longest(*lol, fillvalue="    "))):
        transposed.append([x[1] for x in filter(lambda x: x != '    ', reversed(i[:-1]))])

    for line in inst_lines:
        _, quant, _, src, _, dst = line.split()
        for i in range(int(quant)):
            transposed[int(dst) - 1].append(transposed[int(src) - 1].pop())

    return "".join([x.pop() for x in transposed]), 0


if __name__ == '__main__':
    print(solution5("../input/5.txt"))
