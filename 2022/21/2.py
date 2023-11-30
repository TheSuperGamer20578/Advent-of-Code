"""https://adventofcode.com/2022/day/21#part2"""
from typing import Any
from dataclasses import dataclass

from aoc import *


monkeys = {}


@dataclass
class Monkey:
    code: str

    def value(self) -> int:
        return eval(self.code, {**monkeys, "humn": humn})

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
    root = None
    for monkey in input.splitlines():
        key, value = monkey.split(": ", 1)
        if key == "root":
            root = value.split(" ")[::2]
            continue
        if key == "humn":
            continue
        if value.isnumeric():
            monkeys[key] = MonkeyInt(value)
        else:
            monkeys[key] = Monkey(value)
    return root


@solution(2022, 21, 2)
def solve(input: str) -> int | str:
    """Solve the puzzle"""
    input = parse(input)
    global humn
    a, b = input
    a = monkeys[a]
    b = monkeys[b]
    humn = MonkeyInt(10)
    aold = a.value()
    humn = MonkeyInt(1000)
    if a.value() == aold:
        target = aold
        changer = b
    else:
        target = b.value()
        changer = a
    high = 1e20
    low = 0
    while True:
        mid = (low + high) // 2
        humn = MonkeyInt(mid)
        difference = target - changer.value()
        if difference < 0:
            low = humn
        elif difference == 0:
            return humn
        elif difference > 0:
            high = humn
