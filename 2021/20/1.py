"""https://adventofcode.com/2021/day/20"""
from typing import Any

from aoc import *

TRANSLATION = {
    ".": False,
    "#": True
}


def neighbours(r: int, c: int):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            yield r + dr, c + dc


def parse(input: str) -> tuple[list[bool], list[tuple[int, int]]]:
    """Parse the input"""
    enhancement, image = input.split("\n\n")
    enhancement = [TRANSLATION[char] for char in enhancement]
    image = {(r, c) for r, row in enumerate(image.splitlines()) for c, char in enumerate(row) if char == "#"}
    return enhancement, image


def solve(input: tuple[list[bool], list[tuple[int, int]]]) -> int | str | Answer:
    """Solve the puzzle"""
    enhancement, image = input
    for iteration in range(2):
        on = iteration % 2 == 0
        new_image: set[tuple[int, int]] = set()
        minr = min([r for r, _ in image])
        maxr = max([r for r, _ in image])
        minc = min([c for _, c in image])
        maxc = max([c for _, c in image])
        for r in irange(minr - 1, maxr + 1):
            for c in irange(minc - 1, maxc + 1):
                index = 0
                for i, neighbour in enumerate(neighbours(r, c)):
                    index |= ((neighbour in image) == on) << (8-i)
                if enhancement[index] != on:
                    new_image.add((r, c))
        image = new_image
    return len(image)


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
