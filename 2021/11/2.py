"""https://adventofcode.com/2021/day/11#part2"""
from typing import Any
from itertools import product, count

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [[int(energy) for energy in line] for line in input.split("\n")]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    flashes = 0
    flashed: set[tuple[int, int]] = set()
    ready: list[tuple[int, int]] = []
    for step in count():
        flashed.clear()
        for x in range(len(input)):
            for y in range(len(input[0])):
                input[x][y] += 1
                if input[x][y] > 9:
                    ready.append((x, y))
                    flashed.add((x, y))
        while len(ready) > 0:
            x, y = ready.pop()
            for dx, dy in product([-1, 0, 1], repeat=2):
                if dx == 0 == dy:
                    continue
                if 0 <= x + dx < len(input) and 0 <= y + dy < len(input[0]):
                    input[x + dx][y + dy] += 1
                    if input[x + dx][y + dy] > 9 and (x + dx, y + dy) not in flashed:
                        ready.append((x + dx, y + dy))
                        flashed.add((x + dx, y + dy))
        for x, line in enumerate(input):
            for y, crab in enumerate(line):
                if crab > 9:
                    input[x][y] = 0
                    flashes += 1
        if len(set(sum(input, start=[]))) == 1:
            return step + 1


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
