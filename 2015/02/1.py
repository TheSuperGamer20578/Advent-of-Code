"""https://adventofcode.com/2015/day/2"""
from typing import Any
import re

from aoc import *

REGEX = re.compile(r"^(\d+)x(\d+)x(\d+)$")


def parse(input: str) -> Any:
    """Parse the input"""
    return list(map(lambda x: (int(x.group(1)), int(x.group(2)), int(x.group(3))), (REGEX.match(line.strip()) for line in input.splitlines())))


def solve(input: Any) -> Answer:
    """Solve the puzzle"""
    area = 0
    for present in input:
        sides = present[0]*present[1], present[1]*present[2], present[0]*present[2]
        area += sum(sides)*2 + min(sides)
    return Answer(area)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
