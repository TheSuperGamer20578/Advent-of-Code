"""https://adventofcode.com/2015/day/8"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(line.strip(), eval(line)) for line in input.splitlines()]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return sum(len(code) - len(string) for code, string in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
