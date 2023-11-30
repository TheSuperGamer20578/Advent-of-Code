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


@solution(2021, 16, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
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
