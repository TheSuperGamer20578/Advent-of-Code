"""https://adventofcode.com/2022/day/21"""
from typing import Any
from dataclasses import dataclass

from aoc import *


monkeys = {}


@dataclass
class Monkey:
    code: str

    def value(self) -> int:
        return eval(self.code, monkeys)

    def __add__(self, other) -> int:
        if isinstance(other, Monkey):
            return self.value() + other.value()
        return self.value() + other

    def __sub__(self, other) -> int:
        if isinstance(other, Monkey):
            return self.value() - other.value()
        return self.value() - other

    def __mul__(self, other) -> int:
        if isinstance(other, Monkey):
            return self.value() * other.value()
        return self.value() * other

    def __truediv__(self, other) -> int:
        if isinstance(other, Monkey):
            return self.value() // other.value()
        return self.value() // other


class MonkeyInt(int):
    def __add__(self, other: int | Monkey) -> int:
        if isinstance(other, int):
            return super().__add__(other)
        return super().__add__(other.value())

    def __sub__(self, other: int | Monkey) -> int:
        if isinstance(other, int):
            return super().__sub__(other)
        return super().__sub__(other.value())

    def __mul__(self, other: int | Monkey) -> int:
        if isinstance(other, int):
            return super().__mul__(other)
        return super().__mul__(other.value())

    def __truediv__(self, other: int | Monkey) -> int:
        if isinstance(other, int):
            return super().__floordiv__(other)
        return super().__floordiv__(other.value())


def parse(input: str) -> Any:
    """Parse the input"""
    for monkey in input.splitlines():
        key, value = monkey.split(": ", 1)
        if value.isnumeric():
            monkeys[key] = MonkeyInt(value)
        else:
            monkeys[key] = Monkey(value)


@solution(2022, 21, 1)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    return monkeys["root"].value()
