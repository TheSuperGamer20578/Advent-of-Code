"""https://adventofcode.com/2022/day/12#part2"""
from typing import Any
from collections import deque

from aoc import *


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse(input: str) -> Any:
    """Parse the input"""
    return [list(map(ord, line)) for line in input.splitlines()]


def find(to_search: list[list[Any]], to_find: Any) -> tuple[int, int] | None:
    for i, slist in enumerate(to_search):
        try:
            found = slist.index(to_find)
        except ValueError:
            continue
        return i, found
    return None


def find_all(to_search: list[list[Any]], to_find: Any) -> list[tuple[int, int]]:
    return [(x, y) for x, row in enumerate(to_search) for y, item in enumerate(row) if item == to_find]


@solution(2022, 12, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    sx, sy = find(input, ord("S"))
    ex, ey = find(input, ord("E"))
    input[sx][sy] = ord("a")
    input[ex][ey] = ord("z")
    queue = deque([[(x, y, ord("a"))] for x, y in find_all(input, ord("a"))])
    seen = set()
    while queue:
        path = queue.popleft()
        x, y, height = path[-1]
        if (x, y) == (ex, ey):
            return len(path) - 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0:
                continue
            try:
                nh = input[nx][ny]
            except IndexError:
                continue
            if (nx, ny) in seen:
                continue
            if not nh <= height + 1:
                continue
            queue.append(path + [(nx, ny, nh)])
            seen.add((nx, ny))
