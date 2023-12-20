"""https://adventofcode.com/2023/day/20"""
from abc import ABC, abstractmethod
from collections import deque
from itertools import count
from math import lcm
from typing import Callable
from dataclasses import dataclass

from aoc import *


@dataclass
class State:
    node: "Node"
    caller: "Node"
    value: bool


class Node(ABC):
    name: str
    send_signal: Callable[[State], None]
    next: list["Node"] = None

    def __init__(self, name: str, send_signal: Callable[[State], None]):
        self.name = name
        self.send_signal = send_signal

    def init(self, next_nodes: list["Node"], previous_nodes: list["Node"]):
        self.next = next_nodes

    @abstractmethod
    def __call__(self, caller: "Node", value: bool):
        ...

    def send(self, value: bool):
        for node in self.next:
            self.send_signal(State(node, self, value))

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __eq__(self, other: "Node"):
        return self.name == other.name


class FlipFlop(Node):
    value = False

    def __call__(self, caller: Node, value: bool):
        if value:
            return
        self.value = not self.value
        self.send(self.value)


class Conjunction(Node):
    values: dict[Node, bool]

    def init(self, next_nodes: list[Node], previous_nodes: list[Node]):
        super().init(next_nodes, previous_nodes)
        self.values = {node: False for node in previous_nodes}

    def __call__(self, caller: Node, value: bool):
        self.values[caller] = value
        self.send(not all(self.values.values()))


class Broadcaster(Node):
    def __call__(self, caller: Node, value: bool):
        self.send(value)


class Noop(Node):
    def __init__(self, name: str = ""):
        super().__init__(name, lambda *args, **kwargs: None)

    def __call__(self, caller: Node, value: bool):
        pass


def parse(data: str, send_signal: Callable[[State], None]) -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    links: dict[Node, list[str]] = {}

    for line in data.splitlines():
        name, to = line.split(" -> ")
        if name == "broadcaster":
            node = Broadcaster(name, send_signal)
        else:
            kind = name[0]
            name = name[1:]
            match kind:
                case "%":
                    node = FlipFlop(name, send_signal)
                case "&":
                    node = Conjunction(name, send_signal)
                case _:
                    raise ValueError(f"Unknown kind: {kind!r}")
        nodes[name] = node
        links[node] = to.split(", ")

    for node in nodes.values():
        node.init([nodes.get(name, Noop(name)) for name in links[node]], [n for n, links in links.items() if node.name in links])

    return nodes


def links_to(nodes: dict[str, Node], node: Node) -> list[Node]:
    return [n for n in nodes.values() if node in n.next]


@solution(2023, 20, 1)
def part1(data: str) -> int:
    queue: deque[State] = deque()
    nodes = parse(data, queue.append)
    low = 0
    high = 0

    for _ in range(1000):
        queue.append(State(nodes["broadcaster"], Noop(), False))
        while queue:
            state = queue.popleft()
            if state.value:
                high += 1
            else:
                low += 1
            state.node(state.caller, state.value)

    return low * high


@solution(2023, 20, 2)
def part2(data: str) -> int:
    queue: deque[State] = deque()
    nodes = parse(data, queue.append)

    to_rx = links_to(nodes, Noop("rx"))
    assert len(to_rx) == 1
    assert isinstance(to_rx[0], Conjunction)

    previous = {}
    end = list(links_to(nodes, to_rx[0]))
    cycles = []
    for i in count(1):
        queue.append(State(nodes["broadcaster"], Noop(), False))
        while queue:
            state = queue.popleft()
            if not state.value:
                if state.node in previous and state.node in end:
                    cycles.append(i - previous[state.node])
                    if len(cycles) == len(end):
                        return lcm(*cycles)
                previous[state.node] = i
            state.node(state.caller, state.value)
