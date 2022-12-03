"""https://adventofcode.com/2021/day/12"""
from typing import Any
from collections import defaultdict, deque

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    caves: dict[str, set[str]] = defaultdict(set)
    for connection in input.splitlines():
        cave, other = connection.split("-")
        caves[cave].add(other)
        caves[other].add(cave)
    return caves


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    queue = deque([("start",)])
    paths = 0
    while queue:
        path = queue.pop()
        for cave in input[path[-1]]:
            if cave.islower() and cave in path:
                continue
            if cave == "start":
                continue
            if cave == "end":
                paths += 1
                continue
            queue.append(path + (cave,))
    return paths


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
