#!/usr/bin/env python3

count = 7900


def solution8(filename: str) -> tuple[int, int]:
    grid = []
    part1 = part2 = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            grid.append(line)

    maxheights = [[[0, 0, 0, 0] for y in grid[0]] for x in grid]
    for y in range(len(grid)):
        # Left to right
        maxheight = -1
        for x in range(len(grid[0])):
            height = int(grid[y][x])
            maxheights[y][x][0] = maxheight
            if height > maxheight:
                maxheight = height
        # Right to left
        maxheight = -1
        for x in range(len(grid[0]) - 1, -1, -1):
            height = int(grid[y][x])
            maxheights[y][x][1] = maxheight
            if height > maxheight:
                maxheight = height

    for x in range(len(grid[0])):
        # Top to bottom
        maxheight = -1
        for y in range(len(grid)):
            height = int(grid[y][x])
            maxheights[y][x][2] = maxheight
            if height > maxheight:
                maxheight = height
        # Bottom to top
        maxheight = -1
        for y in range(len(grid) - 1, -1, -1):
            height = int(grid[y][x])
            maxheights[y][x][3] = maxheight
            if height > maxheight:
                maxheight = height

    part1 = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            height = int(grid[y][x])
            maxheight = maxheights[y][x]
            visible = False
            for m in maxheight:
                if height > m:
                    visible = True
            if visible:
                part1 += 1

    return part1, part2


if __name__ == '__main__':
    print(solution8("../input/8.txt"))
