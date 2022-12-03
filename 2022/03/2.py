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


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return sum(priority((first & second & third).pop()) for first, second, third in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
