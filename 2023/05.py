"""https://adventofcode.com/2023/day/5"""
from dataclasses import dataclass

from aoc import *


@dataclass
class Map:
    dest_start: int
    source_start: int
    length: int

    def __contains__(self, item: int) -> bool:
        return self.source_start <= item < self.source_start + self.length

    def __getitem__(self, item: int) -> int:
        if item not in self:
            return item
        return self.dest_start + (item - self.source_start)

    def range(self, start: int, end: int) -> tuple[tuple[int, int], tuple[int, int] | None]:
        if start in self and end in self:
            return (self[start], self[end]), None
        if start in self:
            return (self[start], self.dest_start + self.length - 1), (self.source_start + self.length, end)
        if end in self:
            return (self.dest_start, self[end]), (start, self.source_start - 1)
        raise IndexError(f"Range {start}\u2013{end} not in map")


@dataclass
class MapList:
    maps: list[Map]

    def __getitem__(self, item: int) -> int:
        for map_ in self.maps:
            if item in map_:
                return map_[item]
        return item

    def range(self, start: int, end: int) -> list[tuple[int, int]]:
        extra: set[tuple[int, int]] = {(start, end)}
        ranges: list[tuple[int, int]] = []
        previous = None
        while extra != previous and len(extra) != 0:
            previous = extra.copy()
            for map_ in self.maps:
                for start, end in extra.copy():
                    if start in map_ or end in map_:
                        extra.remove((start, end))
                        new_range, new_extra = map_.range(start, end)
                        if new_range[0] >= new_range[1] or (new_extra is not None and new_extra[0] >= new_extra[1]):
                            print(f"Invalid: {start}\u2013{end} -> {new_range=} {new_extra=}")
                        ranges.append(new_range)
                        if new_extra is not None:
                            extra.add(new_extra)
        return ranges + list(extra)


def parse_maps(sections: list[str]) -> dict[str, MapList]:
    return {
        section.splitlines()[0].split("-to-")[0]: (
            section.splitlines()[0].split("-to-")[1].removesuffix(" map:"),
            MapList([
                Map(int(dest), int(source), int(length))
                for dest, source, length in map(str.split, section.splitlines()[1:])
            ]),
        )
        for section in sections
    }


@solution(2023, 5, 1)
def part1(data: str) -> int:
    [seeds, *sections] = data.split("\n\n")
    items = [int(seed) for seed in seeds.split()[1:]]
    maps = parse_maps(sections)
    type_ = "seed"
    while type_ != "location":
        type_, map_ = maps[type_]
        items = [map_[item] for item in items]
    return min(items)


@solution(2023, 5, 2)
def part2(data: str) -> int:
    [seeds, *sections] = data.split("\n\n")
    seeds = [int(seed) for seed in seeds.split()[1:]]
    ranges = [(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]
    maps = parse_maps(sections)
    type_ = "seed"
    while type_ != "location":
        type_, map_ = maps[type_]
        ranges = sum((map_.range(start, end) for start, end in ranges), start=[])
    return min(start for start, _ in ranges)
