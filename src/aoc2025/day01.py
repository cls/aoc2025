from __future__ import annotations

import dataclasses
import logging
import re
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import ClassVar

logger = logging.getLogger(__name__)


class Direction(Enum):
    L = -1
    R = 1


@dataclass
class Rotation:
    pattern: ClassVar[re.Pattern[str]] = re.compile(
        r"(?P<direction>[LR])(?P<distance>\d+)"
    )

    direction: Direction
    distance: int

    @classmethod
    def parse(cls, rotation_str: str) -> Rotation:
        matchobj = cls.pattern.fullmatch(rotation_str)
        if matchobj is None:
            raise ValueError(f"Invalid rotation: {rotation_str!r}")
        direction_str, distance_str = matchobj.group("direction", "distance")
        direction = Direction[direction_str]
        distance = int(distance_str)
        return Rotation(direction, distance)

    def __str__(self) -> str:
        return f"{self.direction.name}{self.distance}"

    @property
    def value(self) -> int:
        return self.direction.value * self.distance


@dataclass
class Dial:
    size: ClassVar[int] = 100

    position: int = dataclasses.field(default=50)

    def __post_init__(self) -> None:
        logger.debug(f"The dial starts by pointing at {self.position}.")

    def rotate(self, rotation: Rotation) -> None:
        self.position = (self.position + rotation.value) % self.size
        logger.debug(f"The dial is rotated {rotation} to point at {self.position}.")

    def count_zeros(self, rotation: Rotation) -> int:
        origin = (self.size + self.position * rotation.direction.value) % self.size
        return (origin + rotation.distance) // self.size


def part1(document: Sequence[str]) -> int:
    password = 0
    dial = Dial()
    for line in document:
        rotation = Rotation.parse(line.strip())
        dial.rotate(rotation)
        if dial.position == 0:
            password += 1
    return password


def part2(document: Sequence[str]) -> int:
    password = 0
    dial = Dial()
    for line in document:
        rotation = Rotation.parse(line.strip())
        password += dial.count_zeros(rotation)
        dial.rotate(rotation)
    return password


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day01.txt") as file:
        document = list(file)
    password = part1(document)
    print(f"Part 1: {password}")
    password = part2(document)
    print(f"Part 2: {password}")
