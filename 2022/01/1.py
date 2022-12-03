"""https://adventofcode.com/2022/day/1"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [map(int, elf.splitlines()) for elf in input.split("\n\n")]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    return max(sum(elf) for elf in input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
