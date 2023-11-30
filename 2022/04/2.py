"""https://adventofcode.com/2022/day/4#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [(map(int, first.split("-")), map(int, second.split("-"))) for first, second in [line.split(",") for line in input.splitlines()]]


@solution(2022, 4, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    count = 0
    for ((first_start, first_end), (second_start, second_end)) in input:
        count += (first_start <= second_start <= first_end) or (first_start <= second_end <= first_end) or (second_start <= first_start <= second_end) or (second_start <= first_end <= second_end)
    return count
