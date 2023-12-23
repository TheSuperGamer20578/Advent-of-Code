"""https://adventofcode.com/2023/day/22"""
from typing import Iterable, Iterator, Callable
from itertools import cycle

from aoc import *


def plot(bricks: Iterable[Iterable[tuple[int, int, int]]], predicate: Callable[[Iterable[tuple[int, int, int]]], bool] = None):
    """Plot a stack of bricks in 3D for debugging.
    Slow for large stacks.
    :param bricks: The bricks to plot.
    :param predicate: A predicate to colour the outlines of the bricks.
    """
    import numpy
    import matplotlib
    from matplotlib import pyplot

    colours = cycle(matplotlib.colors.XKCD_COLORS)
    fig = pyplot.figure()
    fig.tight_layout()
    ax = fig.add_subplot(
        projection='3d',
        xlim=(0, max(max(x for x, y, z in brick) for brick in bricks)+1),
        ylim=(0, max(max(y for x, y, z in brick) for brick in bricks)+1),
        zlim=(1, max(max(z for x, y, z in brick) for brick in bricks)+1),
        xlabel="X",
        ylabel="Y",
        zlabel="Z",
    )
    for i, brick in enumerate(bricks):
        xs, ys, zs = zip(*brick)
        array = numpy.full((max(xs) + 1, max(ys) + 1, max(zs) + 1), False, dtype=bool)
        for x, y, z in brick:
            array[x][y][z] = True
        ax.voxels(
            array,
            edgecolor="black" if predicate is None else "green" if predicate(brick) else "red",
            facecolor=next(colours),
        )
    pyplot.show()


class Stack:
    _highest: dict[tuple[int, int], int]
    _bricks: dict[tuple[int, int, int], frozenset[tuple[int, int, int]]]

    def __init__(self):
        self._highest = {}
        self._bricks = {}

    def __getitem__(self, item: tuple[int, int, int]) -> frozenset[tuple[int, int, int]]:
        return self._bricks[item]

    def __iter__(self) -> Iterator[frozenset[tuple[int, int, int]]]:
        return iter(set(self._bricks.values()))

    def __contains__(self, item) -> bool:
        return item in self._bricks

    def __len__(self) -> int:
        return len(set(self._bricks.values()))

    def highest(self, x: int, y: int) -> int:
        return self._highest.get((x, y), 0)

    def drop(self, item: Iterable[tuple[int, int, int]]) -> bool:
        z_offset = min(z - self.highest(x, y) - 1 for x, y, z in item)
        assert z_offset >= 0
        brick = frozenset((x, y, z - z_offset) for x, y, z in item)
        for x, y, z in brick:
            if self.highest(x, y) < z:
                self._highest[x, y] = z
            assert (x, y, z) not in self
            self._bricks[x, y, z] = brick
        return z_offset > 0


def brick_sort_key(brick: Iterable[tuple[int, int, int]]) -> int:
    return min(z for x, y, z in brick)


def parse(data: str) -> Stack:
    bricks = []
    for line in data.splitlines():
        to, fro = line.split("~")
        x1, y1, z1 = tuple(map(int, to.split(",")))
        x2, y2, z2 = tuple(map(int, fro.split(",")))
        assert sum([x1 != x2, y1 != y2, z1 != z2]) <= 1
        if x1 != x2:
            bricks.append({(x, y1, z1) for x in range(min(x1, x2), max(x1, x2)+1)})
        elif y1 != y2:
            bricks.append({(x1, y, z1) for y in range(min(y1, y2), max(y1, y2)+1)})
        elif z1 != z2:
            bricks.append({(x1, y1, z) for z in range(min(z1, z2), max(z1, z2)+1)})
        else:
            bricks.append({(x1, y1, z1)})
    bricks.sort(key=brick_sort_key)
    stack = Stack()

    for brick in bricks:
        stack.drop(brick)

    return stack


@solution(2023, 22, 1)
def part1(data: str) -> int:
    stack = parse(data)
    total = 0
    for brick in stack:
        for x, y, z in brick:
            if (x, y, z + 1) in brick:
                continue
            if (x, y, z + 1) in stack:
                n = stack[x, y, z + 1]
                for nx, ny, nz in n:
                    if (nx, ny, nz - 1) in brick or (nx, ny, nz - 1) in n:
                        continue
                    if (nx, ny, nz - 1) in stack:
                        break
                else:
                    break
        else:
            total += 1
    return total


@solution(2023, 22, 2)
def part2(data: str) -> int:
    stack = parse(data)
    total = 0
    for to_remove in stack:
        new_stack = Stack()
        for brick in sorted(stack, key=brick_sort_key):
            if brick != to_remove:
                total += new_stack.drop(brick)
    return total
