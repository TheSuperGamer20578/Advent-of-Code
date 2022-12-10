"""https://adventofcode.com/2022/day/10#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return sum(([None] if line == "noop" else [None, int(line.split(" ")[1])] for line in input.splitlines()), start=[])


_print = print


def print(*args, **kwargs):
    _print(*args, **kwargs, end="")


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
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


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
