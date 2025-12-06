from __future__ import annotations

import logging
import math
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar


@dataclass(frozen=True)
class ProductIdRange:
    min: int
    max: int

    @classmethod
    def parse(cls, id_range_str: str) -> ProductIdRange:
        min_id, max_id = map(int, id_range_str.split("-"))
        return ProductIdRange(min_id, max_id)

    @classmethod
    def parse_list(cls, id_ranges_str: str) -> list[ProductIdRange]:
        id_range_strs = id_ranges_str.split(",")
        return [ProductIdRange.parse(id_range_str) for id_range_str in id_range_strs]

    def __post_init__(self) -> None:
        if self.min > self.max:
            raise ValueError(f"Invalid product ID range: {self.min} > {self.max}")

    @staticmethod
    def next_invalid_id(value: int) -> int:
        tens = math.floor(math.log10(value))
        if tens % 2 == 0:
            tens += 1
            value = 10**tens
        factor: int = 10 ** ((tens + 1) // 2)
        top = value // factor
        bottom = value % factor
        if top < bottom:
            top += 1
        return top * factor + top

    def invalid_ids(self) -> Iterator[int]:
        invalid_id = self.next_invalid_id(self.min)
        while invalid_id <= self.max:
            yield invalid_id
            invalid_id = self.next_invalid_id(invalid_id + 1)

    @staticmethod
    def all_invalid_ids(id_ranges: Iterable[ProductIdRange]) -> Iterator[int]:
        for id_range in id_ranges:
            yield from id_range.invalid_ids()


def part1(id_ranges_str: str) -> int:
    id_ranges = ProductIdRange.parse_list(id_ranges_str)
    return sum(ProductIdRange.all_invalid_ids(id_ranges))


def part2_scuffed(id_ranges_str: str) -> int:
    id_ranges = ProductIdRange.parse_list(id_ranges_str)
    pattern = re.compile(r"(\d+)\1+")  # Not even a regular expression!
    return sum(
        value
        for id_range in id_ranges
        for value in range(id_range.min, id_range.max + 1)
        if pattern.fullmatch(str(value)) is not None
    )


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day02.txt") as file:
        [id_ranges_str] = file
    total = part1(id_ranges_str)
    print(f"Part 1: {total}")
    total = part2_scuffed(id_ranges_str)
    print(f"Part 2: {total}")
