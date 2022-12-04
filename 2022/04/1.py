"""https://adventofcode.com/2022/day/4"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(map(int, first.split("-")), map(int, second.split("-"))) for first, second in [line.split(",") for line in input.splitlines()]]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    count = 0
    for ((first_start, first_end), (second_start, second_end)) in input:
        count += (first_start >= second_start and first_end <= second_end) or (first_start <= second_start and first_end >= second_end)
    return count


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
