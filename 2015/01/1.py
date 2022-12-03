"""https://adventofcode.com/2015/day/1"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> Answer:
    """Solve the puzzle"""
    return Answer(input.count("(") - input.count(")"))


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
