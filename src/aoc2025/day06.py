from __future__ import annotations

import logging
import operator
from collections.abc import Sequence
from pathlib import Path

operators = {"+": operator.add, "*": operator.mul}


def part1(worksheet: Sequence[str]) -> int:
    rows = []
    for row_str in worksheet[:-1]:
        rows.append([int(cell) for cell in row_str.strip().split()])
    ops = [operators[cell] for cell in worksheet[-1].strip().split()]
    it = iter(rows)
    totals = next(it)
    for row in it:
        for i, (op, lhs, rhs) in enumerate(zip(ops, totals, row)):
            totals[i] = op(lhs, rhs)
    return sum(totals)


def part2(worksheet: Sequence[str]) -> int:
    columns = []
    column = []
    columns.append(column)
    for column_str in zip(*worksheet[:-1]):
        value_str = "".join(column_str).strip()
        if not value_str:
            column = []
            columns.append(column)
            continue
        column.append(int(value_str))
    ops = [operators[cell] for cell in worksheet[-1].strip().split()]
    total = 0
    for op, column in zip(ops, columns):
        it = iter(column)
        lhs = next(it)
        for rhs in it:
            lhs = op(lhs, rhs)
        total += lhs
    return total


if __name__ == "__main__":
    with open(Path(__file__).parent / "input" / "day06.txt") as file:
        worksheet = list(file)
    result1 = part1(worksheet)
    print(f"Part 1: {result1}")
    result2 = part2(worksheet)
    print(f"Part 2: {result2}")
