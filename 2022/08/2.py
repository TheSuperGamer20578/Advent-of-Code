"""https://adventofcode.com/2022/day/8#part2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [list(map(int, row)) for row in input.splitlines()]


@solution(2022, 8, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    highest_score = 0
    for x, row in enumerate(input):
        for y, tree in enumerate(row):
            score = 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x, y
                trees = 0
                highest = -1
                while 0 <= nx + dx < len(input) and 0 <= ny + dy < len(input[0]):
                    nx += dx
                    ny += dy
                    ntree = input[nx][ny]
                    trees += 1
                    if ntree >= tree:
                        break
                    if ntree > highest:
                        highest = ntree
                score *= trees
            if score >= highest_score:
                highest_score = score
    return highest_score
