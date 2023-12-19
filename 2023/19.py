"""https://adventofcode.com/2023/day/19"""
from collections import deque
from math import prod

from aoc import *


@solution(2023, 19, 1)
def part1(data: str) -> int:
    workflows, parts = data.split("\n\n")
    workflows = {
        workflow.split("{")[0]: [step.split(":") for step in workflow.split("{")[1][:-1].split(",")]
        for workflow in workflows.splitlines()
    }
    total = 0
    for part in parts.splitlines():
        values = {}
        exec(part[1:-1].replace(",", "\n"), values)
        workflow = "in"
        while workflow not in "AR":
            for step in workflows[workflow]:
                if len(step) == 1:
                    workflow = step[0]
                else:
                    condition, to = step
                    if eval(condition, values):
                        workflow = to
                        break
        if workflow == "A":
            total += sum(values[var] for var in "xmas")
    return total


@solution(2023, 19, 2)
def part2(data: str) -> int:
    workflows = {
        workflow.split("{")[0]: [step.split(":") for step in workflow.split("{")[1][:-1].split(",")]
        for workflow in data.split("\n\n")[0].splitlines()
    }
    queue = deque([("in", {var: 1 for var in "xmas"}, {var: 4000 for var in "xmas"})])
    answer = 0
    while queue:
        workflow, high, low = queue.popleft()
        if workflow == "A":
            answer += prod(low[var] - high[var] + 1 for var in "xmas")
            continue
        if workflow == "R":
            continue
        for condition, to in workflows[workflow][:-1]:
            var = condition[0]
            op = condition[1]
            val = int(condition[2:])
            if high[var] < val < low[var]:
                match op:
                    case "<":
                        queue.append((to, {**high}, {**low, var: val - 1}))
                        high[var] = val
                    case ">":
                        queue.append((to, {**high, var: val + 1}, {**low}))
                        low[var] = val
                    case _:
                        raise ValueError(f"Unknown operator: {op!r}")
        to = workflows[workflow][-1][0]
        queue.append((to, high, low))
    return answer
