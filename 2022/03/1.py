"""https://adventofcode.com/2022/day/3"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(set(sack[:len(sack) // 2]), set(sack[len(sack) // 2:])) for sack in input.splitlines()]


def priority(char: str) -> int:
    """Get the priority of an item"""
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


@solution(2022, 3, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(priority((first & last).pop()) for first, last in input)
