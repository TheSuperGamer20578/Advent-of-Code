"""https://adventofcode.com/2015/day/4#part2"""
from __future__ import annotations

from _md5 import md5
from typing import Any
from itertools import count

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 4, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    for i in count(1):
        hash_ = md5((input + str(i)).encode()).hexdigest()
        if hash_.startswith("0" * 6):
            return i
