"""https://adventofcode.com/2022/day/2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [round.split(" ") for round in input.splitlines()]


WIN = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}


@solution(2022, 2, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    total = 0
    for them, you in input:
        total += ord(you) - 87
        if ord(you) - 23 == ord(them):
            total += 3
        elif you == WIN[them]:
            total += 6
    return total
