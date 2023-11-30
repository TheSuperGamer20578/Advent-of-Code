"""https://adventofcode.com/2022/day/2#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [round.split(" ") for round in input.splitlines()]


SCORE = {
	"X": {
		"A": 3 + 0,
		"B": 1 + 0,
		"C": 2 + 0,
	},
	"Y": {
		"A": 1 + 3,
		"B": 2 + 3,
		"C": 3 + 3,
	},
	"Z": {
		"A": 2 + 6,
		"B": 3 + 6,
		"C": 1 + 6,
	},
}


@solution(2022, 2, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    total = 0
    for them, result in input:
        total += SCORE[result][them]
    return total
