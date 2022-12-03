"""https://adventofcode.com/2015/day/10"""
from typing import Any
from re import compile

from aoc import *

REGEX = compile(r"((.)\2*)")

def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    for _ in range(40):
        new = ""
        for match in REGEX.finditer(input):
            new += f"{len(match.group(1))}{match.group(2)}"
        input = new
    return len(input)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
