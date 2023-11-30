"""https://adventofcode.com/2022/day/3#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    lines = input.splitlines()
    return [[set(lines[line]) for line in range(chunk, chunk + 3)] for chunk in range(0, len(lines), 3)]


def priority(char: str) -> int:
    """Get the priority of an item"""
    if char.islower():
        return ord(char) - ord("a") + 1
    return ord(char) - ord("A") + 27


@solution(2022, 3, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(priority((first & second & third).pop()) for first, second, third in input)
