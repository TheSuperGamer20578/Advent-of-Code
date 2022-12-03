"""https://adventofcode.com/2015/day/4"""
from __future__ import annotations

from typing import Any
from hashlib import md5
from itertools import count

# from aoc import * TODO


def parse(input: str) -> Any:
    """Parse the input"""
    return input


def solve(input: Any) -> int | str:
    """Solve the puzzle"""
    for i in count(1):
        hash_ = md5((input + str(i)).encode("utf-8")).hexdigest()
        if hash_.startswith("0" * 5):
            return i


if __name__ == "__main__":
    with open(".input") as f:
        input = parse(f.read().strip())
    print(solve(input))
