"""https://adventofcode.com/2022/day/7"""
from typing import Any
from collections import Counter

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    path = []
    files = {}
    for command in input.split("\n$ "):
        command, *output = command.splitlines()
        match command.split(" ", 1):
            case "cd", "/":
                path.clear()
            case "cd", "..":
                path.pop()
            case "cd", dir:
                path.append(dir)
            case "ls",:
                for file in output:
                    size, file = file.split(" ", 1)
                    if size != "dir":
                        files[(*path, file)] = int(size)
    return files


@solution(2022, 7, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    dirs = Counter()
    for (*dir, _), size in input.items():
        if size is not None:
            for i in range(len(dir)):
                dirs[tuple(dir[:i + 1])] += size
    return sum(size for size in dirs.values() if size <= 100000)
