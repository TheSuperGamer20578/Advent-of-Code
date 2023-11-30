"""https://adventofcode.com/2015/day/10#part2"""
from typing import Any
from re import compile

from aoc import *

REGEX = compile(r"((.)\2*)")

def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 10, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    for _ in range(50):
        new = ""
        for match in REGEX.finditer(input):
            new += f"{len(match.group(1))}{match.group(2)}"
        input = new
    return len(input)
