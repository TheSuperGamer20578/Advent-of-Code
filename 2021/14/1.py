"""https://adventofcode.com/2021/day/14"""
from typing import Any
from collections import defaultdict

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    template, rules = input.split("\n\n")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()}
    return template, rules


@solution(2021, 14, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    poly, rules = input
    for _ in range(10):
        offset = 1
        for index, (a, b) in enumerate(zip(poly[:], poly[1:])):
            if a + b in rules:
                poly = poly[:index + offset] + rules[a + b] + poly[index + offset:]
                offset += 1
    counts = defaultdict(int)
    for char in poly:
        counts[char] += 1
    return max(counts.values()) - min(counts.values())
