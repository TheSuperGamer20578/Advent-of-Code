"""https://adventofcode.com/2023/day/7"""
from typing import Self

from aoc import *


class Hand:
    cards: str
    bid: int
    card_order: str
    p2: bool

    def __init__(self, line: str, card_order: str, p2: bool) -> None:
        [self.cards, bid] = line.split()
        self.bid = int(bid)
        self.card_order = card_order
        self.p2 = p2

    def __repr__(self) -> str:
        return f"{self.cards!r} {self.bid!r}"

    @staticmethod
    def _type(cards: str) -> int:
        card_set = set(cards)
        counts = [cards.count(card) for card in card_set]
        if 5 in counts:
            return 7
        if 4 in counts:
            return 6
        if 3 in counts and 2 in counts:
            return 5
        if 3 in counts:
            return 4
        if counts.count(2) == 2:
            return 3
        if 2 in counts:
            return 2
        return 1

    def type(self) -> int:
        if self.p2:
            return max(self._type(self.cards.replace("J", card)) for card in self.card_order)
        return self._type(self.cards)

    def card_gt(self, other: Self, offset: int = 0) -> bool:
        if self.card_order.index(self.cards[offset]) < self.card_order.index(other.cards[offset]):
            return True
        if self.card_order.index(self.cards[offset]) == self.card_order.index(other.cards[offset]):
            return self.card_gt(other, offset + 1)
        return False

    def __gt__(self, other: Self) -> bool:
        if self.type() > other.type():
            return True
        if self.type() == other.type():
            return self.card_gt(other)
        return False


@solution(2023, 7, 1)
def part1(data: str) -> int:
    # noinspection SpellCheckingInspection
    hands = [Hand(line, "AKQJT98765432", False) for line in data.splitlines()]
    hands.sort()
    return sum(hand.bid * i for i, hand in enumerate(hands, start=1))


@solution(2023, 7, 2)
def part2(data: str) -> int:
    # noinspection SpellCheckingInspection
    hands = [Hand(line, "AKQT98765432J", True) for line in data.splitlines()]
    hands.sort()
    return sum(hand.bid * i for i, hand in enumerate(hands, start=1))
