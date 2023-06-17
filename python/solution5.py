#!/usr/bin/env python3

from itertools import zip_longest

count = 2985


def solution5(filename: str) -> tuple[str, str]:
    stack_lines: list[str] = []
    inst_lines: list[str] = []
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
        x: list[str]
        part1.append([x[1] for x in filter(lambda x: x != '    ', reversed(i[:-1]))])

    part2 = [x[:] for x in part1]

    for line in inst_lines:
        _, quant, _, src, _, dst = line.split()
        quant = int(quant)
        dst = int(dst)-1
        src = int(src)-1
        for i in range(quant):
            part1[dst].append(part1[src].pop())

        part2[dst].extend(part2[src][-quant:])
        del (part2[src][-quant:])

    return "".join([x.pop() for x in part1]), "".join([x.pop() for x in part2])


if __name__ == '__main__':
    print(solution5("../input/5.txt"))
