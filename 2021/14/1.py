"""https://adventofcode.com/2021/day/14"""
from typing import Any
from collections import defaultdict

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    template, rules = input.split("\n\n")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()}
    return template, rules


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
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


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
