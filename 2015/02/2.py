"""https://adventofcode.com/2015/day/2#part2"""
from typing import Any
from math import prod
import re

from aoc import *

REGEX = re.compile(r"^(\d+)x(\d+)x(\d+)$")


def parse(input: str) -> Any:
    """Parse the input"""
    return list(map(lambda x: (int(x.group(1)), int(x.group(2)), int(x.group(3))), (REGEX.match(line.strip()) for line in input.splitlines())))


@solution(2015, 2, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    ribbon = 0
    for present in input:
        faces = (present[0]+present[1]) * 2, (present[1]+present[2]) * 2, (present[0]+present[2]) * 2
        ribbon += min(faces) + prod(present)
    return ribbon
