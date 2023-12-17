"""https://adventofcode.com/2023/day/17"""
from heapq import heappush, heappop

from aoc import *


def solve(grid: list[list[int]], p2: bool) -> int:
    queue = [(0, 0, 0, -1, 0)]
    seen = set()

    while len(queue) > 0:
        loss, x, y, direction, travel = heappop(queue)
        if (x, y, direction, travel) in seen:
            continue
        seen.add((x, y, direction, travel))
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            return loss
        for i, (dx, dy) in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if i == direction and travel < (10 if p2 else 3) or direction == -1:
                    heappush(queue, (loss + grid[ny][nx], nx, ny, i, travel + 1))
                elif i % 2 != direction % 2 and (not p2 or travel >= 4):
                    heappush(queue, (loss + grid[ny][nx], nx, ny, i, 1))


@solution(2023, 17, 1)
def part1(data: str) -> int:
    grid = [[int(char) for char in row] for row in data.splitlines()]
    return solve(grid, False)


@solution(2023, 17, 2)
def part2(data: str) -> int:
    grid = [[int(char) for char in row] for row in data.splitlines()]
    return solve(grid, True)
