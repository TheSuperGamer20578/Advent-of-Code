"""https://adventofcode.com/2019/day/2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


@solution(2019, 2, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    pc = 0
    # input[1] = 12
    # input[2] = 2
    while True:
        # print(input)
        match input[pc]:
            case 1:
                input[input[pc + 3]] = input[pc + 1] + input[pc + 2]
                pc += 4
            case 2:
                input[input[pc + 3]] = input[pc + 1] + input[pc + 2]
                pc += 4
            case 99:
                break
            case _:
                raise Exception('"Encountering an unknown opcode means something went wrong."')
    return input
