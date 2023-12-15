"""https://adventofcode.com/2023/day/15"""
import re
from collections import defaultdict, OrderedDict

from aoc import *


def hash_algorithm(string: str) -> int:
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value


@solution(2023, 15, 1)
def part1(data: str) -> int:
    return sum(hash_algorithm(string) for string in data.strip().split(","))


@solution(2023, 15, 2)
def part2(data: str) -> int:
    hashmap: dict[int, dict[str, int]] = defaultdict(OrderedDict)
    for instruction in data.strip().split(","):
        match re.fullmatch(r"^(\w+)([=-])(\d)?$", instruction).groups():
            case label, "=", lens:
                hashmap[hash_algorithm(label)][label] = int(lens)
            case label, "-", _:
                hashmap[hash_algorithm(label)].pop(label, None)
            case _:
                raise ValueError(f"Invalid instruction: {instruction!r}")
    return sum(
        (1 + box) * i * lens
        for box, lenses in hashmap.items()
        for i, (label, lens) in enumerate(lenses.items(), start=1)
    )
