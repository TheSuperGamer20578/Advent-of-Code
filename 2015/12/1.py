"""https://adventofcode.com/2015/day/12"""
from typing import Any
from json import loads

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return loads(input)


def count(tree) -> int:
    n = 0
    for item in tree:
        if isinstance(item, int):
            n += item
        elif isinstance(item, dict):
            n += count(item.values())
        elif isinstance(item, list):
            n += count(item)
    return n


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return count(input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
