"""https://adventofcode.com/2023/day/1"""
import regex

from aoc import *

WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


@solution(2023, 1, 1)
def part1(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        nums = [int(n) for n in line if n.isnumeric()]
        n1 = nums[0]
        n2 = nums[-1]
        n = 10*n1 + n2
        sum += n
    return sum


@solution(2023, 1, 2)
def part2(data: str) -> int:
    sum = 0
    for line in data.splitlines():
        # language=PythonRegExp
        nums = regex.findall(r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True)
        n1 = nums[0]
        n2 = nums[-1]
        if n1.isnumeric():
            n1 = int(n1)
        else:
            n1 = WORDS.index(n1)
        if n2.isnumeric():
            n2 = int(n2)
        else:
            n2 = WORDS.index(n2)
        n = 10*n1 + n2
        sum += n
    return sum
