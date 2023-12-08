"""https://adventofcode.com/2023/day/8"""
import re
from itertools import cycle
from math import lcm

from aoc import *


@solution(2023, 8, 1)
def part1(data: str) -> int:
    [instructions, nodes] = data.split("\n\n")
    nodes = {
        node: {"L": l, "R": r}
        for node, l, r in re.findall(r"^(\w+) = \((\w+), (\w+)\)$", nodes, re.MULTILINE)
    }

    node = "AAA"
    for i, instruction in enumerate(cycle(instructions), 1):
        node = nodes[node][instruction]
        if node == "ZZZ":
            return i


@solution(2023, 8, 2)
def part2(data: str) -> int:
    [instructions, nodes] = data.split("\n\n")
    nodes = {
        node: {"L": l, "R": r}
        for node, l, r in re.findall(r"^(\w+) = \((\w+), (\w+)\)$", nodes, re.MULTILINE)
    }

    intervals = set()
    for node in nodes:
        if node.endswith("A"):
            for i, instruction in enumerate(cycle(instructions), 1):
                node = nodes[node][instruction]
                if node.endswith("Z"):
                    intervals.add(i)
                    break
    return lcm(*intervals)
