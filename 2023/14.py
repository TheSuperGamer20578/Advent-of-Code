"""https://adventofcode.com/2023/day/14"""
from typing import Iterable

from aoc import *


def rotate(rows: Iterable[str]) -> list[str]:
    return ["".join(row) for row in zip(*rows)]


def shift_rows(rows: Iterable[str], west: bool) -> list[str]:
    return [
        "#".join("".join(sorted(run, reverse=west)) for run in row.split("#"))
        for row in rows
    ]


def shift_cols(cols: Iterable[str], north: bool) -> list[str]:
    return rotate(shift_rows(("".join(col) for col in zip(*cols)), north))


def load(rows: Iterable[str]) -> int:
    total = 0
    for col in rotate(rows):
        for i, char in enumerate(col):
            if char == "O":
                total += len(col) - i
    return total


@solution(2023, 14, 1)
def part1(data: str) -> int:
    return load(shift_cols(data.splitlines(), True))


@solution(2023, 14, 2)
def part2(data: str) -> int:
    cycles = 1_000_000_000
    rows = data.splitlines()
    seen = {}
    i = 0
    while i < cycles:
        if tuple(rows) in seen:
            cycle_len = i - seen[tuple(rows)]
            if i + cycle_len < cycles:
                i = cycles - (cycles - i) % cycle_len
                continue
        seen[tuple(rows)] = i
        rows = shift_cols(rows, True)
        rows = shift_rows(rows, True)
        rows = shift_cols(rows, False)
        rows = shift_rows(rows, False)
        i += 1
    return load(rows)
