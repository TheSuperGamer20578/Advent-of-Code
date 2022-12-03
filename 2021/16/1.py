"""https://adventofcode.com/2021/day/16"""
import math
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return list(bin(int(input, 16))[2:].zfill(8 * len(input) // 2).rstrip("0"))


def read(input, bits):
    stuff = input[:bits]
    for _ in range(bits):
        input.pop(0)
    return int("".join(stuff), 2)


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    versions = 0
    while input:
        versions += read(input, 3)
        t = read(input, 3)
        if t == 4:
            while read(input, 5) >> 4:
                pass
        else:
            read(input, 11 if read(input, 1) else 15)
    return versions


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
