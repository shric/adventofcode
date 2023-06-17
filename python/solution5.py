#!/usr/bin/env python3

from itertools import zip_longest

count = 2027


def solution5(filename):
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

    part1 = []
    for i in list(map(list, zip_longest(*lol, fillvalue="    "))):
        part1.append([x[1] for x in filter(lambda x: x != '    ', reversed(i[:-1]))])

    part2 = [x[:] for x in part1]

    for line in inst_lines:
        _, quant, _, src, _, dst = line.split()
        quant = int(quant)
        for i in range(quant):
            part1[int(dst) - 1].append(part1[int(src) - 1].pop())

        part2[int(dst) - 1].extend(part2[int(src) - 1][-quant:])
        del (part2[int(src) - 1][-quant:])

    return "".join([x.pop() for x in part1]), "".join([x.pop() for x in part2])


if __name__ == '__main__':
    print(solution5("../input/5.txt"))
