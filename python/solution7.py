#!/usr/bin/env python3

from collections import defaultdict
from enum import Enum

count = 2148


class State(Enum):
    NONE = 0
    LISTING = 1
    COMMAND = 2


class AutoTree(defaultdict):
    def __init__(self):
        super().__init__()
        self.default_factory = type(self)


def BuildTree(filename: str) -> AutoTree:
    state = State.NONE
    root = AutoTree()
    cwd = root
    cwd_stack = [root]
    cwd[0] = 0
    sumsize = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("$"):
                state = State.COMMAND
            if line.startswith("$ cd "):
                target = line[5:]
                if target == "/":
                    cwd = root
                elif target == "..":
                    size = cwd[0]
                    cwd_stack.pop()
                    cwd = cwd_stack[-1]
                    cwd[0] += size
                else:
                    cwd = cwd[target]
                    if 0 not in cwd:
                        cwd[0] = 0
                    cwd_stack.append(cwd)
                continue

            if line == "$ ls":
                state = State.LISTING
                continue
            if state == State.LISTING:
                if line.startswith("dir "):
                    folder = line[4:]
                    cwd[folder] = AutoTree()
                    continue
                else:
                    size, name = line.split()
                    cwd[name] = int(size)
                    cwd[0] += int(size)
    # Simulate "cd .." back to root if we reach the end while still in a subdir
    while len(cwd_stack) > 1:
        size = cwd[0]
        cwd_stack.pop()
        cwd = cwd_stack[-1]
        cwd[0] += size
    return root


def get_all_kv(d, key_pred=lambda x: True, value_pred=lambda x: True):
    for key, value in d.items():
        if key_pred(key) and value_pred(value):
            yield key, value
        if isinstance(value, dict):
            yield from get_all_kv(value, key_pred, value_pred)


def solution7(filename: str) -> tuple[int, int]:
    tree = BuildTree(filename)

    # Part 1
    part1 = 0
    for _, val in get_all_kv(tree, lambda x: x == 0, lambda x: x <= 100000):
        part1 += val

    # Part 2
    used_space = tree[0]
    free_space = 70000000 - used_space
    required = 30000000
    free_require = required - free_space
    part2 = min([v for k, v in get_all_kv(tree, lambda x: x == 0, lambda x: x >= free_require)])
    return part1, part2


if __name__ == '__main__':
    print(solution7("../input/7.txt"))
