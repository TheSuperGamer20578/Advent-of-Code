"""https://adventofcode.com/2021/day/21"""
from typing import Any
from functools import cache

from aoc import *


def increment(num: int, max: int, amount: int = 1) -> int:
    num += amount
    while num > max:
        num -= max
    return num


def parse(input: str) -> Any:
    """Parse the input"""
    return int(input.splitlines()[0].split(" ")[-1]), int(input.splitlines()[1].split(" ")[-1])


@cache
def count_win(player1: int, player2: int, score1: int, score2: int) -> tuple[int, int]:
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    ans = 0, 0
    for r1 in (1, 2, 3):
        for r2 in (1, 2, 3):
            for r3 in (1, 2, 3):
                roll = r1 + r2 + r3
                re1, re2 = count_win(player2, increment(player1, 10, roll), score2, score1 + increment(player1, 10, roll))
                ans = ans[0] + re2, ans[1] + re1
    return ans


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    player1, player2 = input
    return max(count_win(player1, player2, 0, 0))


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
