"""https://adventofcode.com/2022/day/1#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [map(int, elf.splitlines()) for elf in input.split("\n\n")]


@solution(2022, 1, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return sum(sorted(sum(elf) for elf in input)[-3:])
