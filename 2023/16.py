"""https://adventofcode.com/2023/day/16"""
from collections import deque
from typing import Generator

from aoc import *


def solve(grid: list[str], x: int, y: int, dx: int, dy: int) -> int:
    energised: set[tuple[int, int]] = set()
    queue = deque([(x, y, dx, dy)])
    seen: set[tuple[int, int, int, int]] = set()

    while queue:
        key = queue.popleft()
        x, y, dx, dy = key
        if y >= len(grid) or y < 0 or x >= len(grid[y]) or x < 0 or key in seen:
            continue
        seen.add(key)
        energised.add((x, y))
        match grid[y][x]:
            case ".":
                queue.append((x + dx, y + dy, dx, dy))
            case "/":
                queue.append((x - dy, y - dx, -dy, -dx))
            case "\\":
                queue.append((x + dy, y + dx, dy, dx))
            case "|" if dy != 0:
                queue.append((x + dx, y + dy, dx, dy))
            case "|" if dx != 0:
                queue.append((x, y + 1, 0, 1))
                queue.append((x, y - 1, 0, -1))
            case "-" if dx != 0:
                queue.append((x + dx, y + dy, dx, dy))
            case "-" if dy != 0:
                queue.append((x + 1, y, 1, 0))
                queue.append((x - 1, y, -1, 0))

    return len(energised)


def edges(grid: list[str]) -> Generator[tuple[int, int, int, int], None, None]:
    for x in range(len(grid[0])):
        yield x, 0, 0, 1
        yield x, len(grid) - 1, 0, -1
    for y in range(len(grid)):
        yield 0, y, 1, 0
        yield len(grid[y]) - 1, y, -1, 0


@solution(2023, 16, 1)
def part1(data: str) -> int:
    return solve(data.splitlines(), 0, 0, 1, 0)


@solution(2023, 16, 2)
def part2(data: str) -> int:
    grid = data.splitlines()
    return max(solve(grid, *args) for args in edges(grid))
