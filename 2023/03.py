"""https://adventofcode.com/2023/day/3"""
from aoc import *

# TODO: Move into aoc-cli
ORTHOGONAL = {(0, 1), (0, -1), (1, 0), (-1, 0)}
DIAGONAL = {(1, 1), (-1, 1), (1, -1), (-1, -1)}
DIRECTIONS = ORTHOGONAL | DIAGONAL


@solution(2023, 3, 1)
def part1(data: str) -> int:
    lines = data.splitlines()
    numbers: set[tuple[int, int]] = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                for (dx, dy) in DIRECTIONS:
                    ny = y + dy
                    nx = x + dx
                    if lines[ny][nx].isnumeric() and (nx - 1, ny) not in numbers:
                        numbers.add((nx, ny))
    total = 0
    seen: set[tuple[int, int]] = set()
    for (x, y) in numbers:
        if (x, y) in seen:
            continue
        ex = x
        while x != 0 and lines[y][x - 1].isnumeric():
            x -= 1
            seen.add((x, y))
        while ex < len(lines[y]) - 1 and lines[y][ex + 1].isnumeric():
            ex += 1
            seen.add((ex, y))
        total += int(lines[y][x:ex + 1])
    return total


@solution(2023, 3, 2)
def part2(data: str) -> int:
    lines = data.splitlines()
    gears: list[set[tuple[int, int]]] = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                adjacent: set[tuple[int, int]] = set()
                for (dx, dy) in DIRECTIONS:
                    ny = y + dy
                    nx = x + dx
                    if lines[ny][nx].isnumeric():
                        adjacent.add((nx, ny))
                u: set[tuple[int, int]] = set()
                for ax, ay in adjacent:
                    if (ax - 1, ay) not in adjacent:
                        u.add((ax, ay))
                if len(u) == 2:
                    gears.append(u)
    total = 0
    for gear in gears:
        ratio = 1
        for (x, y) in gear:
            ex = x
            while x != 0 and lines[y][x - 1].isnumeric():
                x -= 1
            while ex < len(lines[y]) - 1 and lines[y][ex + 1].isnumeric():
                ex += 1
            ratio *= int(lines[y][x:ex + 1])
        total += ratio
    return total
