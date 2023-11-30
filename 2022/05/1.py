"""https://adventofcode.com/2022/day/5"""
import re
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    start, proc = input.split("\n\n")
    start, _ = start.rsplit("\n", 1)
    start = [row[1::4] for row in start.splitlines()]
    start = {stack + 1: [row[stack] for row in start if row[stack] != " "] for stack in range(len(start[0]))}
    proc = [list(map(int, instruction)) for instruction in re.findall(r"^move (\d+) from (\d+) to (\d+)$", proc, re.MULTILINE)]
    return start, proc


# TODO: Implement irange()
# @solution(2022, 5, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    stacks, proc = input
    for n, f, t in proc:
        for _ in range(n):
            stacks[t].insert(0, stacks[f].pop(0))
    return "".join(stacks[stack][0] for stack in irange(1, len(stacks.keys())))
