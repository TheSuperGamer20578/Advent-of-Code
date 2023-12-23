"""https://adventofcode.com/2023/day/23"""
from collections import deque
from operator import itemgetter

from networkx import Graph

from aoc import *


@solution(2023, 23, 1)
def part1(data: str) -> int:
    grid: dict[tuple[int, int], tuple[int, int] | None] = {}
    rows = data.splitlines()
    sx, sy = rows[0].index("."), 0
    ex, ey = rows[-1].index("."), len(rows) - 1
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            match c:
                case "#":
                    continue
                case ".":
                    grid[x, y] = None
                case "^":
                    grid[x, y] = (0, -1)
                case "v":
                    grid[x, y] = (0, 1)
                case "<":
                    grid[x, y] = (-1, 0)
                case ">":
                    grid[x, y] = (1, 0)
                case _:
                    raise ValueError(f"Unknown character: {c!r}")

    queue = deque([(sx, sy, set())])
    longest = 0
    while queue:
        x, y, seen = queue.popleft()
        if (x, y) not in grid or (x, y) in seen:
            continue
        seen.add((x, y))
        if (x, y) == (ex, ey):
            longest = max(longest, len(seen))
            continue
        if (n := grid[x, y]) is not None:
            dx, dy = n
            queue.append((x + dx, y + dy, set(seen)))
        else:
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                queue.append((x + dx, y + dy, set(seen)))
    return longest - 1


@solution(2023, 23, 2)
def part2(data: str) -> int:
    grid: set[tuple[int, int]] = set()
    rows = data.splitlines()
    sx, sy = rows[0].index("."), 0
    ex, ey = rows[-1].index("."), len(rows) - 1
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            if c != "#":
                grid.add((x, y))
    graph = Graph()
    for x, y in grid:
        neighbors = {(x + dx, y + dy) for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)) if (x + dx, y + dy) in grid}
        graph.add_weighted_edges_from(((x, y), (nx, ny), 1) for nx, ny in neighbors)
    for node, edges in list(graph.adjacency()):
        if len(edges) == 2:
            graph.add_edge(*edges.keys(), weight=sum(map(itemgetter("weight"), edges.values())))
            graph.remove_node(node)

    queue = deque([((sx, sy), set(), 0)])
    longest = 0
    while queue:
        node, seen, length = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        if node == (ex, ey):
            longest = max(longest, length)
            continue
        for neighbor, attr in graph[node].items():
            queue.append((neighbor, set(seen), length + attr["weight"]))
    return longest
