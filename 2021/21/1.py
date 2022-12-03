"""https://adventofcode.com/2021/day/21#part2"""
from typing import Any

from aoc import *


def increment(num: int, max: int, amount: int = 1) -> int:
    num += amount
    while num > max:
        num -= max
    return num


def parse(input: str) -> Any:
    """Parse the input"""
    return int(input.splitlines()[0].split(" ")[-1]), int(input.splitlines()[1].split(" ")[-1])


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    player1, player2 = input
    dice = rolls = score1 = score2 = 0
    p1 = False
    while max(score1, score2) < 1000:
        move = 0
        for _ in range(3):
            dice = increment(dice, 100)
            move += dice
            rolls += 1
        player1 = increment(player1, 10, move)
        score1 += player1
        if score1 >= 1000:
            p1 = True
            break
        move = 0
        for _ in range(3):
            dice = increment(dice, 100)
            move += dice
            rolls += 1
        player2 = increment(player2, 10, move)
        score2 += player2
    return (score2 if p1 else score1) * rolls


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
