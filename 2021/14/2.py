"""https://adventofcode.com/2021/day/14#part2"""
from typing import Any
from collections import defaultdict

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    template, rules = input.split("\n\n")
    rules = {rule.split(" -> ")[0]: rule.split(" -> ")[1] for rule in rules.splitlines()}
    count = defaultdict(int)
    for a, b in zip(template, template[1:]):
        count[a + b] += 1
    return count, rules, template[-1]


@solution(2021, 14, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    poly, rules, last_char = input
    for _ in range(40):
        last = poly.copy()
        for rule, thing in rules.items():
            poly[rule[0] + thing] += last[rule]
            poly[thing + rule[1]] += last[rule]
            poly[rule] -= last[rule]
    counts = defaultdict(int)
    counts[last_char] += 1
    for pair, count in poly.items():
        counts[pair[0]] += count
    return max(counts.values()) - min(counts.values())
