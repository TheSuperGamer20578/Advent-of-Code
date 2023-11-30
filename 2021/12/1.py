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


@solution(2021, 12, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
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
