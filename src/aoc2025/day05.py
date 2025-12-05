from __future__ import annotations

import dataclasses
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from intervaltree import Interval, IntervalTree  # type: ignore[import-untyped]


@dataclass
class Database:
    fresh_id_ranges: IntervalTree = dataclasses.field(default_factory=IntervalTree)
    available_ids: list[int] = dataclasses.field(default_factory=list)

    @classmethod
    def parse(cls, strs: Sequence[str]) -> Database:
        database = cls()
        it = iter(map(str.strip, strs))
        for line in it:
            if not line:
                break
            first, last = map(int, line.split("-"))
            fresh_id_range = Interval(first, last + 1)
            database.fresh_id_ranges.add(fresh_id_range)
        database.available_ids.extend(map(int, it))
        return database


def part1(db: Database) -> int:
    count = 0
    for id in db.available_ids:
        if db.fresh_id_ranges[id]:
            count += 1
    return count


def part2(db: Database) -> int:
    db.fresh_id_ranges.merge_overlaps()
    count = 0
    for id_range in db.fresh_id_ranges:
        count += id_range.end - id_range.begin
    return count


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day05.txt") as file:
        database_strs = list(file)
    database = Database.parse(database_strs)
    count1 = part1(database)
    print(f"Part 1: {count1}")
    count2 = part2(database)
    print(f"Part 2: {count2}")
