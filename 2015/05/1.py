"""https://adventofcode.com/2015/day/5"""
from __future__ import annotations

from typing import Any
from itertools import pairwise

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input.splitlines()
        

@solution(2015, 5, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    nice = 0
    for s in input:
        if any(ss in s for ss in ("ab", "cd", "pq", "xy")):
            continue
        if (s.count("a")
          + s.count("e")
          + s.count("i")
          + s.count("o")
          + s.count("u")
          < 3):
            continue
        if not any(ss[0] == ss[1] for ss in pairwise(s)):
            continue
        nice += 1
    return nice
