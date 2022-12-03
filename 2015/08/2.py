"""https://adventofcode.com/2015/day/8#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [line.strip() for line in input.splitlines()]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return sum(line.count('"') + line.count("\\") + 2 for line in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
