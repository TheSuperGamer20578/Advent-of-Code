"""https://adventofcode.com/2015/day/2"""
from typing import Any
import re

from aoc import *

REGEX = re.compile(r"^(\d+)x(\d+)x(\d+)$")


def parse(input: str) -> Any:
    """Parse the input"""
    return list(map(lambda x: (int(x.group(1)), int(x.group(2)), int(x.group(3))), (REGEX.match(line.strip()) for line in input.splitlines())))


@solution(2015, 2, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    area = 0
    for present in input:
        sides = present[0]*present[1], present[1]*present[2], present[0]*present[2]
        area += sum(sides)*2 + min(sides)
    return area
