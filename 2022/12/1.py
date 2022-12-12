"""https://adventofcode.com/2022/day/12"""
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


def solve(input: list[list[int]]) -> int | str | Answer:
    """Solve the puzzle"""
    sx, sy = find(input, ord("S"))
    ex, ey = find(input, ord("E"))
    input[sx][sy] = ord("a")
    input[ex][ey] = ord("z")
    queue = deque([[(sx, sy, input[sx][sy])]])
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


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
