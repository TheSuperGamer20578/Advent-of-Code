"""https://adventofcode.com/2021/day/12#part2"""
from typing import Any
from collections import defaultdict, deque
from dataclasses import dataclass

from aoc import *


@dataclass
class Path:
    path: tuple[str]
    small2: bool = False

    def __add__(self, other):
        return Path(self.path + (other,), self.small2 or (other.islower() and other in self.path))


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
    queue = deque([Path(("start",))])
    paths = 0
    while queue:
        path = queue.pop()
        for cave in input[path.path[-1]]:
            if cave.islower() and cave in path.path and path.small2:
                continue
            if cave == "start":
                continue
            if cave == "end":
                paths += 1
                continue
            queue.append(path + cave)
    return paths


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
