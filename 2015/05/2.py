"""https://adventofcode.com/2015/day/5#part2"""
from __future__ import annotations

from typing import Any
import re

from aoc import *

REGEX_1 = re.compile(r"(..).*\1")
REGEX_2 = re.compile(r"(.).\1")



def parse(input: str) -> Any:
    """Parse the input"""
    return input.splitlines()
        

@solution(2015, 5, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    nice = 0
    for s in input:
        if REGEX_1.search(s) and REGEX_2.search(s):
            nice += 1
    return nice
