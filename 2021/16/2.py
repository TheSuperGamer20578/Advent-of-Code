"""https://adventofcode.com/2021/day/16#part2"""
import math
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return list(bin(int(input, 16))[2:].zfill(8 * len(input) // 2).rstrip("0"))


def read(input, bits):
    stuff = input[:bits]
    for _ in range(bits):
        try:
            input.pop(0)
        except IndexError:
            stuff.append("0")
    return int("".join(stuff), 2)


def readl(input, bits):
    stuff = input[:bits]
    for _ in range(bits):
        try:
            input.pop(0)
        except IndexError:
            stuff.append("0")
    return stuff


def evaluate(input, n = -1):
    packets = []
    while input and n != 0:
        n -= 1
        read(input, 3)
        t = read(input, 3)
        if t == 4:
            ret = 0
            while True:
                chunk = read(input, 5)
                ret = (ret << 4) | (chunk&0b1111)
                if not chunk >> 4:
                    break
            packets.append(ret)
        else:
            length_type = read(input, 1)
            length = read(input, 11 if length_type else 15)
            if length_type:
                subpackets = evaluate(input, length)
            else:
                subpackets = evaluate(readl(input, length))
            if t == 0:
                packets.append(sum(subpackets))
            elif t == 1:
                packets.append(math.prod(subpackets))
            elif t == 2:
                packets.append(min(subpackets))
            elif t == 3:
                packets.append(max(subpackets))
            elif t == 5:
                packets.append(int(subpackets[0] > subpackets[1]))
            elif t == 6:
                packets.append(int(subpackets[0] < subpackets[1]))
            elif t == 7:
                packets.append(int(subpackets[0] == subpackets[1]))
    return packets


# TODO: Fix
# @solution(2021, 16, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return evaluate(input)[0]
