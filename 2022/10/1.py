"""https://adventofcode.com/2022/day/10"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return sum(([None] if line == "noop" else [None, int(line.split(" ")[1])] for line in input.splitlines()), start=[])


@solution(2022, 10, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    x = 1
    answer = 0
    for i, instruction in enumerate(input, 1):
        if i in (20, 60, 100, 140, 180, 220):
            answer += x * i
        if instruction is not None:
            x += instruction
    return answer
