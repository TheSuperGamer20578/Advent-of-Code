"""https://adventofcode.com/2022/day/10#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return sum(([None] if line == "noop" else [None, int(line.split(" ")[1])] for line in input.splitlines()), start=[])


_print = print


def print(*args, **kwargs):
    _print(*args, **kwargs, end="")


# TODO: Implement NoSubmit
# @solution(2022, 10, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    x = 1
    for i, instruction in enumerate(input):
        cursor = i % 40
        if cursor == 0:
            print("\n")
        if x - 1 <= cursor <= x + 1:
            print("\N{Black Square}")
        else:
            print(" ")
        if instruction is not None:
            x += instruction
    return NoSubmit(None)
