"""https://adventofcode.com/2021/day/22#part2"""
import re
from itertools import product
from typing import Any

from aoc import *


def parse(input: str) -> list[tuple[bool, int, int, int, int, int, int]]:
    """Parse the input"""
    regex = re.compile(r"^(on|off) x=(-?[0-9]*)\.\.(-?[0-9]*),y=(-?[0-9]*)\.\.(-?[0-9]*),z=(-?[0-9]*)\.\.(-?[0-9]*)$")
    steps = []
    for step in input.splitlines():
        match = regex.match(step)
        assert match
        group = match.group
        steps.append((True if group(1) == "on" else False, int(group(2)), int(group(3)), int(group(4)), int(group(5)), int(group(6)), int(group(7))))
    return steps


# TODO: Implement irange()
# @solution(2021, 22, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    on = set()
    for step in input:
        enable, x1, x2, y1, y2, z1, z2 = step
        if enable:
            on |= set(product(irange(x1, x2), irange(y1, y2), irange(z1, z2)))
        else:
            on -= set(product(irange(x1, x2), irange(y1, y2), irange(z1, z2)))
    return len(on)
