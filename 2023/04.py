"""https://adventofcode.com/2023/day/4"""
from aoc import *


@solution(2023, 4, 1)
def part1(data: str) -> int:
    total = 0
    for card in data.splitlines():
        [winning, numbers] = card.split(": ")[1].split(" | ")
        winning = {int(num) for num in winning.split(" ") if num}
        numbers = {int(num) for num in numbers.split(" ") if num}
        won = winning & numbers
        if len(won) > 0:
            total += 2 ** (len(won)-1)
    return total


def score(cards: list[int], i: int) -> int:
    card = cards[i]
    if card == 0:
        return 1
    return sum(score(cards, j) for j in range(i+1, i+1+card)) + 1


@solution(2023, 4, 2)
def part2(data: str) -> int:
    cards: list[int] = []
    for card in data.splitlines():
        [winning, numbers] = card.split(": ")[1].split(" | ")
        winning = {int(num) for num in winning.split(" ") if num}
        numbers = {int(num) for num in numbers.split(" ") if num}
        won = winning & numbers
        cards.append(len(won))
    return sum(score(cards, i) for i in range(len(cards)))
