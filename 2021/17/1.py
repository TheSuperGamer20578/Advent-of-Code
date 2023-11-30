"""https://adventofcode.com/2021/day/17"""
import math
from typing import Any
from collections import namedtuple

from aoc import *

bounds = namedtuple("bounds", ["x1", "x2", "y1", "y2"])


def parse(input: str) -> bounds:
    """Parse the input"""
    return bounds(*map(int, input[15:].replace(", y=", "..").split("..")))


@solution(2021, 17, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    best = -math.inf
    for dx in range(-200, 200):
        for dy in range(-200, 200):
            vx = dx
            vy = dy
            x = y = 0
            highest = -math.inf
            while x <= input.x2 and y >= input.y2:
                x += vx
                y += vy
                highest = max(highest, y)
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
                if input.x1 <= x <= input.x2 and input.y1 <= y <= input.y2:
                    best = max(best, highest)
                    break
    return best
