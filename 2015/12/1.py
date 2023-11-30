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


@solution(2015, 12, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return count(input)
