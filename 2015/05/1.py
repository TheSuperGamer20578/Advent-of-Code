"""https://adventofcode.com/2015/day/5"""
from __future__ import annotations

from typing import Any
from itertools import pairwise

# from aoc import * TODO


def parse(input: str) -> Any:
    """Parse the input"""
    return input.splitlines()
        

def solve(input: Any) -> int | str:
    """Solve the puzzle"""
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


if __name__ == "__main__":
    with open(".input") as f:
        input = parse(f.read().strip())
    print(solve(input))
