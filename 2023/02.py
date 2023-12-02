"""https://adventofcode.com/2023/day/2"""
from collections import defaultdict
from math import prod

from aoc import *


def parse(data: str) -> dict[int, list[dict[str, int]]]:
    games = defaultdict(list)
    for line in data.splitlines():
        [_, game, cubes] = line.split(" ", 2)
        game = int(game[:-1])
        sets = cubes.split("; ")
        for s in sets:
            cubes = s.split(", ")
            games[game].append({c.split()[1]: int(c.split()[0]) for c in cubes})
    return games


@solution(2023, 2, 1)
def part1(data: str) -> int:
    games = parse(data)
    total = 0
    for i, game in games.items():
        for s in game:
            if s.get("red", 0) > 12:
                break
            if s.get("green", 0) > 13:
                break
            if s.get("blue", 0) > 14:
                break
        else:
            total += i
    return total


@solution(2023, 2, 2)
def part2(data: str) -> int:
    games = parse(data)
    total = 0
    for game in games.values():
        m = defaultdict(int)
        for s in game:
            for c, n in s.items():
                m[c] = max(m[c], n)
        total += prod(m.values())
    return total
