"""https://adventofcode.com/2019/day/2"""
from typing import Any

from aoc import *


def parse(input: str) -> Any:
    """Parse the input"""
    return [int(num) for num in input.split(",")]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    pc = 0
    # input[1] = 12
    # input[2] = 2
    while True:
        print(input)
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


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
