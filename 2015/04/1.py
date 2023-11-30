"""https://adventofcode.com/2015/day/4"""
from __future__ import annotations

from typing import Any
from hashlib import md5
from itertools import count

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return input


@solution(2015, 4, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    for i in count(1):
        hash_ = md5((input + str(i)).encode("utf-8")).hexdigest()
        if hash_.startswith("0" * 5):
            return i
