"""https://adventofcode.com/2022/day/13#part2"""
from typing import Any
from dataclasses import dataclass

from aoc import *


def compare(a: list[int | list], b: list[int | list]) -> bool | None:
    for left, right in zip(a, b):
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
        elif isinstance(left, list) and isinstance(right, list):
            comp = compare(left, right)
            if comp is not None:
                return comp
        elif isinstance(left, int):
            comp = compare([left], right)
            if comp is not None:
                return comp
        else:
            comp = compare(left, [right])
            if comp is not None:
                return comp
    return len(a) < len(b) if len(a) != len(b) else None


@dataclass
class Packet:
    packet: list[list | int]

    def __lt__(self, other: "Packet") -> bool:
        return compare(self.packet, other.packet)
    
    def __eq__(self, other: "Packet") -> bool:
        return self.packet == other.packet


def parse(input: str) -> Any:
    """Parse the input"""
    return [Packet(eval(packet)) for packet in input.replace("\n\n", "\n").splitlines()]


@solution(2022, 13, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    div1 = Packet([[2]])
    div2 = Packet([[6]])
    input.append(div1)
    input.append(div2)
    input.sort()
    return (input.index(div1) + 1) * (input.index(div2) + 1)
