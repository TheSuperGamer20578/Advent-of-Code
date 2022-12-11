"""https://adventofcode.com/2022/day/11"""
from typing import Any
from dataclasses import dataclass

from aoc import *


@dataclass
class Monkey:
    items: list[int]
    operation: str
    test: int
    true: int
    false: int
    inspections: int = 0

    def __gt__(self, other: "Monkey"):
        return self.inspections > other.inspections

    def __lt__(self, other: "Monkey"):
        return self.inspections < other.inspections


def parse(input: str) -> Any:
    """Parse the input"""
    monkeys = [{line.split(":", 1)[0].strip(): line.split(":", 1)[1].strip() for line in monkey.splitlines()} for monkey in input.split("\n\n")]
    return [Monkey(
        items=list(map(int, str(monkey["Starting items"]).split(", "))),
        operation=monkey["Operation"].removeprefix("new = "),
        test=int(monkey["Test"].split(" ")[-1]),
        true=int(monkey["If true"].split(" ")[-1]),
        false=int(monkey["If false"].split(" ")[-1]),
    ) for monkey in monkeys]


def solve(input: Any) -> int | str | Answer:
    """Solve the puzzle"""
    for _ in range(20):
        for monkey in input:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                item = eval(monkey.operation, {"old": item})
                item //= 3
                input[monkey.true if item % monkey.test == 0 else monkey.false].items.append(item)
                monkey.inspections += 1
    m1, m2 = *sorted(input)[-2:],
    return m1.inspections * m2.inspections


if __name__ == "__main__":
    from aoc.run import run
    run(parse, solve)
